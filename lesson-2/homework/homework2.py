"""1. Age Calculator
Write a Python program to ask for a user's name and year of birth, then calculate and display their age."""
import datetime
name = input('Enter your name: ')
year_of_birth = int(input('Enter your birth of date: '))
age = datetime.datetime.now().year - year_of_birth
print(f"{name.title()} is {age} years old.")


"""2. Extract Car Names
Extract car names from the following text:
txt = 'LMaasleitbtui'"""

txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]
print(f"The name of car1 is",car1)
print(f"The name of car1 is",car2)


"""3. Extract Car Names
Extract car names from the following text:
txt = 'MsaatmiazD'"""

txt = 'MsaatmiazD'
car1 = txt[::2]
car2 = txt[::-2]
print(f"Teh name of car2 is",car2)
print(f"The name of car1 is",car1)


"""4. Extract Residence Area
Extract the residence area from the following text:
txt = "I'am John. I am from London"""

txt = "I'am John. I am from London"
residence_area = txt[-6:]
print(residence_area)



"""5. Reverse String
Write a Python program that takes a user input string and prints it in reverse order.
"""

user = input("Please, enter a string: ")
print(user[::-1])


"""6. Count Vowels
Write a Python program that counts the number of vowels in a given string."""

given_string = input("Enter a string: ").lower()
count = 0
for i in given_string:
    if i in 'aeiou':
        count += 1
print(count)
        


"""7. Find Maximum Value
Write a Python program that takes a list of numbers as input and prints the maximum value.
"""
list_numbers = []
for num in range(5):
    number = int(input(f"Enter {num + 1} - number: "))
    list_numbers.append(number)
print(f"The max value is {max(list_numbers)}.")


"""8. Check Palindrome
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
"""

def palindrome(word):
    """Checking Palindrome"""
    if word == word[::-1]:
        return f"{word} is a palindrome word."
    else:
        return f"{word} is not a palindrome word."
print(palindrome('america'))

"""
9. Extract Email Domain
Write a Python program that extracts and prints the domain from an email address provided by the user.
"""

def email_domain(email):
    """Extract email domain"""
    domain = email[email.find('@') + 1:len(email)]
    return domain
print(email_domain('iamnurlanbek@gmail.com'))


"""10. Generate Random Password
Write a Python program to generate a random password containing letters, digits, and special characters."""
import string
def random_password(password):
    """Generate random password"""
    harf = any(value in string.ascii_letters for value in password)
    raqam = any(value in string.digits for value in password)
    belgi = any(value in '!@#$%' for value in password)
    
    if harf and raqam and belgi:
        return f"The passwor is valid"
    else:
        return f"The password is invalid"
print(random_password('Salom1'))