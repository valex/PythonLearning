import os
import json
import csv
from numpy import histogram
import pandas as pd

# ----------------------------------------------------
# Titanic
#
# Datasets
# https://vincentarelbundock.github.io/Rdatasets/
# https://github.com/awesomedata/awesome-public-datasets
#
#
# R datasets directly in Python
# https://github.com/iamaziz/PyDataset
# ----------------------------------------------------

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')

print( titanic.head() )
#                         Unnamed: 0 survived     sex      age passengerClass
# 0    Allen, Miss. Elisabeth Walton      yes  female  29.0000            1st
# 1   Allison, Master. Hudson Trevor      yes    male   0.9167            1st
# 2     Allison, Miss. Helen Loraine       no  female   2.0000            1st
# 3  Allison, Mr. Hudson Joshua Crei       no    male  30.0000            1st
# 4  Allison, Mrs. Hudson J C (Bessi       no  female  25.0000            1st

print( titanic.tail() )
#                      Unnamed: 0 survived     sex   age passengerClass
# 1304       Zabour, Miss. Hileni       no  female  14.5            3rd
# 1305      Zabour, Miss. Thamine       no  female   NaN            3rd
# 1306  Zakarian, Mr. Mapriededer       no    male  26.5            3rd
# 1307        Zakarian, Mr. Ortin       no    male  27.0            3rd
# 1308         Zimmerman, Mr. Leo       no    male  29.0            3rd

titanic.columns=['name','survived','sex','age','class']

print( titanic.head() )
#                               name survived     sex      age class
# 0    Allen, Miss. Elisabeth Walton      yes  female  29.0000   1st
# 1   Allison, Master. Hudson Trevor      yes    male   0.9167   1st
# 2     Allison, Miss. Helen Loraine       no  female   2.0000   1st
# 3  Allison, Mr. Hudson Joshua Crei       no    male  30.0000   1st
# 4  Allison, Mrs. Hudson J C (Bessi       no  female  25.0000   1st

print( titanic.describe() )
#                age
# count  1046.000000
# mean     29.881135
# std      14.413500
# min       0.166700
# 25%      21.000000
# 50%      28.000000
# 75%      39.000000
# max      80.000000

print( (titanic.survived=='yes').describe() )
# count      1309
# unique        2
# top       False
# freq        809
# Name: survived, dtype: object


# ----------------------------------------------------
# Working with CSV files
# https://docs.python.org/3/library/csv.html
# ----------------------------------------------------


# # load csv

# df = pd.read_csv('accounts.csv', names=['account','name','balance'])
# print( df ) 
# #    account   name  balance
# # 0      100  Jones    24.98
# # 1      200    Doe   345.67
# # 2      300  White     0.00
# # 3      400  Stone   -42.16
# # 4      500   Rich   224.62

# # save csv
# df.to_csv('accounts_from_dataframe.csv', index=False)


# # Read

# with open('accounts.csv', 'r', newline='') as accounts:
#     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
#     reader = csv.reader(accounts)
#     for record in reader:  
#         account, name, balance = record
#         print(f'{account:<10}{name:<10}{balance:>10}')
# # Account   Name         Balance
# # 100       Jones          24.98
# # 200       Doe           345.67
# # 300       White            0.0
# # 400       Stone         -42.16
# # 500       Rich          224.62

# # Write

# with open('accounts.csv', mode='w', newline='') as accounts:
#     writer = csv.writer(accounts)
#     writer.writerow([100, 'Jones', 24.98])
#     writer.writerow([200, 'Doe', 345.67])
#     writer.writerow([300, 'White', 0.00])
#     writer.writerow([400, 'Stone', -42.16])
#     writer.writerow([500, 'Rich', 224.62])



# ----------------------------------------------------
# Raising Exceptions
# ----------------------------------------------------

# def function1():
#     function2()
    
# def function2():
#     raise Exception('An exception occurred')

# # function1()


# ----------------------------------------------------
# finally Clause
# ----------------------------------------------------

# try:
#     print('try suite with no exceptions raised')
# except:
#     print('this will not execute')
# else:
#     print('else executes because no exceptions in the try suite')
# finally:  
#     print('finally always executes')
# # try suite with no exceptions raised
# # else executes because no exceptions in the try suite
# # finally always executes

# try:
#     print('try suite that raises an exception')
#     int('hello')
#     print('this will not execute')
# except ValueError:
#     print('a ValueError occurred')
# else:
#     print('else will not execute because an exception occurred')
# finally:  
#     print('finally always executes')
# # try suite that raises an exception
# # a ValueError occurred
# # finally always executes
    
