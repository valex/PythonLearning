from decimal import Decimal
from collections import namedtuple
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from classes10.account import Account
from classes10.timewithproperties import Time
from classes10.private import PrivateClass
from classes10.deck import DeckOfCards
from classes10.commissionemployee import CommissionEmployee
from classes10.salariedcommissionemployee import SalariedCommissionEmployee
from classes10.complexnumber import Complex
from classes10.carddataclass import Card


# ----------------------------------------------------
# Time Series

# Sources
#
# https://www.data.gov/
#
# weather-related time series
# https://www.ncdc.noaa.gov/cag/
#
# climat-related time series
# https://psl.noaa.gov/data/timeseries/
# 
# financial-related time series
# https://www.quandl.com/search
#
# University of California Irvine (UCI)
# https://archive.ics.uci.edu/ml/datasets.php
# 
# economic time series
# http://www.inforum.umd.edu/econdata/econdata.html
#
# ----------------------------------------------------

c = lambda f: 5/9 * (f-32)
temps = [(f, c(f)) for f in range(0,101,10)]

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])

axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')

y_label = axes.set_ylabel('Celsius')

# plt.show()


nyc = pd.read_csv('./classes10/ave_hi_nyc_jan_1895-2018.csv')

print(nyc.head())
#      Date  Value  Anomaly
# 0  189501   34.2     -3.2
# 1  189601   34.7     -2.7
# 2  189701   35.5     -1.9
# 3  189801   39.6      2.2
# 4  189901   36.4     -1.0

print(nyc.tail())
#        Date  Value  Anomaly
# 119  201401   35.5     -1.9
# 120  201501   36.1     -1.3
# 121  201601   40.8      3.4
# 122  201701   42.8      5.4
# 123  201801   38.7      1.3

nyc.columns=['Date', 'Temperature', 'Anomaly']
print(nyc.head(3))
#      Date  Temperature  Anomaly
# 0  189501         34.2     -3.2
# 1  189601         34.7     -2.7
# 2  189701         35.5     -1.9

print(nyc.Date.dtype)
# int64

nyc.Date = nyc.Date.floordiv(100)
print(nyc.head(3))
#    Date  Temperature  Anomaly
# 0  1895         34.2     -3.2
# 1  1896         34.7     -2.7
# 2  1897         35.5     -1.9

pd.set_option('precision', 2)
print(nyc.Temperature.describe())
# count    124.00
# mean      37.60
# std        4.54
# min       26.10
# 25%       34.58
# 50%       37.60
# 75%       40.60
# max       47.60
# Name: Temperature, dtype: float64


linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)

print(linear_regression.slope)
# 0.01477136113296616

print(linear_regression.intercept)
# 8.694993233674293


#predict for 2019
print( linear_regression.slope * 2019 + linear_regression.intercept )
# 38.51837136113297

#predict for 1890
print( linear_regression.slope * 1890 + linear_regression.intercept )
# 36.612865774980335


plt.cla()
plt.clf()

sns.set_style('whitegrid')

axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)

axes.set_ylim(10,70)


plt.show()

# ----------------------------------------------------
# Namespaces and Scopes
# ----------------------------------------------------

# ----------------------------------------------------
# Unit Testing with Docstrings and doctest
# https://docs.python.org/3/library/doctest.html
# ----------------------------------------------------


# ----------------------------------------------------
# Python 3.7 New Data Classes
# https://docs.python.org/3/library/dataclasses.html
#
# https://docs.python.org/3/library/typing.html
#
# ----------------------------------------------------

# c1 = Card(Card.FACES[0], Card.SUITS[3])

# print(c1)
# # Ace of Spades

# print(c1.image_name)
# # Ace_of_Spades.png

# c2 = Card(Card.FACES[0], Card.SUITS[3])
# c3 = Card(Card.FACES[0], Card.SUITS[0])

# print(c1 == c2)
# # True

