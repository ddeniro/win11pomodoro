from winotify import Notification, audio
import time, sys, os
import pkg_resources
from infi.systray import SysTrayIcon

# def say_hello(systray):
#     print("Hello, World!")

def onQuit(systray):
    os._exit(1)

#menu_options = (("Say Hello", "test", say_hello), )


session_count = 1 # number of sessions continuously tracked.
session_time = 5 * 60 # Number of minutes to work.
break_time = 1 * 60 # Number of minutes break.

#Create each of our notifcation objects to send to Desktop using winotify library.
notif_endBreak = Notification(app_id="Pomodoro App", title="Break ended!", msg="Time to get back to work!", icon=r"a:/PomoTimer/terminal.png")
notif_endBreak.set_audio(audio.Mail, loop=False)

notif_startBreak = Notification(app_id="Pomodoro App", title=f"Work session {session_count} ended!", msg="Time to take a break.", icon=r"a:/PomoTimer/terminal.png")
notif_startBreak.set_audio(audio.Mail, loop=False)

notif_startSession = Notification(app_id="Pomodoro App", title=f"Work session {session_count} started.", msg="Timer has started, get to work!", icon=r"a:/PomoTimer/terminal.png")
notif_startSession.set_audio(audio.Mail, loop=False)

try:
    systray = SysTrayIcon("icon.ico", "Pomodoro Timer", on_quit=onQuit)
    systray.start()
    
    choice = 1

    while int(choice) != 0:

        notif_startSession.build().show()
        time.sleep(session_time)
        
        session_count += 1

        notif_startBreak.build().show()
        time.sleep(break_time)

    systray.shutdown()
except (KeyboardInterrupt, SystemExit):
    systray.shutdown()
    os._exit(1)