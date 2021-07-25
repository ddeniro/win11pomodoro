from winotify import Notification, audio
import time, sys
import pkg_resources
from infi.systray import SysTrayIcon

# def say_hello(systray):
#     print("Hello, World!")



#menu_options = (("Say Hello", "test", say_hello), )


#Function checkInput() which runs at the start of each while loop, it can be expanded in the case of other funcitonality/customization.
def checkInput(choice): 
    if choice == 'edit':
        editChoice = input("Enter [1] for editing session time, or [2] for break time.")
        if int(editChoice) == 1:
            session_time = int(input("Enter number of minutes for each session:")) * 60
        elif int(editChoice) == 2:
            break_time = int(input("Enter number of minutes for each break session:")) * 60


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
    systray = SysTrayIcon("icon.ico", "Pomodoro Timer")
    systray.start()
    #choice = input(f"Press anything to start session {session_count}:")
    choice = 1

    while int(choice) != 0:
        checkInput(choice)
        #print(f'Starting session {session_count} of {session_time // 60} minutes')
        notif_startSession.build().show()
        time.sleep(session_time)

        #print(f'Starting break of {break_time // 60} minutes')
        session_count += 1
        notif_startBreak.build().show()
        time.sleep(break_time)
        #print('Ending break! Get back to work!')

        notif_endBreak.build().show()
        #input('Enter 0 or q to end session or anything to continue:')
    

    systray.shutdown()
except (KeyboardInterrupt, SystemExit):
    systray.shutdown()


#input('enter to continue')