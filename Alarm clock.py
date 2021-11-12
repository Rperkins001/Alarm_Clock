import datetime
import time 
import webbrowser
from builtins import input

def get_hour():
    global hour_choice
    while True:
        hour_choice = input("Please select an hour for the alarm: ")
        if not hour_choice.isdigit():
            print("Error: You must input a numberic value.")
            continue
        hour_choice = int(hour_choice)
        
        if hour_choice >= 1 and hour_choice <= 12:
            break
        print("Error: Hour choice must be between 1-12.")

def get_minute():
    global minute_choice
    while True:
        minute_choice = input("Please select the minute for the alarm: ")
        if not minute_choice.isdigit():
            print("Error: You must input a numberic value.")
            continue
        minute_choice = int(minute_choice)
        
        if minute_choice >= 0 and minute_choice <= 59:
            break
        print("Error: Minute choice must be between 0-59.")
          
def get_meridiem():
    global mer
    valid_inputs = ["AM", "PM"]
    mer = input("Is that AM or PM?: ").upper()
    if mer not in valid_inputs:
        print("Error: You must choose between AM or PM.")
        return get_meridiem()

def countdown_clock():
    time_now = datetime.datetime.now()
    cc = int(input("How many minutes until alarm? "))
    global new_time
    time_change = datetime.timedelta(minutes = cc)
    new_time = time_now + time_change
    print(f'Alarm will activate at {new_time}.  Please wait.')
    clock_process()

def clock_process():
    time_now = datetime.datetime.now()
    if (time_now >= new_time):
        webbrowser.open('https://youtu.be/dQw4w9WgXcQ?t=43')
    else:
        time.sleep(1)
        clock_process()    

def alarm_clock():
    print("Please choose a time when the alarm should activate. ")
    hour = get_hour()
    minute = get_minute()
    meridiem = get_meridiem()
    print('Alarm Set.')

    clock_process2()

def clock_process2():
    time_now = datetime.datetime.now()
    a = [time_now.strftime("%I"), time_now.strftime("%M"), time_now.strftime("%p")]
    b = [str(hour_choice).zfill(2), str(minute_choice).zfill(2), str(mer)]
   
    if (a==b):
        webbrowser.open('https://youtu.be/dQw4w9WgXcQ?t=43')
    else:
        time.sleep(1)
        clock_process2()
  
def clock_type():
    valid_inputs2 = ["1", "2"]
    clock_choice = input("Please select clock format.  Press '1' for countdown or '2' to set time: ").lower()
    if clock_choice not in valid_inputs2:
        print("Error:  Please choose between 1 or 2")
        return clock_type()
    if clock_choice == str("1"):
        return countdown_clock()
    else:
        return alarm_clock()
    

clock_type()    
