from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pages.neural_random.neural_random import NeuralRandom
from pages.a_45deg_button.a_45deg_button import A45degButton


class Main:
  def __init__(self):
    self.kv: BoxLayout = Builder.load_file('main.kv')
    self.buttons_box_layout: BoxLayout = self.kv.children[0]

class SuperApp(App):
  def build(self):
    main = Main()
    pages = [
      NeuralRandom(),
      A45degButton()
    ]
    for page in pages:
      button = Button()
      button.text = type(page).__name__

      def button_on_press(page):
        main.kv.remove_widget(main.kv.children[0])
        main.kv.add_widget(page.kv)

      button.on_press = lambda page=page: button_on_press(page)
      main.buttons_box_layout.add_widget(button)
    main.kv.add_widget(pages[0].kv)
    return main.kv
  
SuperApp().run()