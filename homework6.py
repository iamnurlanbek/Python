"""1. Modify String with Underscores
Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character.
No underscore should be added at the end.

Examples
Input: hello Output: hel_lo

Input: assalom Output: ass_alom

Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abc_dab_cdab_cdef"""
def insert_underscore(txt):
    result = ""
    count = 0
    vowels = 'aeiou'

    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                result += txt[i + 1] if i + 1 < len(txt) else ''
                result += '_'
                i += 1  
            else:
                result += '_'
            count = 0
        i += 1
        
    return result.rstrip('_')

print(insert_underscore("hello"))         
print(insert_underscore("assalom"))         
print(insert_underscore("abcabcabcdeabcdefabcdefg"))  






"""The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
"""
n = int(input("Enter number:"))
for number in range(0,n):
    print(number ** 2)



"""Exercise 1: Print first 10 natural numbers using a while loop"""

one = 1
eleven = 11

while one < eleven:
    print(one)
    one += 1
    
"""Print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
    

"""Exercise 3: Calculate sum of all numbers from 1 to a given number
"""

given_num = int(input("Eneter a number: "))
sum = 0
start = 1

while start <= given_num:
    sum += start
    start += 1
    
print(sum)


"""Exercise 4: Print multiplication table of a given number
"""

given_number = int(input("Enter a number: "))


start = 1
while start <= given_number:
    print(f"{given_number} * {start} = {given_number * start}")
    start += 1


"""Exercise 5: Display numbers from a list using a loop
"""
    
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    print(num)


"""Exercise 6: Count the total number of digits in a number
"""

given_number = int(input('Enter a number: '))

count = 0
for digit in str(given_number):
    if digit.isdigit():
        count += 1
print(count)


"""Exercise 7: Print reverse number pattern
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1"""


for i in range(1,6):
    for j in reversed(range(i+1,7)):
        print(j-i, end=' ')
    print()


"""Exercise 8: Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]"""

list1 = [10, 20, 30, 40, 50]

for num in reversed(list1):
    print(num)



"""Exercise 9: Display numbers from -10 to -1 using a for loop
"""

for num in range(-10,0):
    print(num)


"""Exercise 10: Display message “Done” after successful loop execution

"""

given_number = int(input('Enter a number: '))

for num in range(given_number):
    print(num)
else:
    print('Done!')


"""Exercise 11: Print all prime numbers within a range
"""

start_number = int(input("Enter start number: "))
end_number = int(input("Enter end number: "))

for number in range(start_number, end_number):
    if number == 1:
        continue
    for num in range(2,number):
        if number % num == 0:
            break
    else:
        print(number)    



"""Exercise 12: Display Fibonacci series up to 10 terms
Example:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34"""

n = int(input("Nechta Fibonacci soni kerak? "))
a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    fib = a + b
    a = b
    b = fib


    
"""Exercise 13: Find the factorial of a given number
Example: 5! = 120"""


given_number = int(input('Enter a number: '))

def factorial_hisoblash(given_number):
    factorial = 1
    for num in range(1,given_number + 1):
        factorial *= num
    return factorial

print(factorial_hisoblash(given_number))
    
    
"""4. Return Uncommon Elements of Lists
Task
Return the elements that are not common between two lists. The order of elements does not matter.

Examples
Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
Output: [1, 1, 3, 4]

Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
Output: [2, 2, 5]"""

list1 = [1, 1, 2]
list2 = [2, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

new_list = []
for i in list1:
    if i not in list2:
        new_list.append(i)

for j in list2:
    if j not in list1:
        new_list.append(j)
            
print(new_list)


    