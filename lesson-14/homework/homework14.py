"""Task: JSON Parsing
write a Python script that reads the students.jon JSON file and prints details of each student.
"""

# import json

# students_data = [
#     {'name':'Ali', 'age':25, 'major':'Biology'},
#     {'name':'Salim', 'age':15, 'major':'History'},
#     {'name':'Tolib', 'age':45, 'major':'Math'},
#     {'name':'Botir', 'age':30, 'major':'Science'},
#     {'name':'Sodiq', 'age':19, 'major':'Law'}
# ]


# with open(r'students.json', mode='w') as file:
#     json.dump(students_data, file, indent=4)
    
# with open(r'C:\Python\lesson-14\homework\students.json', mode='r') as file:
#     json_date = json.load(file)
#     for date in json_date:
#         print(f"Name: {date['name']}, Age: {date['age']}, Major: {date['major']}\n")


"""Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print 
relevant information (temperature, humidity, etc.).
"""
import json
import requests
import datetime

myapi_key = 'dc76eb75a95459890a7d3d92123a0761'
city = 'Tashkent'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={myapi_key}&units=metric&lang=uz'

response = requests.get(url)
data = response.json()
print(data)




