"""# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
"""
fruits = ['apple','melon','watermelon','grape','avacado']
third_element = fruits[2]
print(third_element)

"""# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list
"""
nums_list1 = [1, 2, 3, 4, 5]
nums_list2 = [6, 7, 8, 9]
merge_list = nums_list1 + nums_list2
print(merge_list)


"""# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
"""
nums_list = [5, 8, 9, 45, 12, 45, 100]
new_nums_list = []
first_element = nums_list[0]
middle_element = nums_list[len(nums_list)//2]
last_element = nums_list[-1]

new_nums_list.append(first_element)
new_nums_list.append(middle_element)
new_nums_list.append(last_element)

print(new_nums_list)




"""# # 4. Convert List to Tuple
# # Create a list of your five favorite movies and convert it into a tuple.
"""
movies = ['Insteller','Forsaj','Troya','Hacker','Blackberry']
movies = tuple(movies)
print(movies)



"""# # 5. Check Element in a List
# # Given a list of cities, check if "Paris" is in the list and print the result.
"""

def check_city(cities):
    if 'Paris' in cities:
        return f"Paris in the cities list"
    else:
        return f"Paris is not in cities list"
    
cities = ['Paris','London','Berlin','Munich']
print(check_city(cities))



"""# # 6. Duplicate a List Without Using Loops
# # Create a list of numbers and duplicate it without using loops.
"""
numbers = [5, 8, 9, 41, 99]
duplicated_numbers = numbers.copy()
print(duplicated_numbers)


"""# # 7. Swap First and Last Elements of a List
# # Given a list of numbers, swap the first and last elements.
"""
numbers = [5, 10, 15, 25, 45, 99]
numbers = tuple(numbers)
numbers = (numbers[-1],) + numbers[1:-1] + (numbers[0],)
print(list(numbers))



"""# # 8. Slice a Tuple
# # Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
"""
numbers = tuple(range(1,11))
sliced_numbers = numbers[3:7]
print(sliced_numbers)


"""# # 9. Count Occurrences in a List
# # Create a list of colors and count how many times "blue" appears in the list.
"""
colors = ['blue','red','yellow', 'blue','pink','blue']
print(colors.count('blue'))


"""# # 10. Find the Index of an Element in a Tuple
# # Given a tuple of animals, find the index of "lion".
"""
animals = ('lion','tiger','bear','zebra')
print(animals.index('lion'))


"""# # 11. Merge Two Tuples
# # Create two tuples of numbers and merge them into a single tuple.
"""
numbers1 = (5, 8, 9, 15)
numbers2 = (6, 18, 29, 25)


def merge_tuples(numbers1, numbers2):
    return numbers1 + numbers2

print(merge_tuples(numbers1, numbers2))


"""# # 12. Find the Length of a List and Tuple
# # Given a list and a tuple, find and print their lengths.
"""
lists = [8, 15, False, '','apple',[5, 8]]
tuples = (8, 15, False, '','apple',[5, 8], (5, 18))
print(len(lists))
print(len(tuples))


"""# # 13. Convert Tuple to List
# # Create a tuple of five numbers and convert it into a list
"""
numbers = (5, 88, 99, 101, 550)
numbers = list(numbers)
print(numbers)



"""# # 14. Find Maximum and Minimum in a Tuple
# # Given a tuple of numbers, find and print the maximum and minimum values.
"""
numbers = (101, 500, 158, 499, 0)

def max_min_value(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    
    print(f"Max_value: {max_value}")
    print(f"Min_value: {min_value}")
    
max_min_value(numbers)




"""# # 15. Reverse a Tuple
# # Create a tuple of words and print it in reverse order.
"""
words = ('apple','grape','melon','watermelon','lemon')

words = list(words)

words.reverse()
print(tuple(words))
