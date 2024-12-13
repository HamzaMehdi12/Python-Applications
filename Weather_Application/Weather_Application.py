#Welcome to Weather Application using Python
#This App would contain a complete weather forecast with integration of AI based suggestions regarding weather
#Lets begin

import sys
import tkinter as tk
from tkinter import *
from urllib import response
import requests
import json
import datetime
from datetime import *

city_value = StringVar() #input value for city



def time_loc(time_and_location):
    local_time = datetime.utcfromtimestamp(time_and_location)
    return local_time.time()


def Weather(*args):
    tfield = Text(args, width=46, heigh=10)
    tfield.pack()
    api_key = "54c603a33903da833b269bdac97968d7" #freekeyfrom OpenWeather 
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key #API URL
    response = response.get(weather_url)#Getting respone from url
    weather_info = response.json() #converting json to python
    tfield.delete("1.0", "end") #clearing text field

    if weather_info['cod'] == 200:
        kelvin = 273
        
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['main']['speed']
        sunrise = weather_info['main']['sunrise']
        sunset = weather_info['main']['sunset']
        timezone_t = weather_info['timezone'] 
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_loc(sunrise + timezone_t)
        sunset_time = time_loc(sunset + timezone_t)

        weather = f'Weather of: {city_name}\nTemperature (Celcius): {temp}Åã\nFeels like (Celcius): {feels_like_temp}Åã\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at (time) and Sunset (time) at {sunrise_time} and {sunset_time}\nCloud: {cloudy}%\nInfo: {description}' 
        weather  = weather.encocode('utf-8')
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
#degree sign using Alt + 0176
    tfield.insert(INSERT, weather)




def Interface(*args):
    city_head = Label(args[0], text= 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #Label Heading
    inp_city = Entry(args[0], textvariable = args[1], width=24, font='Arial 14 bold').pack()
    Button(args[0], command = Weather, text = "Check Weather", font = "Arial 10", bg = 'Lightblue', fg = 'black', activebackground="teal", padx=5, pady=5).pack(pady=20)#to view output
    weather_now = Label(args[0], command = Weather, text = "Check Weather", font = "Arial 12 bold").pack(pady = 10)

def main():
    """
    This is the main function, all tasks would be initiated here
    Using root to initialize Tkinter

    Using root.mainloop to initialize the Application
    """
    root = Tk()
    root.geometry("600x600")#default window size
    root.resizable(0,0)
    root.title("Weather Application")
    Interface(root, city_value)
    root.mainloop()
    
if __name__ == "__main__":
    main()
