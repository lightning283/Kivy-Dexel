screen_nav = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    AndroidScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel :
        text : 'Choose what you want to read about'
    MDFloatingActionButton:
        icon :  "android"
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'screen_android'
    MDFloatingActionButton:
        icon :  "language-python"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'screen1'
    MDRectangleFlatButton:
        text : 'LightMode'
        on_press:
            import subprocess #to run any local commmands
            subprocess.call("" , shell=True)


<ProfileScreen>:
    name: 'screen1'
    MDLabel:
        text: "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective. "
        multiline : True
        halign: 'center'
    MDRectangleFlatButton:
        text : 'Go-Back'
        on_press: root.manager.current = 'menu'

<AndroidScreen>:
    name : 'screen_android'
    MDLabel : 
        text: "Android is an open source and Linux-based Operating System for mobile devices such as smartphones and tablet computers. Android was developed by the Open Handset Alliance, led by Google, and other companies.Android offers a unified approach to application development for mobile devices which means developers need only develop for Android, and their applications should be able to run on different devices powered by Android.The first beta version of the Android Software Development Kit (SDK) was released by Google in 2007 where as the first commercial version, Android 1.0, was released in September 2008.On June 27, 2012, at the Google I/O conference, Google announced the next Android version, 4.1 Jelly Bean. Jelly Bean is an incremental update, with the primary aim of improving the user interface, both in terms of functionality and performance.The source code for Android is available under free and open source software licenses. Google publishes most of the code under the Apache License version 2.0 and the rest, Linux kernel changes, under the GNU General Public License version 2."
        multiline: True
    MDFloatingActionButton:
        icon :  "arrow-left"
        on_press: root.manager.current = 'menu'

"""
