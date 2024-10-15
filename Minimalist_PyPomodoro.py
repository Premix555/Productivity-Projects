import time
from win10toast import ToastNotifier
import msvcrt

notification = ToastNotifier()

def counter(t):
    print("\n")
    while t:
        mins=t//60
        secs=t%60
        display = '{:02d}:{:02d}'.format(mins, secs)
        print(display, end="\r")
        time.sleep(1)
        t-=1

def wait_for_input():
    print("Press any key to continue....")
    if msvcrt.kbhit():
        pomodoro_timer


def pomodoro_timer(): #Notification and Ui
    cycle=1
    while cycle:
        if cycle%4:
            print("Cycle Number :",cycle)
            print("\tPomodoro Started\nTake Break in....")
            notification.show_toast("Pomodoro Timer","Pomodoro Started, Focus..",duration=5)
            counter(study_time-5)
            wait_for_input()

            print("\n\tBreak Time!")
            notification.show_toast("Pomodoro Timer","Break Time!",duration=5)
            counter(break_time-5)
            wait_for_input()

        else:
            print("Cycle Number :",cycle)
            print("\tPomodoro Started\nTake Break in....")
            notification.show_toast("Pomodoro Timer","Pomodoro Started, Focus..",duration=5)
            counter(study_time-5)
            wait_for_input()
            print("\n\tLong Break Time!...chill")
            notification.show_toast("Pomodoro Timer","Long Break Time!",duration=5)
            counter(lbreak_time-5)
            wait_for_input()
        cycle+=1

print("\t_______POMODORO TIMER_______\n")

study_time=1500
break_time=300
lbreak_time=1500
print("Press 1 to start Pomodoro\nPress 2 to Customize Pomodoro Duration")
i=input("Enter here: ")
if '1'== i:
    print("Pomodoro Time:",study_time//60,"mins","\tBreak :",break_time//60,"mins\t","Long Break:",lbreak_time//60)
    pomodoro_timer()
elif '2'==i:
    study_time=int(input("Enter New Pomodoro Time in Minutes:"))*60 
    break_time=int(input("Enter Short Break Time in Minutes:"))*60 
    lbreak_time=int(input("Enter Long Break Time in Minutes:"))*60
    print("Changes Saved!")
    print("Pomodoro Time:",study_time//60,"mins","\tBreak :",break_time//60,"mins\t","Long Break:",lbreak_time//60)
    pomodoro_timer()
else:
    print("Please Enter only given character")