# print(c1 == c3)
# # False

# print(c1 != c3)
# # True

# ----------------------------------------------------
# Named Tuples
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# ----------------------------------------------------

# Card = namedtuple('Card', ['face', 'suit'])

# card = Card(face='Ace', suit='Spades')

# print( card.face )
# # Ace

# print( card.suit )
# # Spades

# print(card)
# # Card(face='Ace', suit='Spades')

# values = ['Queen', 'Hearts']

# card = Card._make(values)

# print(card)
# # Card(face='Queen', suit='Hearts')

# print(card._asdict())
# # {'face': 'Queen', 'suit': 'Hearts'}


# ----------------------------------------------------
# Operator Overloading
# ----------------------------------------------------

# x = Complex(real=2, imaginary=4)

# print( x )
# # (2 + 4i)

# y = Complex(real=5, imaginary=-1)
# print( y )
# # (5 - 1i)

# print( x+y )
# # (7 + 3i)

# x += y 
# print( x )
# # (7 + 3i)

# ----------------------------------------------------
# Duck Typing and Polymorphism
# ----------------------------------------------------

# class WellPaidDuck:
#     def __repr__(self):
#         return 'I am a well-paid duck'
#     def earnings(self):
#         return Decimal(1_000_000.00)

# c = CommissionEmployee('Sue', 'Jones', '333-33-3333',
#                             Decimal(10000.00), Decimal(0.06))

# s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
#                             Decimal(5000.00), Decimal(0.04), Decimal(300.00))

# d = WellPaidDuck()

# employees = [c, s, d]

# for employee in employees:
#     print(employee)
#     print(f'{employee.earnings():,.2f}\n')
# # CommissionEmployee: Sue Jones
# # social security number: 333-33-3333
# # gross sales: 10000.00
# # commission rate: 0.06
# # 600.00

# # SalariedCommissionEmployee: Bob Lewis
# # social security number: 444-44-4444
# # gross sales: 5000.00
# # commission rate: 0.04
# # base salary: 300.00
# # 500.00

# # I am a well-paid duck
# # 1,000,000.00




# ----------------------------------------------------
# Inheritance
# ----------------------------------------------------

# c = CommissionEmployee('Sue', 'Jones', '333-33-3333',
#                             Decimal(10000.00), Decimal(0.06))

# print( c )
# # CommissionEmployee: Sue Jones
# # social security number: 333-33-3333
# # gross sales: 10000.00
# # commission rate: 0.06


# print(f'{c.earnings():,.2f}')
# # 600.00

# c.gross_sales = Decimal(20000.00)
# c.commission_rate = Decimal(0.1)
# print(f'{c.earnings():,.2f}')
# # 2,000.00

# s = SalariedCommissionEmployee('Bob', 'Lewis', '444-44-4444',
#                             Decimal(5000.00), Decimal(0.04), Decimal(300.00))

# print(s)
# # SalariedCommissionEmployee: Bob Lewis
# # social security number: 444-44-4444
# # gross sales: 5000.00
# # commission rate: 0.04
# # base salary: 300.00

# print(f'{s.earnings():,.2f}')
# # 500.00

# s.gross_sales = Decimal(10000.00)
# s.commission_rate = Decimal(0.05)
# s.base_salary = Decimal(1000.00)

# print(f'{s.earnings():,.2f}')
# # 1,500.00

# print( issubclass(SalariedCommissionEmployee, CommissionEmployee) )
# # True

# print( isinstance(s, CommissionEmployee) )
# # True

# print( isinstance(s, SalariedCommissionEmployee) )
# # True


# employees = [c, s]

# for employee in employees:
#     print(employee)
#     print(f'{employee.earnings():,.2f}\n')
# # CommissionEmployee: Sue Jones
# # social security number: 333-33-3333
# # gross sales: 20000.00
# # commission rate: 0.10
# # 2,000.00

