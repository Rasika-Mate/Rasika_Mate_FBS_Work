# 2. Create a class Product with members as pid,pname,price and quantity. Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook 

class Product:
    # Constructor
    def __init__(self, id, name, price, quantity):
        self.pid = id
        self.pname = name
        self.price = price
        self.pquantity = quantity

    # Destructor  
    def __del__(self):
        print(f"Product object with id {self.pid} is being destroyed")
    
    # showBook
    def showBook(self):
        print("----- Product Details -----")
        print("Product ID  :",self.pid)
        print("Product Name:",self.pname)
        print("Price       :",self.price)
        print("Quantity    :",self.pquantity)
        print("---------------------------")

p1 = Product('P1', 'DELL Laptop', 80000, 2)
p1.showBook()

p2 = Product('P2', 'HP Laptop', 50000, 5)
p2.showBook()