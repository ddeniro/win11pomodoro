from winotify import Notification, audio
import time, sys, os
import pkg_resources
from infi.systray import SysTrayIcon
from configparser import ConfigParser

def readConfig():
    config = ConfigParser()
    config.read('notify.cfg')
    session_time = float(config.get('config', 'session_time'))
    break_time = float(config.get('config', 'break_time'))
    return session_time * 60, break_time * 60

session_time, break_time = readConfig()

def say_hello(systray):
    print("Hello, World!")
#Function which exits program, accessible by right clicking the systray
def onQuit(systray):
    os._exit(1)

# incrementTime(): increments the number of minutes 

def testing():
    pass


menu_options = (("Say Hello", None, say_hello),
                ("testing", None, testing))

session_count = 1 # number of sessions continuously tracked.

#Create each of our notifcation objects to send to Desktop using winotify library.

notif_startBreak = Notification(app_id="Pomodoro App", title=f"Work session {session_count} ended!", msg="Time to take a break.", icon=r"a:/PomoTimer/terminal.png")
notif_startBreak.set_audio(audio.Mail, loop=False)

notif_startSession = Notification(app_id="Pomodoro App", title=f"Work session {session_count} started.", msg="Timer has started, get to work!", icon=r"a:/PomoTimer/terminal.png")
notif_startSession.set_audio(audio.Mail, loop=False)

try:
    #Create the system tray icon
    systray = SysTrayIcon("icon.ico", "Pomodoro Timer", on_quit=onQuit, menu_options=menu_options)
    systray.start()
    #Main Pomodoro loop.
    while True:

        #Start the Pomodoro work session
        notif_startSession.build().show()
        systray.update(hover_text=f'Work Session {session_count}')
        time.sleep(session_time)

        #Start break session
        notif_startBreak.build().show()
        systray.update(hover_text=f'Break Session {session_count}')
        session_count += 1
        notif_startBreak.title = f"Work session {session_count} ended!"
        notif_startSession.title=f"Work session {session_count} started."
        time.sleep(break_time)

except (KeyboardInterrupt, SystemExit):
    systray.shutdown()
    os._exit(1)