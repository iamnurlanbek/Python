"""
Python Exam 
Question 1: Reverse String 
Write a Python program that prompts the user to enter a string and then prints the 
reversed version of that string. For example, if the user enters "Hello, World!", the 
program should output "!dlroW ,olleH". Ensure that your program handles the user's
"""


# string = input("Enter a string:  ")

# print(string[::-1])



"""
missing_number([3, 0, 1])   
# Output: [2] 
missing_number([9, 6, 4, 2, 3, 12, 5, 7, 0, 1])   
# Output: [8, 10, 11] 
# """


# def missing_number(lines):
#     new_lines = []
#     max_element = max(lines)
#     for i in range(0, max_element + 1):
#         if i not in lines:
#             new_lines.append(i)
            
#     return new_lines

# lines= [3, 0, 1]
# print(missing_number(lines))


"""
Question 3: Count vowels 
Write a Python function count_vowels_in_sentence(sentence) that uses a loop 
to count the number of vowels in a sentence. 
"""
# sentence = input('Enter a string: ')

# def count_vowels_in_sentence(sentence):
#     count = 0
#     for letter in sentence:
#         if letter.lower() in 'aeiou':
#             count += 1
            
#     return count

# print(count_vowels_in_sentence(sentence))



"""Question 4: Prime Number Generator """

# n = int(input("Enter a number: "))

# def is_prime(n):
#     primes = []

#     for son in range(2, n):
#         for x in range(2, son):
#             if son % x != 0:
#                  primes.append(n)
            
#     return primes
# print(is_prime(n))



