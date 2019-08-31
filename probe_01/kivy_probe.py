# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import Python3Lexer

from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.scatter import Scatter

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


class MyApp(App):

    def build(self):

        # return CodeInput(lexer=Python3Lexer())

        fl = FloatLayout(size=(100, 100))
        fl.add_widget(Button(text='ХУЙ',
                             size_hint=(.5, .25),
                             pos=(160, 175),
                             font_size=100,
                             on_press=self.button_press,
                             background_color=[1, 0, 0, 1],
                             background_normal='')
                      )
        return fl

    def button_press(self, instance):
         print('хуяк!')
         instance.text = 'ЗАЕБИСЬ!!!!'


if __name__ == '__main__':
    MyApp().run()
