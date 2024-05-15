from kivy.lang import Builder
from webview import WebView


class WebViewTest:
  def __init__(self):
    self.kv: WebView = Builder.load_file('pages/web_view_test/web_view_test.kv')
    