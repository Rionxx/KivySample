#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

#Windows is C:\Windows\Fonts
#Mac is /System/Library/Fonts

resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'ヒラギノ角ゴシック W0.ttc')

class TextApp(App):
  def build(self):
      return Label(text='皆さん、こんにちは、今入力中です')

TextApp().run()