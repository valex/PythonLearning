import numpy as np
import random
import pandas as pd

# ----------------------------------------------------
# DataFrames (enhanced two-dimensional array)
# ----------------------------------------------------
grades_dict = {'Wally':[87,96,70], 'Eva':[100,87,90],
               'Sam':[94,77,90], 'Katie':[100,81,82],
               'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

print( grades )
# Output:
#    Wally  Eva  Sam  Katie  Bob
# 0     87  100   94    100   83
# 1     96   87   77     81   65
# 2     70   90   90     82   85
    
grades.index = ['Test1', 'Test2', 'Test3']
print( grades )
# Output:
#        Wally  Eva  Sam  Katie  Bob
# Test1     87  100   94    100   83
# Test2     96   87   77     81   65
# Test3     70   90   90     82   85

print( grades['Eva'] )
# Output:
# Test1    100
# Test2     87
# Test3     90
# Name: Eva, dtype: int64
    
print( grades.Sam )
# Output:
# Test1    94
# Test2    77
# Test3    90
# Name: Sam, dtype: int64

print( grades.loc['Test1'] ) # access a row RECOMMENDED
# Wally     87
# Eva      100
# Sam       94
# Katie    100
# Bob       83
# Name: Test1, dtype: int64

print( grades.iloc[1] ) # access a row by integer(i) index RECOMMENDED
# Wally    96
# Eva      87
# Sam      77
# Katie    81
# Bob      65
# Name: Test2, dtype: int64

# When using slices containing labels with loc, 
# the range specified includes the high index
print( grades.loc['Test1':'Test3'] ) 
#        Wally  Eva  Sam  Katie  Bob
# Test1     87  100   94    100   83
# Test2     96   87   77     81   65
# Test3     70   90   90     82   85

# When using slices containing integer indices with iloc, 
# the range you specify excludes the high index
print( grades.iloc[0:2] ) 
#        Wally  Eva  Sam  Katie  Bob
# Test1     87  100   94    100   83
# Test2     96   87   77     81   65

# To select specific rows use list rather than slice
print( grades.loc[['Test1','Test3']] ) 
#        Wally  Eva  Sam  Katie  Bob
# Test1     87  100   94    100   83
# Test3     70   90   90     82   85

print( grades.iloc[[0,2]] ) 
#        Wally  Eva  Sam  Katie  Bob
# Test1     87  100   94    100   83
# Test3     70   90   90     82   85

print( grades.loc['Test1':'Test2', ['Eva', 'Katie']] )
#        Eva  Katie
# Test1  100    100
# Test2   87     81

print( grades.iloc[[0,2], 0:3] ) 
#        Wally  Eva  Sam
# Test1     87  100   94
# Test3     70   90   90

print( grades[grades >= 90] ) 
#        Wally    Eva   Sam  Katie  Bob
# Test1    NaN  100.0  94.0  100.0  NaN
# Test2   96.0    NaN   NaN    NaN  NaN
# Test3    NaN   90.0  90.0    NaN  NaN

print( grades[(grades>=80) & (grades < 90)] ) 
#        Wally   Eva  Sam  Katie   Bob
# Test1   87.0   NaN  NaN    NaN  83.0
# Test2    NaN  87.0  NaN   81.0   NaN
# Test3    NaN   NaN  NaN   82.0  85.0

# use at and iat to get single value
print( grades.at['Test2', 'Eva'] ) 
# 87

print( grades.iat[2, 0] ) 
# 70

grades.at['Test2', 'Eva'] = 100
print( grades.at['Test2', 'Eva'] ) 
# 100
grades.iat[1, 1] = 87
print( grades.at['Test2', 'Eva'] )
# 87

print( grades.describe() )
#            Wally         Eva        Sam       Katie        Bob
# count   3.000000    3.000000   3.000000    3.000000   3.000000
# mean   84.333333   92.333333  87.000000   87.666667  77.666667
# std    13.203535    6.806859   8.888194   10.692677  11.015141
# min    70.000000   87.000000  77.000000   81.000000  65.000000
# 25%    78.500000   88.500000  83.500000   81.500000  74.000000
# 50%    87.000000   90.000000  90.000000   82.000000  83.000000
# 75%    91.500000   95.000000  92.000000   91.000000  84.000000
# max    96.000000  100.000000  94.000000  100.000000  85.000000

pd.set_option('precision', 2)
print( grades.describe() )
#        Wally     Eva    Sam   Katie    Bob
# count   3.00    3.00   3.00    3.00   3.00
# mean   84.33   92.33  87.00   87.67  77.67
# std    13.20    6.81   8.89   10.69  11.02
# min    70.00   87.00  77.00   81.00  65.00
# 25%    78.50   88.50  83.50   81.50  74.00
# 50%    87.00   90.00  90.00   82.00  83.00
# 75%    91.50   95.00  92.00   91.00  84.00
# max    96.00  100.00  94.00  100.00  85.00

print( grades.mean() )
# Wally    84.33
# Eva      92.33
# Sam      87.00
# Katie    87.67
# Bob      77.67
# dtype: float64

print( grades.T ) # T returns view, not a copy
#        Test1  Test2  Test3
# Wally     87     96     70
# Eva      100     87     90
# Sam       94     77     90
# Katie    100     81     82
# Bob       83     65     85


print( grades.T.describe() )
#         Test1  Test2  Test3
# count    5.00   5.00   5.00
# mean    92.80  81.20  83.40
# std      7.66  11.54   8.23
# min     83.00  65.00  70.00
# 25%     87.00  77.00  82.00
# 50%     94.00  81.00  85.00
# 75%    100.00  87.00  90.00
# max    100.00  96.00  90.00

print( grades.T.mean() )
# Test1    92.8
# Test2    81.2
# Test3    83.4
# dtype: float64

# sort rows by index
# returns copy
print( grades.sort_index(ascending=False) )
#        Wally  Eva  Sam  Katie  Bob
# Test3     70   90   90     82   85
# Test2     96   87   77     81   65
# Test1     87  100   94    100   83

# sort columns by index
print( grades.sort_index(axis=1) ) # for rows use axis=0, default
#        Bob  Eva  Katie  Sam  Wally
# Test1   83  100    100   94     87
# Test2   65   87     81   77     96
# Test3   85   90     82   90     70

# sort based on column values (axis=1) for 'Test1'
# returns copy
print( grades.sort_values(by='Test1', axis=1, ascending=False) ) 
#        Eva  Katie  Sam  Wally  Bob
# Test1  100    100   94     87   83
# Test2   87     81   77     96   65
# Test3   90     82   90     70   85

print( grades.T.sort_values(by='Test1', ascending=False) ) 
#        Test1  Test2  Test3
# Eva      100     87     90
# Katie    100     81     82
# Sam       94     77     90
# Wally     87     96     70
# Bob       83     65     85

print( grades.loc['Test1'].sort_values(ascending=False) )
# Eva      100
# Katie    100
# Sam       94
# Wally     87
# Bob       83
# Name: Test1, dtype: int64

# inplace sorting
grades.sort_index(ascending=False, inplace=True)
print( grades )
#        Wally  Eva  Sam  Katie  Bob
# Test3     70   90   90     82   85
# Test2     96   87   77     81   65
# Test1     87  100   94    100   83

grades.sort_values(by='Test1', axis=1, ascending=False, inplace=True)
print( grades )
#        Eva  Katie  Sam  Wally  Bob
# Test3   90     82   90     70   85
# Test2   87     81   77     96   65
# Test1  100    100   94     87   83

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
