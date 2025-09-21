# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%. (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    @staticmethod   # static method to calculate price based on size
    def calculate_price(base_price, size): 
        size = size.lower()
        if size == 'small':
            return base_price
        elif size == 'medium':
            return base_price * 1.10
        elif size == 'large':
            return base_price * 1.20
        elif size == 'xlarge':
            return base_price * 1.30
        else:
            return base_price  # default if size not matched

    # Constructor (Supports parameterized and parameterless)
    def __init__(self, sid=None, sname=None, stype=None, price=0, size='Small'):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.size = size
        self.sprice = Shirt.calculate_price(price, size) # use static method to adjust price

    # Destructor
    def __del__(self):
        print(f"Shirt object with id {self.sid} is being destroyed")

    # ShowBook
    def showBook(self):
        print("----- Shirt Details -----")
        print("Shirt ID  :", self.sid)
        print("Shirt Name:", self.sname)
        print("Type      :", self.stype)
        print("Price     :", round(self.sprice, 2))
        print("Size      :", self.size)
        print("-------------------------")

print("=== Parameterized Constructor ===")
s1 = Shirt('S1', 'Formal Shirt', 'Formal', 1000, 'Small')
s1.showBook()

s2 = Shirt('S2', 'Casual Shirt', 'Casual', 970, 'Large')
s2.showBook()

s3 = Shirt('S3', 'Party Shirt', 'Party', 1500, 'Xlarge')
s3.showBook()

print("\n=== Parameterless Constructor ===")
s4 = Shirt()  # no arguments
s4.showBook()