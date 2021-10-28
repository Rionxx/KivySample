from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

#Windows is C:\Windows\Fonts
#Mac is /System/Library/Fonts

resource_add_path('/System/Library/Fonts')

class TextApp(App):
  def build(self):
      return Label(text='Hello Kivy')

TextApp().run()