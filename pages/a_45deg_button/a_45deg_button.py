from kivy.lang import Builder
from kivy.uix.button import Button


class A45degButton:
  def __init__(self):
    self.kv: Button = Builder.load_file('pages/a_45deg_button/a_45deg_button.kv')