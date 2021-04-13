screen_nav = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    AndroidScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel :
        text : 'what is -->'
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
            import subprocess
            subprocess.call("pm install /apks/hosts.apk" , shell=True)
            

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
    MDFloatingActionButton:
        icon :  "arrow-left"
        on_press: root.manager.current = 'menu'

"""
