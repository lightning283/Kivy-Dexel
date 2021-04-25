#!/bin/python
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFloatingActionButton , MDRectangleFlatButton , MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from plyer import battery,vibrator,brightness,tts
from kivymd.uix.dialog import MDDialog
from kivy.uix.effectwidget import EffectWidget
from screenz import screen_nav
class MenuScreen(Screen):
    pass

class WeebScreen(Screen):
    pass

class SocialMediaScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class AndroidScreen(Screen):
	pass

class PythonScreen(Screen):
	pass

class FunScreen(Screen):
	pass
class TtsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name="menuscreen"))
sm.add_widget(WeebScreen(name="weebscreen"))
sm.add_widget(SocialMediaScreen(name="socials"))
sm.add_widget(InfoScreen(name='infoscreen'))
sm.add_widget(AndroidScreen(name='screen_android'))
sm.add_widget(PythonScreen(name='pythonscreen'))
sm.add_widget(FunScreen(name='funscreen'))
sm.add_widget(TtsScreen(name='ttsscreen'))


class RezApp(MDApp):
    data = {
        'Built with :': 'language-python'
            }
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_nav)
        return screen
    def speak(self ,text_to_read):
        tts.speak(text_to_read)


    def check(self, checkbox,value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def info_battery(self):
    	dialog = MDDialog(title = 'Battery Status', text = str(battery.status))
    	dialog.open()

    def vibrate(self):
    	vibrator.vibrate()

    def set_brightness(self, level):
        brightness.set_level(level)

    def get_current_brightness(self):
        return brightness.current_level()
RezApp().run()
