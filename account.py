from amount import Amount
class Account:
    def __init__(self, number, holder):
        self.number = number
        self.holder = holder
        self.__balance = 0.0
        self.transactions =[]

    def deposit(self, amount):
        transaction1= Amount(amount, 'deposit')
        self.transactions.append(transaction1)
        self.__balance += amount
        print('Deposit:  ', amount, 'Balance:  ', self.__balance)
        return

    def withdrawal(self,amount):
           
        transaction1=Amount(amount, 'withdrawal ')
        self.transactions.append(transaction1)
        self.__balance -= amount
        print('Withdrawal:  ', amount, 'Balance:  ', self.__balance)
        if amount > self.__balance:
            print('Insufficient funds ')
        
        
    def transactions_history(self):
        
        if not self.transactions:
            print('No transactions')
            return
            
        print('History of Transactions:')
        
        for transaction1 in self.transactions:
            print(transaction1)


    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.number 
    
    def set_account_number(self, number):
        self.number= number 
        
    def get_holder(self):
        return self.holder 
    
    def __str__(self):
        return f'Account Holder:  {self.holder}, ID:  {self.number} Balance:  {self.__balance}'
        
            
    def __add__(self):
        action=Amount(amount, 'deposit')
        self.transactions.append(action)
        self.__balance += amount
        return 'Deposit: ', amount, 'Balance: ', self.__balance
        
    def __sub__(self):
        if amount > self.__balance:
            return 'Insufficient funds'
        action=Amount(amount, 'withdrawal')
        self.transactions.append(action)
        self.__balance -= amount
        return 'Withdrawal:', amount, 'Balance:', self.__balance
        