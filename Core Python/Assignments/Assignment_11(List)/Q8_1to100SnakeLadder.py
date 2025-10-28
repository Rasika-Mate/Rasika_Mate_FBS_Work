# 8. Print 1 to 100 in snakes and ladder pattern.

num = 100  # starting number
for i in range(10):  # 10 rows
    row = []
    for j in range(10):
        row.append(num)
        num -= 1
    # Reverse every alternate row to create snake pattern
    if i % 2 == 1:
        row.reverse()
    print(row)