class Book:
    def __init__(self, bid, name, price, author):
        self.bid = bid
        self.name = name
        self.price = price
        self.author = author

    def display(self):
        print(f"Book ID: {self.bid}, Name: {self.name}, Price: {self.price}, Author: {self.author}")
