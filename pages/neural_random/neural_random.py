from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random as random_lib


class NeuralRandom:
  def __init__(self):
    self.kv: BoxLayout = Builder.load_file('pages/neural_random/neural_random.kv')
    self.random_label: Label = self.kv.ids.random_label
    self.random_button: Button = self.kv.ids.random_button
    self.random_button.on_press = self.generate_number

  def generate_number(self):
    self.random_label.text = str(random_lib.randint(0, 1000))
    