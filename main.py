#!/bin/python
import shutil
import os
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatButton, MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList
from plyer import battery, vibrator, brightness, tts , flash
from kivymd.uix.dialog import MDDialog
from kivy.utils import platform
from screenz import screen_nav

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE,
                        Permission.WRITE_EXTERNAL_STORAGE,
                        Permission.CAMERA,
                        Permission.SET_WALLPAPER])

if platform == 'android':
    from kvdroid import statusbar_color
    statusbar_color("#1e95ed","black")

if platform == 'android':
    import time
    time.sleep(6)
    from kvdroid import toast
    toast("App Is Loading This May Take Some Time...")


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


class AppScreen(Screen):
    pass

class WallScreen(Screen):
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
sm.add_widget(AppScreen(name='appscreen'))
sm.add_widget(WallScreen(name='wallscreen'))


class RezApp(MDApp):
    data = {
        'Built with :': 'language-python'
    }
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_nav)
        return screen
    def speak(self, text_to_read):
        tts.speak(text_to_read)
    def check(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
    def info_battery(self):
        dialog = MDDialog(title='Battery Status', text=str(battery.status))
        dialog.open()
    def wait(self):
        dialog = MDDialog(title='Wait a few seconds', text=(
            "so that this tts can configure\nfor the first time.\n\nclick to dismiss"))
        dialog.open()
    def vibrate(self):
        vibrator.vibrate()
    def turn_on(self):
        flash.on()
    def turn_off(self):
        flash.off()
    def whatsapp(self):
        from kvdroid import launch_app
        launch_app('com.whatsapp', 'com.whatsapp.HomeActivity')
    def youtube(self):
        from kvdroid import launch_app
        launch_app('com.google.android.youtube', 'com.google.android.youtube.HomeActivity')
    def facebook(self):
        from kvdroid import launch_app
        launch_app('com.facebook.katana', 'com.facebook.katana.LoginActivity')
    def instagram(self):
        from kvdroid import launch_app
        launch_app('com.instagram.android', 'com.instagram.mainactivity.LauncherActivity')
    def androidegg(self):
        from kvdroid import launch_app
        launch_app('com.android.egg', 'com.android.egg.octo.Ocquarium')
    def walls(self):
        if platform == "android":
            from kvdroid import set_wallpaper
            set_wallpaper("/sdcard/anime_itachi.jpg")
    def walls2(self):
        if platform == "android":
            from kvdroid import set_wallpaper
            set_wallpaper("/sdcard/image_anime.jpg")
    def cpfiles(self):
        if platform == "android":
            check=os.path.isfile("/sdcard/wallpapers/move.kv")
            if check == True:
                print("The files exist..wont do anything.")
            else:
                original = r'wallpapers'
                target = r'/sdcard/wallpapers'
                shutil.copytree(original, target)

RezApp().run()
