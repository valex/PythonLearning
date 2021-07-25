from decimal import Decimal
import re
import pandas as pd

# ----------------------------------------------------
# Reformatting Data
# ----------------------------------------------------

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
                ['Sue Brown', 'demo2@deitel.com', '5555551234']]

contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone'])

print( contactsdf )
#          Name             Email       Phone
# 0  Mike Green  demo1@deitel.com  5555555555
# 1   Sue Brown  demo2@deitel.com  5555551234

formatted_phone = contactsdf['Phone'].map(get_formatted_phone)
print( formatted_phone )
# 0    555-555-5555
# 1    555-555-1234

contactsdf['Phone'] = formatted_phone
print( contactsdf )
#          Name             Email         Phone
# 0  Mike Green  demo1@deitel.com  555-555-5555
# 1   Sue Brown  demo2@deitel.com  555-555-1234


# ----------------------------------------------------
# Data Validation
# ----------------------------------------------------

# zips = pd.Series({'Boston':'02215', 'Miami':'3310'})
# print(zips)
# # Boston    02215
# # Miami      3310
# # dtype: object

# print( zips.str.match(r'\d{5}') )
# # Boston     True
# # Miami     False
# # dtype: bool


# cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
# print( cities )
# # 0    Boston, MA 02215
# # 1     Miami, FL 33101
# # dtype: object

# print( cities.str.contains(r' [A-Z]{2} ') )
# # 0    True
# # 1    True
# # dtype: bool

# print( cities.str.match(r' [A-Z]{2} ') )
# # 0    False
# # 1    False
# # dtype: bool



# ----------------------------------------------------
# Regular Expressions
# https://docs.python.org/3/library/re.html
# ----------------------------------------------------

# pattern = '02215'

# print( 'Match' if re.fullmatch(pattern, '02215') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch(pattern, '51220') else 'No match' )
# # No match

# print( 'Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid' )
# # Valid

# print( 'Valid' if re.fullmatch(r'\d{5}', '9876') else 'Invalid' )
# # Invalid

# print( 'Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid' )
# # Valid

# print( 'Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid' )
# # Invalid

# print( 'Match' if re.fullmatch('[^a-z]', 'A') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch('[^a-z]', 'a') else 'No match' )
# # No match

# # Metacharacters in a custom character class ([]) are treated as literal characters
# print( 'Match' if re.fullmatch('[*+$]', '*') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch('[*+$]', '!') else 'No match' )
# # No match

# print( 'Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Invalid' )
# # Valid

# print( 'Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Invalid' )
# # Invalid

# print( 'Match' if re.fullmatch('labell?ed', 'labelled') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch('labell?ed', 'labeled') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch('labell?ed', 'labellled') else 'No match' )
# # No match

# print( 'Match' if re.fullmatch(r'\d{3,}', '123') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch(r'\d{3,}', '1234567890') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch(r'\d{3,}', '12') else 'No match' )
# # No match

# print( 'Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch(r'\d{3,6}', '123456') else 'No match' )
# # Match

# print( 'Match' if re.fullmatch(r'\d{3,6}', '1234567') else 'No match' )
# # No match

# print( 'Match' if re.fullmatch(r'\d{3,6}', '12') else 'No match' )
# # No match


# # Replacing Substrings and Splitting Strings


# print( re.sub(r'\t', ', ', '1\t2\t3\t4') )
# # 1, 2, 3, 4

# # with max number of replacement
# print( re.sub(r'\t', ', ', '1\t2\t3\t4', count=2) )
# # 1, 2, 3\t4

# print( re.split(r',\s*', '1,   2,  3,4,     5,6,7,8') )
# # ['1', '2', '3', '4', '5', '6', '7', '8']

# # with max number of splits
# print( re.split(r',\s*', '1,   2,  3,4,     5,6,7,8', maxsplit=3) )
# # ['1', '2', '3', '4,     5,6,7,8']



# # search, match, findall, finditer

# # search looks in a string for the first occurrence of a substring
# # that matches a regular expression and retirn match object
# # return None if nothing found
# result = re.search('Python', 'Python is fun')
# print( result.group() if result else 'not found' )
# # Python

# result2 = re.search('fun!', 'Python is fun')
# print( result2 )
# # None
# print( result2.group() if result2 else 'not found' )
# # not found

# # re.match() checks for a match only at the beginning of the string, 
# # while re.search() checks for a match anywhere in the string
# result_z = re.search('is', 'Python is fun')
# print( result_z.group() if result_z else 'not found' )
# # is

