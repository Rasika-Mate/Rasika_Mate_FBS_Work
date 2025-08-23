# 5. WAP to calculate selling price of book based on cost price and discount.
# formula: Selling Price= CP*(1−dicount/100​)

cp = float(input("Enter Cost Price of the book: "))
dis = float(input("Enter Discount(%): "))

sp = cp*(1-dis/100)
print("Selling Price of the book is", sp)
