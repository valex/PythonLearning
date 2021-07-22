import numpy as np
import random
import pandas as pd

# ----------------------------------------------------
# DataFrames (enhanced two-dimensional array)
# ----------------------------------------------------


# ----------------------------------------------------
# Series (enhanced one-dimensional array)
# ----------------------------------------------------

# grades = pd.Series([87, 100, 94])

# print( grades )
# # Output:
# # 0     87
# # 1    100
# # 2     94
# # dtype: int64

# print( pd.Series(98.6, range(3)) )
# # Output:
# # 0    98.6
# # 1    98.6
# # 2    98.6
# # dtype: float64

# print( grades[0] )
# print( grades.count() )
# print( grades.mean() )
# print( grades.min() )
# print( grades.max() )
# print( grades.std() )

# print( grades.describe() )
# # Output:
# # count      3.000000
# # mean      93.666667
# # std        6.506407
# # min       87.000000
# # 25%       90.500000
# # 50%       94.000000
# # 75%       97.000000
# # max      100.000000
# # dtype: float64

# grades = pd.Series([87,100,94], index=["Wally", "Eva", "Sam"])
# print( grades )
# # Output:
# # Wally     87
# # Eva      100
# # Sam       94
# # dtype: int64

# grades = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})
# print( grades )
# # Output:
# # Wally     87
# # Eva      100
# # Sam       94
# # dtype: int64

# print( grades['Eva'] )
# print( grades.Wally )

# print( grades.dtype )

# print( grades.values )
# # Output:
# # [ 87 100  94]


# hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
# print(hardware)
# # Output:
# # 0    Hammer
# # 1       Saw
# # 2    Wrench
# # dtype: object

# print( hardware.str.contains('a') )
# # Output:
# # 0     True
# # 1     True
# # 2    False
# # dtype: bool

# print( hardware.str.upper() )
# # Output:
# # 0    HAMMER
# # 1       SAW
# # 2    WRENCH
# # dtype: object

# ----------------------------------------------------
# Reshaping and Transposing
# ----------------------------------------------------

# grades = np.array([[87,96,70],[100,87,90]])

# # reshape returns a view. It does not modify the original array
# print( grades.reshape(1,6) )
# print( grades )
# # Output:
# # [[ 87  96  70 100  87  90]]
# # [[ 87  96  70]
# #  [100  87  90]]

# # resize modifies the original array's shape
# grades.resize(1,6)
# print( grades )
# # Output:
# # [[ 87  96  70 100  87  90]]

# # flatten deep copies the original array's data
# grades = np.array([[87,96,70],[100,87,90]])
# flattened = grades.flatten()
# print( flattened )
# print( grades )
# # Output:
# # [ 87  96  70 100  87  90]
# # [[ 87  96  70]
# #  [100  87  90]]

# # ravel returns a view
# raveled = grades.ravel()
# print( raveled )
# # Output:
# # [ 87  96  70 100  87  90]

# raveled[0] = 100
# print( raveled )
# print( grades )
# # Output:
# # [100  96  70 100  87  90]
# # [[100  96  70]
# #  [100  87  90]]


# # T attribute returns a transposed view
# # transposing - rows become the columns and the columns become the rows
# print( grades.T )
# print( grades )
# # Output:
# # [[100 100]
# #  [ 96  87]
# #  [ 70  90]]
# # [[100  96  70]
# #  [100  87  90]]



# grades2 = np.array([[94,77,90],[100,81,82]])

# # horizontal stack
# print( np.hstack((grades, grades2)) )  
# # Output:
# # [[100  96  70  94  77  90]
# #  [100  87  90 100  81  82]]

# # vertical stack
# print( np.vstack((grades, grades2)) ) 
# # Output:
# # [[100  96  70]
# #  [100  87  90]
# #  [ 94  77  90]
# #  [100  81  82]]

# ----------------------------------------------------
# Deep Copies
# ----------------------------------------------------

# numbers = np.arange(1,6)

# numbers2 = numbers.copy()

# numbers[1] *= 10

# print(numbers)
# print(numbers2)
# # Output:
# # [ 1 20  3  4  5]
# # [1 2 3 4 5]

# ----------------------------------------------------
# Views: Shallow Copies
# ----------------------------------------------------

# numbers = np.arange(1,6)

# print( numbers )

# numbers2 = numbers.view()

# print( numbers2 )

# print( id(numbers) )
# print( id(numbers2) )

# numbers[1] *= 10
# print( numbers )
# print( numbers2 )

# numbers2[1] /= 10
# print( numbers2 )
# print( numbers )

# # Slices also create views
# numbers2 = numbers[0:3]
# print( numbers2 )

# numbers[1] *= 20
# print( numbers )
# print( numbers2 )
# # Output:
# #[ 1 40  3  4  5]
# #[ 1 40  3]


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