#Welcome to Weather Application using Python
#This App would contain a complete weather forecast with integration of AI based suggestions regarding weather
#Lets begin

import sys
import tkinter as tk
from tkinter import *
import requests
import json
import datetime
from datetime import *

def time_loc(time_and_location):
    local_time = datetime.utcfromtimestamp(time_and_location)
    return local_time.time()


def Weather():




def main():
    """
    This is the main function, all tasks would be initiated here
    Using root to initialize Tkinter
    """
    root = Tk()
    root.geometry("600x600")#default window size
    root.resizable(0,0)
    root.title("Weather Application")
    root.mainloop()
    
    city_value = StringVar() #input value for city



    
if __name__ == "__main__":
    main()
