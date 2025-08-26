# 11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# Person 1
age = int(input("Enter Age of Person-1: "))
ticket1 = float(input("Enter Ticket Amount of Person-1: "))
if age < 12:
    pay1 = ticket1 * 0.70 # Pay= Ticket×(1−30/100)
elif age > 59:
    pay1 = ticket1 * 0.50 # Pay= Ticket×(1−50/100)
else:
    pay1 = ticket1
print(f"You need to pay: {pay1}")

# Person 2
age = int(input("\nEnter Age of Person-2: "))
ticket2 = float(input("Enter Ticket Amount of Person-2: "))
if age < 12:
    pay2 = ticket2 * 0.70 
elif age > 59:
    pay2 = ticket2 * 0.50  
else:
    pay2 = ticket2
print(f"You need to pay: {pay2}")

# Person 3
age = int(input("\nEnter Age of Person-3: "))
ticket3 = float(input("Enter Ticket Amount of Person-3: "))
if age < 12:
    pay3 = ticket3 * 0.70 
elif age > 59:
    pay3 = ticket3 * 0.50  
else:
    pay3 = ticket3
print(f"You need to pay: {pay3}")

# Person 4
age = int(input("\nEnter Age of Person-4: "))
ticket4 = float(input("Enter Ticket Amount of Person-4: "))
if age < 12:
    pay4 = ticket4 * 0.70 
elif age > 59:
    pay4 = ticket4 * 0.50  
else:
    pay4 = ticket4
print(f"You need to pay: {pay4}")

# Person 5
age = int(input("\nEnter Age of Person-5: "))
ticket5 = float(input("Enter Ticket Amount of Person-5: "))
if age < 12:
    pay5 = ticket5 * 0.70 
elif age > 59:
    pay5 = ticket5 * 0.50  
else:
    pay5 = ticket5
print(f"You need to pay: {pay5}")

# Total
total = pay1 + pay2 + pay3 + pay4 + pay5
print("\nTotal Amount to pay=", total)