# result_x = re.match('is', 'Python is fun')
# print( result_x.group() if result_x else 'not found' )
# # not found

# result3 = re.search('Sam', 'SAM WHITE', flags=re.IGNORECASE)
# print( result3.group() if result3 else 'not found' )
# # SAM

# result = re.search('^Python', 'Python is fun')
# print( result.group() if result else 'not found' )
# # Python

# result = re.search('^fun', 'Python is fun')
# print( result.group() if result else 'not found' )
# # not found

# result = re.search('Python$', 'Python is fun')
# print( result.group() if result else 'not found' )
# # not found

# result = re.search('fun$', 'Python is fun')
# print( result.group() if result else 'not found' )
# # fun

# # findall finds every matching and returns a list
# contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
# print( re.findall(r'\d{3}-\d{3}-\d{4}', contact) )
# # ['555-555-1234', '555-555-4321']

# # finditer like findall, returns a lazy iterable of match object
# for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
#     print(phone.group())
# # 555-555-1234
# # 555-555-4321

# # use () to capture substrings in a match
# text = 'Charlie Cian, email: demo1@deitel.com'
# pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), email: (\w+@\w+.\w{3})'
# result = re.search(pattern, text)
# print( result.groups() )
# # ('Charlie Cian', 'demo1@deitel.com')

# # entire match as a single string
# print( result.group() )
# # Charlie Cian, email: demo1@deitel.com

# print( result.group(0) )
# # Charlie Cian, email: demo1@deitel.com

# print( result.group(1) )
# # Charlie Cian

# print( result.group(2) )
# # demo1@deitel.com

# ----------------------------------------------------
# Raw Strings
# treat each backslash as a regular character
# ----------------------------------------------------

# file_path = r'C:\topFolder\newFolder\MyFile.txt'
# print( file_path )
# # C:\topFolder\newFolder\MyFile.txt

# ----------------------------------------------------
# Characters and Character-Testing Methods

# https://docs.python.org/3/library/stdtypes.html
# ----------------------------------------------------

# print( '-27'.isdigit() )
# # False

# print( '27'.isdigit() )
# # True

# # Only digits and letters
# print( 'A9876'.isalnum() )
# # True

# print( '123 Main street'.isalnum() )
# # False

# ----------------------------------------------------
# Splitting and Joining Strings
# ----------------------------------------------------

# letters = 'A B C D E'
# print( letters.split() )
# # ['A', 'B', 'C', 'D', 'E']

# letters = 'A, B, C, D'
# print( letters.split(', ') )
# # ['A', 'B', 'C', 'D']

# # with max number of splits
# print( letters.split(', ', 2) )
# # ['A', 'B', 'C, D']

# print( letters.rsplit(', ', 2) )
# # ['A, B', 'C', 'D']

# letters_list = ['A', 'B', 'C', 'D']
# print( ','.join(letters_list) )
# # A,B,C,D

# print( ','.join([str(i) for i in range(10)]) )
# # 0,1,2,3,4,5,6,7,8,9

# print( 'Amanda: 89, 97, 92'.partition(': ') )
# # ('Amanda', ': ', '89, 97, 92')

# url = 'https://example.test/section/document.html'
# rest_of_url, separator, document = url.rpartition('/')
# print( document )
# # document.html
# print( rest_of_url )
# # https://example.test/section


# lines = """This is line 1
# This is line 2
# This is line 3"""
# print( lines.splitlines() )
# # ['This is line 1', 'This is line 2', 'This is line 3']

# # save newline symbol \n
# print( lines.splitlines(True) )
# # ['This is line 1\n', 'This is line 2\n', 'This is line 3']


# ----------------------------------------------------
# Replacing Substrings
# ----------------------------------------------------

# values = '1\t2\t3\t4\t5'

# print( values.replace('\t', '') )
# # 12345

# ----------------------------------------------------
# Searching for Substrings
# ----------------------------------------------------

# sentence = 'to be or not to be that is the question'

# # Counting Occurences
# print( sentence.count('to') )
# # 2

# # with start_index
# print( sentence.count('to', 12) )
# # 1

# # with end_index
# print( sentence.count('to', 12, 25) )
# # 1

# # Locating a Substring
# # if substring not found returns ValueError exception
# print( sentence.index('be') )
# # 3

# # searches from the end of string and returns the last index
# print( sentence.rindex('be') )
# # 16

