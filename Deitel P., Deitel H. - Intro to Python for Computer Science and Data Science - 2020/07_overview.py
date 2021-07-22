import numpy as np
import random

# ----------------------------------------------------
# Views: Shallow Copies
# ----------------------------------------------------




# ----------------------------------------------------
# Indexing and Slicing
# ----------------------------------------------------
# grades = np.array([[87, 96, 70],[100, 87, 90],
#                     [94, 77, 90],[100, 81, 82]])

# print( grades[0,1] )

# print( grades[1] )

# print( grades[0:2] )

# print( grades[[1,3]] ) 
# # Output:
# #[[100  87  90]
# # [100  81  82]]

# print( grades[:, 0] ) # elements in the first column
# # Output:
# #[ 87 100  94 100]

# print( grades[:, 1:3] ) # select consecutive columns using slice
# # Output:
# # [[96 70]
# #  [87 90]
# #  [77 90]
# #  [81 82]]

# print( grades[:, [0,2]] ) # specific columns using a list of column indices
# # Output:
# # [[ 87  70]
# #  [100  90]
# #  [ 94  90]
# #  [100  82]]

# ----------------------------------------------------
# Universal Functions
# ----------------------------------------------------

# numbers = np.array([1,4,9,16,25,36])

# print( np.sqrt(numbers) )

# numbers2 = np.arange(1,7)*10

# print(numbers2)
# print( np.add(numbers, numbers2) )

# print( np.multiply(numbers2, 5) )

# numbers3 = numbers2.reshape(2,3)
# print(numbers3)

# numbers4 = np.array([2,4,6])

# print( np.multiply(numbers3, numbers4) )

# ----------------------------------------------------
# NumPy calculation Methods
# ----------------------------------------------------

# grades = np.array([[87, 96, 70],[100, 87, 90],
#                    [94, 77, 90],[100, 81, 82]])

# print( grades.sum() )
# print( grades.min() )
# print( grades.max() )
# print( grades.mean() )
# print( grades.std() )
# print( grades.var() )

# print( grades.mean(axis=0) ) # for each column
# print( grades.mean(axis=1) ) # for each row

# ----------------------------------------------------
# array Operators
# ----------------------------------------------------

# numbers = np.arange(1,6)
# print(numbers)
# print(numbers * 2)
# print(numbers ** 3)

# numbers += 10
# print(numbers)

# numbers2 = np.linspace(1.1,5.5,5)
# print(numbers2)
# print(numbers * numbers2)

# print(numbers)
# print(numbers >= 13)

# print(numbers2)
# print(numbers2 < numbers)
# print(numbers2 == numbers)
# print(numbers == numbers)


# ----------------------------------------------------
# List vs arrays Performance
# ----------------------------------------------------

# https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-timeit

# Run this command in console
# Shift+Enter = run comand instead new line
# \ is a line continueation character
# %timeit rolls_list = [random.randrange(1,7) \
# for i in range(0, 500_000)]
    
# # one-line version
# %timeit rolls_list = [random.randrange(1,7) for i in range(0, 500_000)]

# %timeit rolls_array = np.random.randint(1,7,500_000)

# %timeit -n3 -r2 rolls_array = np.random.randint(1,7,500_000)

# ----------------------------------------------------
# Creating arrays from Ranges
# ----------------------------------------------------
# print(np.arange(5))
# print(np.arange(5,10))
# print(np.arange(10,1,-2))

# print(np.linspace(0.0,1.0,num=5))

# print(np.arange(1,21).reshape(4,5))

# print(np.arange(1,100001).reshape(4,25000))
# print(np.arange(1,100001).reshape(100,1000))

# ---------------------------------------------------- 3
# print(np.zeros(5))
# print(np.ones((2,4), dtype=int))
# print(np.full((3,5), 13))

# ---------------------------------------------------- 2
# integers = np.array([[1,2,3],[4,5,6]])
# floats = np.array([0.0,0.1,0.2,0.3,0.4])

# print(integers.dtype)
# print(floats.dtype)
# print(integers.ndim)
# print(floats.ndim)
# print(integers.shape)
# print(floats.shape)
# print(integers.size)
# print(integers.itemsize)
# print(floats.size)
# print(floats.itemsize)

# for row in integers:
#     for column in row:
#         print(column, end=' ')
#     print()
    
# for i in integers.flat:
#     print(i, end=' ')

# ---------------------------------------------------- 1
# numbers = np.array([2,3,5,7,11])
# mdnumbers = np.array([[1,2,3],[4,5,6]])