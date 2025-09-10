# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n = int(input("Enter number of passengers: "))
ticket = float(input("Enter per ticket cost: "))
total_amount = 0

for i in range(1, n+1):
    age = int(input(f"Enter age of Passenger {i}: "))

    if age < 12:       # children
        fare = ticket * 0.7   
    elif age > 59:     # senior citizens
        fare = ticket * 0.5   
    else:              # others
        fare = ticket

    print(f" Ticket for Passenger {i} = {fare}")
    total_amount += fare

print("\nTotal Ticket Amount for all passengers =", total_amount)