# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc).Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor 
# i. showBook

class Shirt:
    # Constructor
    def __init__(self, id, name, stype, price, size):
        self.sid = id
        self.sname = name
        self.stype = stype
        self.sprice = price
        self.size = size

    # Destructor  
    def __del__(self):
        print(f"Shirt object with id {self.sid} is being destroyed")
    
    # showBook
    def showBook(self):
        print("----- Shirt Details -----")
        print("Shirt ID  :",self.sid)
        print("Shirt Name:",self.sname)
        print("Type      :",self.stype)
        print("Price     :",self.sprice)
        print("Size      :",self.size)
        print("-------------------------")

s1 = Shirt('S1', 'Formal Shirt', 'Formal', 1000, 'Small')
s1.showBook()

s2 = Shirt('S2', 'Casual Shirt', 'Casual', 970, 'Large')
s2.showBook()