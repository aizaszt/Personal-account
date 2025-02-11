from datetime import datetime
class Amount:

    def __init__(self,amount, transaction):
        self.amount =float(amount)
        self.time = datetime.now()
        self.transaction = transaction

    def __str__(self):
        return f"{self.time} , {self.transaction}, {self.amount}"