# # Combining with Statements and try…except Statements 

# try:
#     with open('gradez.txt', 'r') as accounts:
#         print(f'{"ID":<3}{"Name":<7}{"Grade"}')
#         for record in accounts:  
#             student_id, name, grade = record.split()
#             print(f'{student_id:<3}{name:<7}{grade}')
# except FileNotFoundError:
#     print('The file name you specified does not exist')
# # The file name you specified does not exist

# ----------------------------------------------------
# Handling Exceptions
# https://docs.python.org/3/tutorial/errors.html
# ----------------------------------------------------

# while True:
#     # attempt to convert and divide values
#     try:
#         number1 = int(input('Enter numerator: '))
#         number2 = int(input('Enter denominator: '))
#         result = number1 / number2
#     except ValueError:  # tried to convert non-numeric value to int
#         print('You must enter two integers\n')
#     except ZeroDivisionError:  # denominator was 0
#         print('Attempted to divide by zero\n')
#     else:  # executes only if no exceptions occur
#         print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
#         break  # terminate the loop



# ----------------------------------------------------
# Serialization with JSON
# https://docs.python.org/3/library/json.html
# ----------------------------------------------------

# accounts_dict = {'accounts': [
#     {'account': 100, 'name':'Jones', 'balance':24.98},
#     {'account': 200, 'name':'Doe', 'balance':345.67}
# ]}

# with open('accounts.txt', 'w') as accounts:
#     json.dump(accounts_dict, accounts)

# with open('accounts.txt', 'r') as accounts:
#     accounts_json = json.load(accounts)

# print(accounts_json)
# # {'accounts': [{'account': 100, 'name': 'Jones', 'balance': 24.98}, {'account': 200, 'name': 'Doe', 'balance': 345.67}]}

# print(accounts_json['accounts'])
# # [{'account': 100, 'name': 'Jones', 'balance': 24.98}, {'account': 200, 'name': 'Doe', 'balance': 345.67}]

# print(accounts_json['accounts'][0])
# # {'account': 100, 'name': 'Jones', 'balance': 24.98}

# print(accounts_json['accounts'][1])
# # {'account': 200, 'name': 'Doe', 'balance': 345.67}

# with open('accounts.txt', 'r') as accounts:
#     print( json.dumps(json.load(accounts), indent=4))

# # {
# #     "accounts": [
# #         {
# #             "account": 100,
# #             "name": "Jones",
# #             "balance": 24.98
# #         },
# #         {
# #             "account": 200,
# #             "name": "Doe",
# #             "balance": 345.67
# #         }
# #     ]
# # }

# ----------------------------------------------------
# Updating Text Files
# https://docs.python.org/3/library/io.html
# ----------------------------------------------------

# accounts = open('accounts.txt', 'r')
# temp_file = open('temp_file.txt', 'w')

# with accounts, temp_file:
#     for record in accounts:
#         account, name, balance = record.split()
#         if account != '800':
#             temp_file.write(record)
#         else:
#             new_record = ' '.join([account, 'Williams', balance])
#             temp_file.write(new_record+'\n')

# os.remove('accounts.txt')
# os.rename('temp_file.txt', 'accounts.txt')


# ----------------------------------------------------
# Text-File Processing
# https://docs.python.org/3/library/io.html
# ----------------------------------------------------

# # Write file

# # mode='w' deletes all the existence data
# # mode='w' creates file if it does not exists
# with open('accounts.txt', mode = 'w') as accounts:
#     accounts.write('100 Jones 24.98\n')
#     accounts.write('200 Doe 345.67\n')
#     accounts.write('300 White 0.00\n')
#     accounts.write('400 Stone -42.16\n')
#     accounts.write('500 Rich 224.62\n')

# # write to file with print. automaticaly outputs \n
# with open('accounts.txt', mode = 'w') as accounts:
#     print('600 Jones 24.98', file=accounts)
#     print('700 Doe 345.67', file=accounts)
#     print('800 White 0.00', file=accounts)
#     print('900 Stone -42.16', file=accounts)
#     print('1000 Rich 224.62', file=accounts)


# # Read file

# with open('accounts.txt', mode = 'r') as accounts:
#     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
#     for record in accounts:
#         account, name, balance = record.split()
#         print(f'{account:<10}{name:<10}{balance:>10}')
# # Account   Name         Balance
# # 600       Jones          24.98
# # 700       Doe           345.67
# # 800       White           0.00
# # 900       Stone         -42.16
# # 1000      Rich          224.62
