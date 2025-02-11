# Created with Pyto ''. ''

from account import Account
from amount import Amount 

if __name__ == '__main__':
    
    first=Account(input('Your nicename: '), int(input('Your ID: ')))
    
    
    first.deposit(float(input("How much did you earn?  ")))

    first.withdrawal(float(input("How much did you spent?  "  )))
    
    
    first.transactions_history()
    print(first)
    