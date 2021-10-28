#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from random import randint

#change font that use default
resource_add_path('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT, 'PingFang.ttc')

resource_add_path('./images')

class ImageWidget(Widget):
  source = StringProperty('./images/01.jpg')

  def __init__(self, **kwargs):
      super(ImageWidget, self).__init__(**kwargs)
      pass

  def buttonStarted(self):
    self.source = './images/01.jpg'
  
  def buttonRandom(self):
    self.source = f'0{ randint(1, 5) }.jpg'

class MonsterApp(App):
  def __init__(self, **kwargs):
      super(MonsterApp, self).__init__(**kwargs)
      self.title = 'モンスター表示'

if __name__ == '__main__':
  MonsterApp().run()