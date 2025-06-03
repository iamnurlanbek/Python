"""1. Convert List to 1D Array
Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

Expected Output:

Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

"""
import numpy as np
nums_list = [12.23, 13.32, 100, 36.32]
nums_array = np.array(nums_list)

print("Original List:", nums_list)
print("One-dimensional NumPy array:", nums_array)




"""
2. Create 3x3 Matrix (2?10)
Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

Expected Output:

[[ 2 3 4] [ 5 6 7] [ 8 9 10]]"""

import numpy as np
array = np.arange(2, 11).reshape(3,3)
print("3x3 Matrix with values from 2 to 10:\n", array)

"""3. Null Vector (10) & Update Sixth Value
Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]"""

import numpy as np
zeros_array = np.zeros(10)

print("Original null vector:")
print(zeros_array)

zeros_array[6] = 11

print("Updated vector (6th value to 11):")
print(zeros_array)

"""4. Array from 12 to 38
Write a NumPy program to create an array with values ranging from 12 to 38.

Expected Output:

[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
"""

import numpy as np
array = np.arange(12,38)

print(f"Array from 12 to 38:\n{array}")


"""
5. Convert Array to Float Type
Write a NumPy program to convert an array to a floating type.

Sample output:

Original array [1, 2, 3, 4]
"""
import numpy as np

array = np.array([1, 2, 3, 4])
float_array = array.astype(float)

print(f"Original array: {array}")
print(f"Float array: {float_array}")

"""6. Celsius to Fahrenheit Conversion
Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

Expected Output:

Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]

Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]

Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]"""


import numpy as np

celsius1 = np.array([0, 12, 45.21, 34, 99.91])
celsius2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ])


fahrenheit1 = (9/5) * celsius1 + 32
fahrenheit2 = (9/5) * celsius2 + 32

print("Values in Celsius degrees:", celsius1)
print("Values in Fahrenheit degrees:", fahrenheit1)

print("Values in Celsius degrees:", celsius2)
print("Values in Fahrenheit degrees:", fahrenheit2)


"""
7. Append Values to Array (Do self-tudy)
Write a NumPy program to append values to the end of an array.

Expected Output:

Original array: [10, 20, 30]

After append values to the end of the array: [10 20 30 40 50 60 70 80 90]
"""

import numpy as np

nums = [10, 20, 30]
nums_array = np.array(nums)
print(f"Original Array: {nums_array}")
nums_array = np.append(nums_array, [40, 50, 60, 70, 80, 90])
print(f"Fianl Array: {nums_array}")


"""8. Array Statistical Functions (Do self-tudy)
Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array
# """
import numpy as np
array = np.random.randint(0, 10, 10)

print(array)
mean_array = sum(array)/len(array)
print(f"Mean:", mean_array)
print('----------------')

sorted_array = sorted(array)
median_array =  (sorted_array[4] + sorted_array[5])/2.0
print(f"Median: {median_array}")
print('----------------')

mean = mean_array
summa = 0
for num in array:
    summa += (num - mean) ** 2

standard_deviation = np.sqrt(summa / len(array))
print(f"Standard deviation: {standard_deviation}")
    



"""9 Find min and max
Create a 10x10 array with random values and find the minimum and maximum values.
"""
import numpy as np

array = np.random.randint(0, 100, (10, 10))
print(array)
min_value = np.min(array)
max_value = np.max(array)
print(f"Min value: {min_value}")
print(f"max value: {max_value}")



"""10
Create a 3x3x3 array with random values.
"""
import numpy as np

array3d = np.random.randint(0, 100, (3, 3, 3))
print(f" 3x3x3 array:", array3d)