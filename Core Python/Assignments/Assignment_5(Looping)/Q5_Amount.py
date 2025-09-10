# 5. WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount. (Use looping to optimize the problem)

amount = int(input("Enter Amount: "))

print("Minimum number of notes for", amount, ":")

while amount > 0:
    if amount >= 2000:
        note = 2000
    elif amount >= 500:
        note = 500
    elif amount >= 200:
        note = 200
    elif amount >= 100:
        note = 100
    elif amount >= 50:
        note = 50
    elif amount >= 20:
        note = 20
    elif amount >= 10:
        note = 10
    elif amount >= 5:
        note = 5
    elif amount >= 2:
        note = 2
    else:
        note = 1

    count = amount // note
    print(note, "=", count)
    amount = amount % note