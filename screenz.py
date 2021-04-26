screen_nav = """
MDNavigationLayout:
    ScreenManager:
        id:manager
        MenuScreen:
        WeebScreen:
        SocialMediaScreen:
        InfoScreen:
        AndroidScreen:
        PythonScreen:
        FunScreen:
        TtsScreen:
        AppScreen:
    MDNavigationDrawer:
        id : test_nav
        bg: app.theme_cls.bg_darkest
        ScrollView:
            MDList:
                OneLineIconListItem:
                    text: "Menu"
                    on_press :
                        manager.current = 'menuscreen'
                    IconLeftWidget:
                        icon: "menu-open"

                OneLineIconListItem:
                    text: "WeebHub"
                    on_press :
                        manager.current = 'weebscreen'
                    IconLeftWidget:
                        icon: "heart"


                OneLineIconListItem:
                    text: "Information"
                    on_press :
                        manager.current = 'infoscreen'
                    IconLeftWidget:
                        icon: "information"


                OneLineIconListItem:
                    text: "Credits"
                    on_press :
                        manager.current = 'socials'
                    IconLeftWidget:
                        icon: "human-greeting"
                OneLineIconListItem:
                    text : 'Light/Dark-mode'
                    MDSwitch:
                        pos_hint : {'center_x' : .1 , 'center_y' : .5}
                        active : True
                        on_active : app.check(*args)
                OneLineIconListItem:
                    text: "FunArena"
                    on_press :
                        manager.current = 'funscreen'
                    IconLeftWidget:
                        icon: "cards-playing-outline"
                OneLineIconListItem:        
                    text: "Text-To-Speech"
                    on_press :
                        manager.current = 'ttsscreen'
                    IconLeftWidget:
                        icon: "speaker"
                OneLineIconListItem:        
                    text: "App-Launch"
                    on_press :
                        manager.current = 'appscreen'
                    IconLeftWidget:
                        icon: "apps"

<MenuScreen>:
    name : 'menuscreen'
    Image:
        source : 'res/image_new_screen.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDIconButton:
        icon : 'menu'
        pos_hint : {'center_x':.05 , 'center_y': .98}
        on_press:app.root.ids.test_nav.set_state("open")
    MDScreen:
        MDCard:
            orientation: "vertical"
            opacity: .7
            padding: "1dp"
            size_hint: None, None
            radius: [12]
            size: "280dp", "480dp"
            pos_hint: {"center_x": .5, "center_y": .5}

            MDLabel:
                text: "                  Howdy,Stranger!\\n\\nFeatures this app has:\\n-Text-To-Speech\\n-Weeb-Hub(For Anime Fans)\\n-Info About Android and Python\\n-Vibrativity\\n-Battery-Status\\n-AppLaunches including android  EasterEgg.\\n-Flash-ON/OFF"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]

            MDSeparator:
                height: "5dp"
            MDLabel:
                text: ''
            MDRectangleFlatButton:
                text : 'Fun-Options'
                on_press: root.manager.current = 'funscreen'                            
    MDFloatingActionButtonSpeedDial:
        data : app.data
        root_button_anim: True


<WeebScreen>:
    name: "weebscreen"
    Image :
        source : "res/image_anime.jpg"
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    Carousel:
        MDFloatLayout:
            MDRectangleFlatIconButton:
                icon : 'arrow-right'
                text : 'Swipe-->>'
                font_style : 'Body1'
                pos_hint: {"center_x": .5, "center_y": .97}
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: "280dp", "533dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Video:
                    id : vid_anime_amv
                    source : 'vid/anime_amv.mp4'
                    allow_stretch :True
                    options : {'eos': 'stop'}


                MDRoundFlatIconButton:
                    text : 'Tap To Play'
                    icon : 'play'
                    pos_hint: {'center_x': .5}
                    on_press:
                        setattr(vid_anime_amv, 'source', 'vid/anime_amv.mp4')
                        setattr(vid_anime_amv, 'state', 'play')


        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: "280dp", "535dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Video:
                    id : vid_obito
                    source : 'vid/obito.mp4'
                    allow_stretch :True
                    options : {'eos': 'stop'}


                MDRoundFlatIconButton:
                    text : 'Tap To Play'
                    icon : 'play'
                    pos_hint: {'center_x': .5}
                    on_press:
                        setattr(vid_obito, 'source', 'vid/obito.mp4')
                        setattr(vid_obito, 'state', 'play')
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: "280dp", "535dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Video:
                    id : vid_rinne
                    source : 'vid/naruto_rinne.mp4'
                    allow_stretch :True
                    options : {'eos': 'stop'}


                MDRoundFlatIconButton:
                    text : 'Tap To Play'
                    icon : 'play'
                    pos_hint: {'center_x': .5}
                    on_press:
                        setattr(vid_rinne, 'source', 'vid/naruto_rinne.mp4')
                        setattr(vid_rinne, 'state', 'play')
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: "280dp", "534dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Video:
                    id : naruto_minato_obito
                    source : 'vid/naruto_minato_obito.mp4'
                    allow_stretch :True
                    options : {'eos': 'stop'}


                MDRoundFlatIconButton:
                    text : 'Tap To Play'
                    icon : 'play'
                    pos_hint: {'center_x': .5}
                    on_press:
                        setattr(naruto_minato_obito, 'source', 'vid/naruto_minato_obito.mp4')
                        setattr(naruto_minato_obito, 'state', 'play')

    MDIconButton:
        icon :  "arrow-left-thick"
        on_press:app.root.ids.test_nav.set_state("open")
<SocialMediaScreen>:
    name : "socials"
    Image :
        source:'res/image_social.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDLabel:
        text:"Follow My Scoials ;)"
        theme_text_color :'Custom'
        text_color : ( 60/255.0, 109/255.0, 247/255.0,1)
        multiline : True
        font_style: "H4"
        pos_hint: {'center_x':0.6,'center_y':0.9}
    MDFloatingActionButton:
        icon :  "github"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press:
            import webbrowser
            url = "https://github.com/LIGHTNING283"
            webbrowser.open_new_tab(url)
    MDFloatingActionButton:
        icon :  "docker"
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press:
            import webbrowser
            url = "https://hub.docker.com/u/lightning283"
            webbrowser.open_new_tab(url)

    MDIconButton:
        icon :  "arrow-left-thick"
        on_press:app.root.ids.test_nav.set_state("open")
<InfoScreen>:
    name : 'infoscreen'
    Image:
        source : 'res/image_warrior.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDIconButton:
        icon : 'menu'
        pos_hint : {'center_x':.05 , 'center_y': .98}
        on_press:app.root.ids.test_nav.set_state("open")
    MDRectangleFlatIconButton:
        text : 'About Android'
        icon : 'android'
        pos_hint : {'center_x': .5 , 'center_y': .5}
        on_press : root.manager.current = 'screen_android'



    MDRectangleFlatIconButton:
        text : 'About Python'
        icon: 'language-python'
        pos_hint : {'center_x': .5 , 'center_y': .4}
        on_press : root.manager.current = 'pythonscreen'

<AndroidScreen>:
    name : 'screen_android'
    Image :
        source:'res/image_android.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDLabel:
        text:"What Is Android?"
        multiline : True
        font_style: "H4"
        theme_text_color :'Custom'
        text_color : ( 43/255.0, 196/255.0, 53/255.0,1)
        pos_hint: {'center_x':0.6,'center_y':0.94}
    MDLabel :
        text: "Android is an open source and Linux-based Operating System for mobile devices such as smartphones and tablet computers. Android was developed by the Open Handset Alliance, led by Google, and other companies.Android offers a unified approach to application development for mobile devices which means developers need only develop for Android, and their applications should be able to run on different devices powered by Android.The first beta version of the Android Software Development Kit (SDK) was released by Google in 2007 where as the first commercial version, Android 1.0, was released in September 2008.On June 27, 2012, at the Google I/O conference, Google announced the next Android version, 4.1 Jelly Bean. Jelly Bean is an incremental update, with the primary aim of improving the user interface, both in terms of functionality and performance.The source code for Android is available under free and open source software licenses. Google publishes most of the code under the Apache License version 2.0 and the rest, Linux kernel changes, under the GNU General Public License version 2."
        pos_hint: {'center_x':0.5,'center_y':0.47}
        multiline: True
        theme_text_color :'Custom'
        text_color : ( 249/255.0, 124/255.0, 30/255.0,1)
    MDIconButton:
        icon :  "arrow-left-thick"
        on_press : root.manager.current = 'infoscreen'



<PythonScreen>:
    name: 'pythonscreen'
    Image :
        source:'res/image_python.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDLabel :
        text : 'What is Python?'
        font_style : "H4"
        pos_hint: {'center_x':0.6,'center_y':0.94}
        theme_text_color :'Custom'
        text_color : ( 224/255.0, 45/255.0, 60/255.0,1)
    MDLabel:
        text: "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective. "
        multiline : True
        font_style : "Body2"
        pos_hint: {'center_x':0.5,'center_y':0.48}
        theme_text_color :'Custom'
        text_color : ( 249/255.0, 243/255.0, 83/255.0,1)
    MDIconButton:
        icon :  "arrow-left-thick"
        on_press : root.manager.current = 'infoscreen'

<FunScreen>:
    name : 'funscreen'
    Image:
        source : 'res/image_fun.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDRectangleFlatIconButton:
        text :'Check Battery'
        icon: 'battery'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press : app.info_battery()
        
    MDRectangleFlatIconButton:
        text: 'ShakeYourPhone'
        icon:'vibrate'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press : app.vibrate()
    MDIconButton:
        icon: 'menu'
        on_press:app.root.ids.test_nav.set_state("open")

    MDRectangleFlatIconButton:
        icon:'flash'
        text : 'flash-ON'
        pos_hint: {'center_x':0.3,'center_y':0.5}
        on_press:
            app.turn_on()
    MDRectangleFlatIconButton:
        icon:'flash'
        text : 'flash-OFF'
        pos_hint: {'center_x':0.7,'center_y':0.5}
        on_press:
            app.turn_off()

    MDRectangleFlatIconButton:
        icon:'android'
        text : 'Android-Easteregg'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:
            app.androidegg()

<TtsScreen>:
    name : 'ttsscreen'
    Image:
        source :'res/image_ai.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDTextField:
        id: text
        pos_hint: {'center_x':0.5,'center_y':0.8}
        hint_text: 'Text To Speech'
        size_hint_x : None
        icon_right : 'speaker'
        width: 500

    MDRectangleFlatIconButton:
        icon:'speaker'
        text : 'speak'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press:
            app.wait()
            app.speak(text.text)
    MDRectangleFlatIconButton:
        icon:'speaker'
        text : 'speak-V2'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press:
            app.wait()
            app.kvtts(text.text)
    MDIconButton:
        icon: 'menu'
        on_press:app.root.ids.test_nav.set_state("open")

<AppScreen>:
    name : 'appscreen'
    Image:
        source : 'res/image_app.jpg'
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        size_hint_x: None
        width: self.parent.width
        height: self.parent.width/self.image_ratio
    MDRectangleFlatIconButton:
        icon: 'whatsapp'
        text : 'Launch-WhatsApp'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: app.whatsapp()

    MDRectangleFlatIconButton:
        icon: 'youtube'
        text : 'Launch-YouTube'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: app.youtube()

    MDRectangleFlatIconButton:
        icon: 'facebook'
        text : 'Launch-FaceBook'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: app.facebook()
    MDIconButton:
        icon: 'menu'
        on_press:app.root.ids.test_nav.set_state("open")
"""