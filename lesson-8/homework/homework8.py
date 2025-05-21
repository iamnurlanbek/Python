# # Homework:

# # Python Exception Handling: Exercises, Solutions, and Practice

# ## Exception Handling Exercises

"""1. Write a Python program to handle a `ZeroDivisionError` exception when dividing a number by zero.
"""

try:
    a = 20
    b = a/0
    print(b)
except ZeroDivisionError:
    print("Dividing by 0 is impossible")
finally:
    print('Closing....')


"""2. Write a Python program that prompts the user to input an integer and raises a `ValueError` exception if the input is not a valid integer.
"""

try:
    number = int(input('Enter number: '))
    print(f"You entered {number}")
except ValueError:
    print(f"Xatolik: You must enter a valid integer.")



"""3. Write a Python program that opens a file and handles a `FileNotFoundError` exception if the file does not exist.
"""

try:
    with open(r'C:\Python\lesson-8\homework\text.txt') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("This file do not exist. ")


"""4. Write a Python program that prompts the user to input two numbers and raises a `TypeError` exception if the inputs are not numerical.
"""

try:
    num1 = input('Enter number1: ')
    num2 = input('Enter number2: ')
    
    if  type(num1) != float or  type(num2) != float or type(num1) != int or  type(num2) != int:
        raise TypeError('Inputs must be numerical values ')
    
except TypeError as e:
    print(f"Error: {e}")



"""5. Write a Python program that opens a file and handles a `PermissionError` exception if there is a permission issue.
"""

try:
        with open('teft.txt', 'r') as f:
                data = f.read()
                print(data)
except Exception:
        print("Bu test uchun sun’iy xato")



"""6. Write a Python program that executes an operation on a list and handles an `IndexError` exception if the index is out of range.
"""

try:
    nums = [5, 7, 9, 8]
    print(nums[10])
except IndexError:
    print("Invalid index: Index is out of range.")



"""7. Write a Python program that prompts the user to input a number and handles a `KeyboardInterrupt` exception if the user cancels the input.
"""

try:
    number = int(input("Enter number: \n"))
    print(f"Entered number: {number}")
except KeyboardInterrupt:
    print('Error: user canceled the input')




"""8. Write a Python program that executes division and handles an `ArithmeticError` exception if there is an arithmetic error.
"""

try:
    num = -100
    print(num / 0) 
except ArithmeticError:
    print('Error: ArithmeticError')



"""9. Write a Python program that opens a file and handles a `UnicodeDecodeError` exception if there is an encoding issue.
"""


try:
    with open(r'C:\Python\lesson-8\homework\text.txt', encoding='ascii') as file:
        print(file.read())
except UnicodeDecodeError:
    print('Error: There is unreadable code.')



"""10. Write a Python program that executes a list operation and handles an `AttributeError` exception if the attribute does not exist.
"""
try:
    text = 225862
    print(text.append(8))
except AttributeError:
    print('Error: attribute does not exist')



# ---

# # Python File Input Output: Exercises, Practice, Solution

# ## File Input/Output Exercises

"""1. Write a Python program to read an entire text file.
"""

with open('entire.txt', mode='r') as file:
    content = file.read()
    print(content)
    
    


"""2. Write a Python program to read first `n` lines of a file.
"""

with open(r'C:\Python\lesson-8\homework\text.txt', mode='r') as file:
    for _ in range(2):
        line = file.readline()
        print(line)


"""3. Write a Python program to append text to a file and display the text.
"""
with open('book.txt', 'a') as file:
     file.write('Hello Python\n')
     
with open('book.txt') as file:
     content = file.read()
     print(content)
     
    

"""4. Write a Python program to read last `n` lines of a file.
"""

n = 3
with open('book.txt', 'r') as file:
    for line in file.readlines()[-n:]:
        print(line.strip())

            

"""5. Write a Python program to read a file line by line and store it into a list.
"""

with open('book.txt') as file:
    print(file.read())
    file.seek(0,0)
    lines = []
    for line in file:
        lines.append(line.strip())
    print(lines)
    


