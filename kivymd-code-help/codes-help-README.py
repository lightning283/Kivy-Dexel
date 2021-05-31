# Hello Stranger!!,
# Here are some useful code i've found in  my kivymd journey..
# These codes helped me a lot,hope they do the same to you!
# Oh yea,these code are from stackoverflow xD.
# To show the Image to Its full Length,stretch to fit.
Image:
    source: "res/card_house.png"
    allow_stretch: True
    keep_ratio: True
    size_hint_y: None
    size_hint_x: None
    width: self.parent.width
    height: self.parent.width/self.image_ratio


# Card Layout to Fit a simple Mp4 Video.
MDFloatLayout:
    MDCard:
        orientation: "vertical"  # give any (vertical or horizontal)
        size_hint: None, None
        size: "280dp", "535dp"  # size of the card
        pos_hint: {"center_x": .5, "center_y": .5}
        Video:
            id: vid_anime_amv  # give any name without ''
            source: ''
            allow_stretch: True
            options: {'eos': 'stop'}


on_press:  # button to control the video playback, this seem to work well with the code,even with the kivymd 'Video' moduel.
    setattr(vid_anime_amv, 'source', '##give source of the video here')
    setattr(vid_anime_amv, 'state', 'play')


# buildozer .spec file nessaccary reqs to have audio/video playback..
requirements = python3, kivy == 2.0.0, ffpyplayer, libshine, libx264, ffpyplayer_codecs, pillow, kivymd
# builozer .spec file reqs 2 with kivymd master repo
requirements = python3, kivy == 2.0.0, ffpyplayer, libshine, libx264, ffpyplayer_codecs, pillow, plyer, https: // github.com/kivymd/KivyMD/archive/master.zip, pygments, sdl2_ttf == 2.0.15

# buildozer required permissions.
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, VIBRATE

# Here is the compilation code for pyinstaller for a linux platform
pyinstaller - -noconfirm - -onefile - -windowed - -hidden-import "kivymd pillow" - -collect-submodules "kivy" - -collect-submodules "kivymd" - -collect-submodules "ffpyplayer" - -collect-submodules "gstreamer" - -collect-submodules "ffpyplayer_codecs" - -collect-submodules "pillow"  "main.py"
# Here is second version with icon.
pyinstaller - -noconfirm - -onefile - -windowed - -hidden-import "kivymd pillow" - -collect-submodules "kivy" - -collect-submodules "kivymd" - -collect-submodules "ffpyplayer" - -collect-submodules "gstreamer" - -collect-submodules "ffpyplayer_codecs" - -collect-submodules "pillow" - -icon "res/icon.ico" "main.py"
#new with ffpyplayer and plyer modules
pyinstaller --noconfirm --onefile --windowed --hidden-import "kivymd pillow" --collect-submodules "kivy" --collect-submodules "kivymd" --collect-submodules "ffpyplayer" --collect-submodules "gstreamer" --collect-submodules "ffpyplayer_codecs" --collect-submodules "pillow" --collect-submodules "plyer"  "main.py"
#to make presplash stay longer.edit line 398 in PythonActivity.java.
/home/lightning/Documents/compiler-zone/.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/src/main/java/org/kivy/android/
