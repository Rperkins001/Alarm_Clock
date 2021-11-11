import datetime
from builtins import input
from time import sleep
import webbrowser




def get_hour():
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
    valid_inputs = ["am", "pm"]
    mer = input("Is that AM or PM?: ").lower()
    if mer not in valid_inputs:
        print("Error: You must choose between AM or PM.")
        return get_meridiem()

def countdown_clock():
    cc = int(input("How many minutes until alarm? "))
    time_change = datetime.timedelta(minutes = cc)
    new_time = time_now + time_change
    print(time_change)
    while True:
        if time_now >= new_time:
            print('done')
        else:
            continue
        time.sleep(1)  



def alarm_clock():
    time_now = datetime.datetime.now()
    print("Please choose a time when the alarm should activate. ")
    hour = get_hour()
    minute = get_minute()
    meridiem = get_meridiem()

    a = [time_now.strftime("%I,"), time_now.strftime("%M"), time_now.strftime("%p")]
    b = [hour, minute, meridiem]
    while True:
        if a == b:
            print('done')
        else:
            continue
        time.sleep(1)       
  
  
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