"""6. Write a Python program to read a file line by line and store it into a variable.
"""

with open('book.txt') as file:
    string = ''
    lines = file.readlines()
    file.seek(0, 0)
    for line in lines:
        string += line.strip() + ' '
    
    print(string)




"""7. Write a Python program to read a file line by line and store it into an array.
"""

with open('book.txt', mode='r+') as file:
    arr1 = []
    lines = file.readlines()
    file.seek(0, 0)
    for line in lines:
        arr1.append(line.strip())
    print(arr1)




"""8. Write a Python program to find the longest words.
"""

with open('book.txt') as file:
    lines = []
    print(file.read())
    file.seek(0, 0)
    for line in file:
        lines.append(line.strip())
    
    longhest_word = max(lines, key=len)
    print(longhest_word)



"""9. Write a Python program to count the number of lines in a text file.
"""

file = open('book.txt')
lines = []
for line in file:
    lines.append(line.strip())   
rows = len(lines)
print(rows)


"""10. Write a Python program to count the frequency of words in a file.
"""

from collections import Counter

with open('book.txt', 'r') as file:
    text = file.read()
    
words = text.lower().split()

word_freq = Counter(words)

for word, freq in word_freq.items():
    print(f"{word}: {freq}")



"""11. Write a Python program to get the file size of a plain file.
"""

with open('book.txt', mode='rb') as file:
    file.seek(0, 2)
    file_size = file.tell()
    print(file_size)



"""12. Write a Python program to write a list to a file.
"""
fruits = ['apple', 'grape', 'melon', 'watermelon', 'banana']
with open('book.txt', 'w') as file:
    for fruit in fruits:      
        file.write(fruit + '\n')



"""13. Write a Python program to copy the contents of a file to another file.
"""

with open('book.txt', 'r') as source_file:
    content = source_file.read()

with open('copy.txt', 'w') as dest_file:
    dest_file.write(content)  



"""14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
"""

with open('book.txt', 'r') as source_file:
    content1 = source_file.readlines()

with open('copy.txt', 'r') as source_file:
    content2 = source_file.readlines()

with open('new_file.txt', 'w') as new_file:
    for line1, line2 in zip(content1, content2):
        combined = new_file.write(f"{line1.strip()} - {line2.strip()}\n")
        print(combined)



"""15. Write a Python program to read a random line from a file.
"""
import random
with open('book.txt', 'r+') as file:
    lists = file.readlines()
    print(lists)
    result = random.choice(lists)
    print(result)


"""16. Write a Python program to assess if a file is closed or not.
"""
file = open('book.txt', 'r')   
print(file.closed)             

file.close()                  
print(file.closed)            



"""17. Write a Python program to remove newline characters from a file.
"""
with open(file='book.txt', mode='r+') as file:
    lines = file.readlines()
    for line in lines:
        print(line.rstrip('\n'))



"""18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
   - **Note:** Some words can be separated by a comma with no space.
# """

with open('book.txt', 'r') as file:
    lines = file.readlines()
    words = []

    for line in lines:
        clean_line = line.replace(',', ' ')
        words += clean_line.split()
    print(words)
    print(f"So‘zlar soni: {len(words)}")




"""19. Write a Python program to extract characters from various text files and put them into a list.
"""

with open('book.txt') as file:
    lines = file.readlines()
    
    
    new_list = []
    for line in lines:
        for l in line:
            if l != '\n':
                new_list.append(l)
    print(new_list)
        


"""20. Write a Python program to generate 26 text files named `A.txt`, `B.txt`, and so on up to `Z.txt`.
"""
import string
for harf in string.ascii_uppercase:
    with open(f"{harf}.txt", mode='w') as file:
        file.write(f"This is file {harf}.txt\n")


"""21. Write a Python program to create a file where all letters of the
English alphabet are listed with a specified number of letters on each line.
"""

import string

letters = string.ascii_uppercase
letters_per_line = 5

with open('text.txt', 'w') as file:
    for i in range(0, len(letters), letters_per_line):
        line = letters[i:i+letters_per_line]
        file.write(line + '\n')


       

        

