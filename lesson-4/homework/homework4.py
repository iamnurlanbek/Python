"""# Python Dictionary and Set Exercises
"""

"""1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
"""

info = {'a':5,'b':10,'c':88,'d':12,'x':0}

asc_sorted = dict(sorted(info.items(),key=lambda item:item[1]))
desc_sorted = dict(sorted(info.items(),key=lambda item:item[1],reverse=True))
print(asc_sorted)
print(desc_sorted)


"""2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.
Sample Dictionary:
{0: 10, 1: 20}
Expected Result:
{0: 10, 1: 20, 2: 30}"""

nums = {0:10, 1:20}
nums[2] = 30
print(nums)



"""3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionaries:

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
Expected Result:

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print(new_dic)



"""4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

Sample Dictionary (n = 5):

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

numbers = []
for i in range(1,5):
    numbers.append((i,i*i))
 
    
print(dict(numbers))



"""5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

Expected Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

numbers = []
for i in range(1,16):
    numbers.append((i,pow(i,2)))

numbers = dict(numbers)
print(numbers)


"""# 1. Create a Set
# Write a Python program to create a set.
"""

new_set = set()
my_set = {1, 2, 3, 4}


"""2. Iterate Over a Set
Write a Python program to iterate over sets."""

new_set = set([1, 2, 3, 4, 5])

for i in new_set:
    print(i)


"""3. Add Member(s) to a Set
Write a Python program to add member(s) to a set."""

new_set = set()
new_set.add('apple')
print(new_set)


"""4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set."""

new_set = {'apple','grape','melon'}
new_set.remove('apple')
# new_set.discard('melon')
print(new_set)

"""5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set."""

# new_set = {'apple','grape','melon','cherry'}
# element = 'apple'
# if element in new_set:
#     new_set.remove(element)
# else:
#     print("this element is not in set")
    
# print(new_set)