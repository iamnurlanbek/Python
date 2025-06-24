"""Task: JSON Parsing
write a Python script that reads the students.jon JSON file and prints details of each student.
"""

import json

with open(r'C:\Python\lesson-14\homework\students.json') as file:
    result = json.load(file)
    print(result)
    for student in result:
        print(f"\nName: {student['name']}\nAge: {student['age']}\nMajor: {student['major']}")



"""Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print 
relevant information (temperature, humidity, etc.).
"""

import requests
import pandas as pd


myapi = '3a6f50cf51b5dd565e38ce3b155b3077'
city = 'Tashkent'

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={myapi}")
if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    temp_kelvin = data['main']['temp']
    temp_celcius = temp_kelvin - 273.15
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    
    print(f'Weather Information:')
    print(f"City name: {city_name.capitalize()}")
    print('Weather:', description)
    print(f"Temprature: {temp_celcius:.2f}°C")
    print(f"Pressure: {pressure} Pa")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")
else:
    print('Ups, Error occured', response.status_code)
    
print('---------------------------------------------')
weather_info = {
    'city_name':[city_name],
    'temprature':[temp_celcius],
    'pressure':[pressure],
    'humidity':[humidity],
    'wind speed':[wind_speed],
    'description':[description]
}

df = pd.DataFrame(weather_info)
print(df)


"""Task: JSON Modification
Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file."""


"""Task: Movie Recommendation System
Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre."""








