# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook 

class Book:
    # Constructor
    def __init__(self, id, name, price, author):
        self.bid = id
        self.bname = name
        self.bprice = price
        self.bauthor = author

    # Destructor  
    def __del__(self):
        print(f"Book object with id {self.bid} is being destroyed")
    
    # showBook
    def showBook(self):
        print("----- Book Details -----")
        print("Book ID   :",self.bid)
        print("Book Name :",self.bname)
        print("Price     :",self.bprice)
        print("Author    :",self.bauthor)
        print("------------------------")

b1 = Book('B1', 'Python Programming', 550, 'Guido Van Rosum')
b1.showBook()

b2 = Book('B2', 'Java Programming', 1090, 'Herbert Schildt')
b2.showBook()