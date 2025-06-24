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

# from datetime import datetime
# import time

# user_input = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")

# future_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

# while True:
#     now = datetime.now()
#     remaining_time = future_time - now

#     if remaining_time.total_seconds() <= 0:
#         print("Time's up!")
#         break


#     days = remaining_time.days
#     hours, remainder = divmod(remaining_time.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     print(f"Time remaining: {days} days, {hours:02}h:{minutes:02}m:{seconds:02}s", end='\r')

#     time.sleep(1)

        



"""Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email
format."""

# import re

# email = input('Enter yout email: ').strip()

# pattern = re.compile(r"[a-zA-Z0-9._+%-]+\@[a-zA-Z0-9_-]+\.[a-z]{2,}")

# result = pattern.fullmatch(email)
# if result:
#     print(f"Your email: {result.group()}")
# else:
#     raise ValueError("Error: This is not a valid email format")



"""Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. 
For example, convert "1234567890" to "(123) 456-7890".
"""

# import re

# number = input('Enter numer: ')
# cleaned = re.sub(r'\D', '', number)

# pattern = re.compile(r"(\d{3})(\d{3})(\d{4})")

# result = pattern.fullmatch(cleaned)

# if result:  
#     formatted = f"Format: ({result.group(1)}) {result.group(2)}-{result.group(3)}"
#     print(f"Format:", formatted)
# else:
#     print("Error: Please enter a 10-digit phone number.")





"""Password Strength Checker: Implement a password strength checker. 
Ask the user to input a password and check if it meets certain criteria 
(e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
"""
# import re

# user_password = input('Enter a password: ')

# if len(user_password) < 8:
#     print("The length of password must be minimum 8 characters")
# elif not re.search(r"[a-z]", user_password):
#     print("Password must be minimum 1 lower letter")
# elif not re.search(r"[A-Z]", user_password):
#     print("Password must be minimum 1 upper letter")
# elif not re.search(r"[0-9]", user_password):
#     print("Password must be minimum 1 digit")
# else:
#     print(f"Your password is {user_password}")


"""Word Finder: Develop a program that finds all occurrences of a specific word in a given text.
Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
"""
# import re

# user_text = input("Enter a text: ")
# user_word = input("Enter a word: ")


# pattern = re.compile(rf"\b{re.escape(user_word)}\b", re.IGNORECASE)

# result = pattern.findall(user_text)

# if result:
#     print(f"'{user_word}' so‘zi {len(result)} marta topildi:")
#     print(result)
# else:
#     print(f"'{user_word}' topilmadi.")


"""
Date Extractor: Write a program that extracts dates from a given text. 
Ask the user to input a text, and then identify and print all the dates present in the text
"""
# import re

# text = input("Enter a text: ")

# pattern = re.compile(r'\b(?:\d{4}[-/\.]\d{2}[-/\.]\d{2}|\d{2}[-/\.]\d{2}[-/\.]\d{4}|[A-Za-z]+\s\d{1,2},\s\d{4})\b')

# dates = pattern.findall(text)

# if dates:
#     print("Found dates:", dates)
# else:
#     print("No dates found.")
