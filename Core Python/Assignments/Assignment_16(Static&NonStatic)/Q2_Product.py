# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    # Static member
    discount = 0  # in percent

    # Constructor (Supports both parameterized and parameterless)
    def __init__(self, id=None, name=None, price=0, quantity=0):
        self.pid = id
        self.pname = name
        self.price = price
        self.pquantity = quantity

    # Destructor  
    def __del__(self):
        print(f"Product object with id {self.pid} is being destroyed")

    # Static method to set discount for all products
    @staticmethod
    def set_discount(d):
        Product.discount = d

    # Method to get price after discount
    def price_after_discount(self):
        return self.price - (self.price * Product.discount / 100)

    # showBook
    def showBook(self):
        print("----- Product Details -----")
        print("Product ID  :", self.pid)
        print("Product Name:", self.pname)
        print("Price       :", self.price)
        print("Quantity    :", self.pquantity)
        print("Discount(%) :", Product.discount)
        print("Price after Discount:", round(self.price_after_discount(), 2))
        print("---------------------------")

Product.set_discount(10)  # 10% discount applied to all products

print("=== Parameterized Constructor ===")
p1 = Product('P1', 'DELL Laptop', 80000, 2)
p1.showBook()

p2 = Product('P2', 'HP Laptop', 50000, 5)
p2.showBook()