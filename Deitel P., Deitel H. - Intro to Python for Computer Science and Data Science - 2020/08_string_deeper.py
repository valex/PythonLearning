from decimal import Decimal

# ----------------------------------------------------
# Splitting and Joining Strings
# ----------------------------------------------------


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