# # find and rfind returns -1 if substring not found 
# print( sentence.find('be') )
# print( sentence.rfind('be') )


# # Whether a String Contains a Substring

# print( 'that' in sentence )
# # True

# print( 'THAT' in sentence )
# # False

# print( 'THAT' not in sentence )
# # True

# # Locating a Substring

# print( sentence.startswith('to') )
# # True

# print( sentence.startswith('be') )
# # False

# print( sentence.endswith('question') )
# # True

# print( sentence.endswith('quest') )
# # False

# ----------------------------------------------------
# Comparision Operators for Strings
# strings are compared based on their underlying integer value
# ----------------------------------------------------

# print( f'A: {ord("A")}; a: {ord("a")}' )
# # 'A: 65; a: 97'

# print( 'Orange' == 'orange' )
# # False

# print( 'Orange' != 'orange' )
# # True

# print( 'Orange' < 'orange' )
# # True

# print( 'Orange' <= 'orange' )
# # True

# print( 'Orange' > 'orange' )
# # False

# print( 'Orange' >= 'orange' )
# # False


# ----------------------------------------------------
# Changing Character Case
# ----------------------------------------------------

# print( 'ABCDEFGH'.lower() )
# # 'abcdefgh'

# print( 'abcdefgh'.upper() )
# # 'ABCDEFGH'

# print( 'happy birthday'.capitalize() )
# # 'Happy birthday'

# print( 'strings: a deeper look'.title() )
# # 'Strings: A Deeper Look'

# ----------------------------------------------------
# Stripping Whitespace from Strings
# ----------------------------------------------------

# sentence = '\t \n  This is a test string. \t\t \n'
# print( sentence.strip() )
# # This is a test string.

# print( sentence.lstrip() )
# # 'This is a test string. \t\t \n'

# print( sentence.rstrip() )
# # '\t \n  This is a test string.'

# ----------------------------------------------------
# Concatenating and Repeating Strings
# ----------------------------------------------------

# s1 = 'happy'
# s2 = 'birthday'
# s1 += ' ' + s2
# print( s1 )
# # happy birthday

# symbol = '>'
# symbol *= 5
# print( symbol )
# # >>>>>


# ----------------------------------------------------
# Formatting Strings
# ----------------------------------------------------

# print( f'{17.489:.2f}' )
# # '17.49'

# # format integer as string
# print( f'{10:d}' )
# # '10'

# # default s presention type
# print ( f'{"hello":s} {7}' )
# # 'hello 7'

# print( f'{Decimal("10000000000000000.0"):.3f}' )
# # '10000000000000000.000'

# print( f'{Decimal("10000000000000000.0"):.3e}' )
# # '1.000e+16'

# # use the type specifier c to display the characters that correspond to the character codes
# print( f'{58:c}{45:c}{41:c}' )
# # ':-)'

# print( f'[{27:10d}]' )
# # '[        27]'

# print( f'[{3.5:10f}]' )
# # '[  3.500000]'

# print( f'[{"hello":10}]' )
# # '[hello     ]'

# print( f'[{27:<15d}]' )
# # '[27             ]'

# print( f'[{3.5:<15f}]' )
# # '[3.500000       ]'

# print( f'[{"hello":>15}]' )
# # '[          hello]'

# print( f'[{27:^7d}]' )
# # '[  27   ]'

# print( f'[{3.5:^7.1f}]' )
# # '[  3.5  ]'

# print( f'[{"hello":^7}]' )
# # '[ hello ]'

# print( f'[{27:+10d}]' )
# # '[       +27]'

# print( f'[{-27:+10d}]' )
# # '[       -27]'

# print( f'[{27:+010d}]' )
# # '[+000000027]'

# # A space indicates that positive numbers should show a space character in the sign position 
# print( f'{27:d}\n{27: d}\n{-27: d}' )
# # 27
# #  27
# # -27

# print( f'{12345678:,d}' )
# # '12,345,678'

# print( f'{123456.78:,.2f}' )
# # '123,456.78'

# print( '{:.2f}'.format(17.489) )
# # '17.49'

# print( '{} {}'.format('Amanda','Cyan') )
# # 'Amanda Cyan'

# print( '{0} {0} {1}'.format('Happy','Birthday') )
# # 'Happy Happy Birthday'

# print( '{first} {last}'.format(first='Amanda', last='Gray') )
# # 'Amanda Gray'

# print( '{last} {first}'.format(first='Amanda', last='Gray') )
# # 'Gray Amanda'