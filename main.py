#!/bin/python
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFloatingActionButton , MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from screenz import screen_nav
import subprocess

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class AndroidScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(ProfileScreen(name="screen1"))
sm.add_widget(AndroidScreen(name="android"))

class RezApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_nav)
        return screen


RezApp().run()