# # SalariedCommissionEmployee: Bob Lewis
# # social security number: 444-44-4444
# # gross sales: 10000.00
# # commission rate: 0.05
# # base salary: 1000.00
# # 1,500.00

# ----------------------------------------------------
# Deck
# ----------------------------------------------------

# deck_of_cards = DeckOfCards()

# print( deck_of_cards )
# # Ace of Hearts      2 of Hearts        3 of Hearts        4 of Hearts        
# # 5 of Hearts        6 of Hearts        7 of Hearts        8 of Hearts        
# # 9 of Hearts        10 of Hearts       Jack of Hearts     Queen of Hearts    
# # King of Hearts     Ace of Diamonds    2 of Diamonds      3 of Diamonds      
# # 4 of Diamonds      5 of Diamonds      6 of Diamonds      7 of Diamonds      
# # 8 of Diamonds      9 of Diamonds      10 of Diamonds     Jack of Diamonds   
# # Queen of Diamonds  King of Diamonds   Ace of Clubs       2 of Clubs         
# # 3 of Clubs         4 of Clubs         5 of Clubs         6 of Clubs         
# # 7 of Clubs         8 of Clubs         9 of Clubs         10 of Clubs        
# # Jack of Clubs      Queen of Clubs     King of Clubs      Ace of Spades      
# # 2 of Spades        3 of Spades        4 of Spades        5 of Spades        
# # 6 of Spades        7 of Spades        8 of Spades        9 of Spades        
# # 10 of Spades       Jack of Spades     Queen of Spades    King of Spades    


# deck_of_cards.shuffle()
# print( deck_of_cards )
# # Ace of Diamonds    8 of Clubs         2 of Diamonds      Queen of Clubs     
# # 9 of Hearts        King of Hearts     6 of Spades        4 of Spades        
# # 6 of Hearts        King of Clubs      9 of Clubs         King of Diamonds   
# # Ace of Clubs       5 of Clubs         3 of Clubs         Jack of Diamonds   
# # 9 of Diamonds      8 of Spades        10 of Hearts       9 of Spades        
# # Jack of Hearts     5 of Diamonds      10 of Diamonds     King of Spades     
# # 10 of Spades       Queen of Hearts    2 of Hearts        6 of Diamonds      
# # 4 of Diamonds      Jack of Clubs      5 of Spades        7 of Hearts        
# # 4 of Clubs         7 of Diamonds      3 of Hearts        7 of Spades        
# # Ace of Hearts      10 of Clubs        8 of Diamonds      5 of Hearts        
# # 3 of Diamonds      4 of Hearts        8 of Hearts        2 of Clubs         
# # 6 of Clubs         Queen of Spades    2 of Spades        Jack of Spades     
# # Queen of Diamonds  7 of Clubs         Ace of Spades      3 of Spades

# deck_of_cards.deal_card()

# card = deck_of_cards.deal_card()

# print( card )
# # 4 of Hearts

# print( card.image_name )

# ----------------------------------------------------
# Custom Class
# ----------------------------------------------------

# account1 = Account('John Green', Decimal('50.00'))

# print(account1.balance)
# # 50.00

# account1.withdraw(Decimal('17.77'))

# print(account1.balance)
# # 32.23

# wake_up = Time(hour=6, minute=30)

# # >>> wake_up
# # Time(hour=6, minute=30, second=0)

# print( wake_up )
# # 6:30:00 AM

# print( wake_up.hour )
# # 6

# wake_up.set_time(hour=7, minute=45)
# print( wake_up.hour )
# # 7

# wake_up.hour = 8
# print( wake_up.hour )
# # 8

# # wake_up.hour = 100
# # ValueError: Hour (100) must be 0-23

# private = PrivateClass()

# print( private.public_data )
# # public

# # print( private.__private_data )
# # AttributeError: 'PrivateClass' object has no attribute '__private_data'

# print( private._PrivateClass__private_data )
# # private