# Homework:

"""Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
"""




"""Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday."""

    



"""Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. 
Calculate and print the date and time when the meeting will end.
"""
# from datetime import datetime, timedelta

# input_datetime = input('Enter date and time (YYYY-MM-DD HH:MM:SS): ')

# try:
#     meeeting_datetime = datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S')
    
#     hours = int(input("Eneter duration of meeting in hours: "))
#     minutes = int(input("Eneter duration of meeting in minutes: "))
#     end_meeting = meeeting_datetime + timedelta(hours=hours, minutes=minutes)

# except ValueError:
#     print('Noto\'g\'ri formatda kiritildi.')
# else:
#     print(f"Meeting wiil end at: {end_meeting}")


"""Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, 
and then convert and print the date and time in another timezone of their choice.
"""
# from datetime import datetime
# import pytz

# try:
#     input_datetime = input('Enter date and time (YYYY-MM-DD HH:MM:SS): ')
#     formatted_datetime = datetime.strptime(input_datetime, '%Y-%m-%d %H:%M:%S')

#     current_tz = pytz.timezone(input('Enter your timezone (Region/City): '))
#     another_tz = pytz.timezone(input('Enter another timezone (e.g. America/New_York): '))

#     localized_tz = current_tz.localize(formatted_datetime)
#     converted_tz = localized_tz.astimezone(another_tz)

# except ValueError:
#     print(" Xatolik: Sana va vaqt formati noto‘g‘ri!")
    
# except pytz.UnknownTimeZoneError:
#     print(" Xatolik: Timezone nomi noto‘g‘ri!")
    
# else:
#     print(f" Local time:    {localized_tz.strftime('%Y-%m-%d %H:%M:%S')}")
#     print(f" Converted to: {converted_tz.strftime('%Y-%m-%d %H:%M:%S')}")
    
# finally:
#     print(" Jarayon yakunlandi.")





"""Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time,
and then continuously print the time remaining until that point in regular intervals (e.g., every second).
"""


        



"""Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email
format."""






"""Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. 
For example, convert "1234567890" to "(123) 456-7890".
"""
import re


phone_number = input('Enter phone number: ')

pattern = re.compile(r'(\d{3})(\d{3})(\d(4)')

print(f"{pattern.group(1)}")






# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).


# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text