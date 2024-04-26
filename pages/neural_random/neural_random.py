from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class NeuralRandom:
  def __init__(self):
    self.kv = Builder.load_file('pages/neural_random/neural_random.kv')