from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Main:
  def __init__(self):
    self.layout: FloatLayout = Builder.load_file('main.kv')
    self.button: Button = self.layout.children[0]

  def configure(self, text = ""):
    self.button.text = text
    return self

class SuperApp(App):
  def build(self):
    main = Main().configure(text="Hello, World!")
    return main.layout

SuperApp().run()