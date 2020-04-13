#!/usr/bin/kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty

from kivy.app import App


class MenuScreen(Screen):
    pass

class PlayGameScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


sm = Builder.load_file('SimpleKivy.kv')

class SimpleKivy(App):
    def build(self):
        return sm

if __name__== '__main__':
    SimpleKivy().run()