import pywhatkit as kit
import time
import pyautogui
import keyboard as k

# Target phone number (include the country code without any leading zeros)
phone_number = "+919511766929"

# Message content
message = "Hello from PyWhatKit!"

# Get the current time
current_time = datetime.datetime.now().time()
print("Current Time:", current_time)
# Get the current hour, minute, and second
hour = current_time.hour
minute = current_time.minute
second = current_time.second
print(minute)
print(second)
# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute+1)
pyautogui.click(1050, 950)
time.sleep(40)
k.press_and_release('enter') 
