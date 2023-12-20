# A simple ChatBot using Python 
from calendar import calendar
import sys
from datetime import datetime
inputs = ""
name = "Shabana"
while ("exit" or "quit" not in inputs):
    inputs = input("Text Here: ")
    if ("Hello" in inputs):
        print("Hi Shabana,What can I do for you? ")
    elif ("name" in inputs):
        print("My name is Akupaak")
    elif ("not good" in inputs):
        print("Oh,i am sorry to hear that, Anyway have a good day by putting some smile on your face")
    elif ("calendar" in inputs):
        year = int(input("Year please "))
        print(calendar(year))
    elif ("time" in inputs):
        print(datetime.now())
    elif ("Info" in inputs):
        print(sys.version)
        print(sys.version_info)
    elif "exit" or "quit" in inputs:
        print("Thank you for talking")
        break

    
    