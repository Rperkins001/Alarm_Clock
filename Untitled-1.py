import datetime
from builtins import input
from time import sleep
import webbrowser


x = datetime.datetime.now()
xnow = (x.strftime("%I:%M%p"))

print(xnow)

time_now = datetime.datetime.now()
print(time_now)

time_change = datetime.timedelta(minutes=600)
new_time = time_now + time_change
print(new_time)

def get_hour():
    while True:
        hour_choice = input("Please select an hour for the alarm:")
        if not hour_choice.isdigit():
            print("Error: You must input a numberic value.")
            continue
        hour_choice = int(hour_choice)
        
        if hour_choice >= 1 and hour_choice <= 12:
            break
        print("Error: Hour choice must be between 1-12.")

def get_minute():
    while True:
        minute_choice = input("Please select the minute for the alarm:")
        if not minute_choice.isdigit():
            print("Error: You must input a numberic value.")
            continue
        minute_choice = int(minute_choice)
        
        if minute_choice >= 0 and minute_choice <= 59:
            break
        print("Error: Minute choice must be between 0-59.")
          
def get_meridiem():
    valid_inputs = ["am", "pm"]
    mer = input("Is that AM or PM?:").lower()
    if mer not in valid_inputs:
        print("Error: You must choose between AM or PM.")
        return get_meridiem()

def set_alarm_time():
    print("Please choose a time when the alarm should activate.")
    hour = get_hour()
    minute = get_minute()
    meridiem = get_meridiem()
    
    a = (x.strftime("%I,"), x.strftime("%M"), x.strftime("%p"))
    b = (hour, minute, meridiem)
  
  



set_alarm_time()
