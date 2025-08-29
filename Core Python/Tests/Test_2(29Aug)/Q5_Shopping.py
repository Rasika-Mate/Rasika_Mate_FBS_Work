# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST

p1 = int(input("Enter price of Product-1: "))
p2 = int(input("Enter price of Product-2: "))
p3 = int(input("Enter price of Product-3: "))
p4 = int(input("Enter price of Product-4: "))
p5 = int(input("Enter price of Product-5: "))

bill = p1+p2+p3+p4+p5
final_bill = bill+(bill*(18/100))

print("Total Bill is", final_bill)