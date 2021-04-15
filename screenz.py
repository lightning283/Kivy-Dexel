screen_nav = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    AndroidScreen:
    SocialMediaScreen:
    DownloadPicScreen:

<MenuScreen>:
    name: 'menu'
    Image : 
        source:'res/image_space.jpg'    
    # MDLabel :
    #     text : 'Click/Choose what you want to read about-->'
    #     font_style : "H4"
    #     pos_hint: {'center_x':0.5,'center_y':0.9}
    #     theme_text_color :'Custom'
    #     text_color : ( 224/255.0, 45/255.0, 60/255.0,1)
    MDFloatingActionButton:
        icon :  "android"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'screen_android'
    MDFloatingActionButton:
        icon :  "language-python"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'screen1'
    MDRectangleFlatButton:
        text : 'Python-Subprocess'
        on_press:
            import subprocess #to run any local commmands
            subprocess.call("" , shell=True)
    MDFloatingActionButton:
        icon :  "flash"
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'socials'
    MDFloatingActionButton:
        icon :  "camera-image"
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'downloadscreen'


<ProfileScreen>:
    name: 'screen1'
    Image : 
        source:'res/image_python.jpg'
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
    MDRectangleFlatButton:
        text : 'Go-Back'
        on_press: root.manager.current = 'menu'

<AndroidScreen>:
    name : 'screen_android'
    Image : 
        source:'res/image_android.jpg'
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
    MDFloatingActionButton:
        icon :  "arrow-left"
        on_press: root.manager.current = 'menu'
<SocialMediaScreen>:
    name : "socials"
    Image : 
        source:'res/image_social.jpg'
    MDLabel:
        text:"Follow My Scoials ;)"
        theme_text_color :'Custom'
        text_color : ( 60/255.0, 109/255.0, 247/255.0,1)
        multiline : True
        font_style: "H4"
        pos_hint: {'center_x':0.6,'center_y':0.9}
    MDFloatingActionButton:
        icon :  "gitlab"
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

    MDFloatingActionButton:
        icon :  "subdirectory-arrow-left"     
        on_press : root.manager.current = 'menu'


<DownloadPicScreen>:
    name: "downloadscreen"
    Image :
        source : "res/image_nature.jpg"
    Carousel:
        MDFloatLayout:
            MDRectangleFlatButton:
                text : 'Swipe-->'
                font_style : 'H4'
                pos_hint: {"center_x": .5, "center_y": .9}
            MDCard:
                orientation: "vertical"
                padding: "1dp"
                size_hint: None, None
                size: "280dp", "180dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Image :
                    source : "res/card_kitty.jpg"    
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: "1dp"
                size_hint: None, None
                size: "280dp", "180dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Image :
                    source : "res/card_house.png"
        MDFloatLayout:
            MDCard:
                orientation: "vertical"
                padding: "1dp"
                size_hint: None, None
                size: "280dp", "180dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                Image :
                    source : "res/card_biker.jpg"

    MDRectangleFlatButton:
        text : 'Go-Back'
        on_press: root.manager.current = 'menu'
"""
