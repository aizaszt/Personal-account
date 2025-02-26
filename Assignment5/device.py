class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name=name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period}'

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period}'

    def apply_discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)

    def is_available(self, amount):
        if self.stock >=amount:
            return True
        return False

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
        else: 
            print('NOT FOUND')