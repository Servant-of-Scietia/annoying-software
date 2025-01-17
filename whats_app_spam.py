#instructions: install vs code 
#install python
#run pip install pywhatkit
#register in whatsapp webbrowser 
#run the code

import pywhatkit as kit
from time import sleep
from datetime import datetime, timedelta



def send_whats_app_message(hour, minute):
    kit.sendwhatmsg("Enter number here", "Howdy, I'm Bob, and I sell hardware. Nice to meet you!", hour, minute, tab_close=True)


while True:
    # Get current time
    current_time = datetime.now()
    
    # Calculate the next minute
    next_minute = current_time + timedelta(minutes=1)
    
    # Call send_whats_app_message function with next minute's hour and minute
    send_whats_app_message(next_minute.hour, next_minute.minute)