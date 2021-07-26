from decimal import Decimal
from classes10.account import Account
from classes10.timewithproperties import Time
from classes10.private import PrivateClass
from classes10.deck import DeckOfCards
from classes10.commissionemployee import CommissionEmployee
from classes10.salariedcommissionemployee import SalariedCommissionEmployee
from classes10.complexnumber import Complex

# ----------------------------------------------------
# Named Tuples
# ----------------------------------------------------




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