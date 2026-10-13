import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

# Этот плейсхолдер заменит workflow на реальный URL
SITE_URL = "SITE_URL_PLACEHOLDER"

if platform == "android":
    from jnius import autoclass
    from android.runnable import run_on_ui_thread

    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')

    class WebViewApp(App):
        def build(self):
            self.create_webview()
            return BoxLayout()

        @run_on_ui_thread
        def create_webview(self):
            activity = Activity.mActivity
            webview = WebView(activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.getSettings().setDomStorageEnabled(True)
            webview.getSettings().setLoadWithOverviewMode(True)
            webview.getSettings().setUseWideViewPort(True)
            webview.setWebViewClient(WebViewClient())
            webview.loadUrl(SITE_URL)
            lp = LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)
            activity.addContentView(webview, lp)
else:
    class WebViewApp(App):
        def build(self):
            return BoxLayout()

WebViewApp().run()
