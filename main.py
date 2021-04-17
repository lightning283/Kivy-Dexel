#!/bin/python
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFloatingActionButton , MDRectangleFlatButton , MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.video import Video
from screenz import screen_nav

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class AndroidScreen(Screen):
    pass

class SocialMediaScreen(Screen):
    pass

class DownloadPicScreen(Screen):
    pass
class NavScreenz(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(ProfileScreen(name="screen1"))
sm.add_widget(AndroidScreen(name="android"))
sm.add_widget(SocialMediaScreen(name="socials"))
sm.add_widget(DownloadPicScreen(name="downloadscreen"))
sm.add_widget(NavScreenz(name='navv'))


class RezApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_nav)
        return screen
RezApp().run()
