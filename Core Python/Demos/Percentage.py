m1 = int(input('Enter marks for subject 1: '))
m2 = int(input('Enter marks for subject 2: '))
m3 = int(input('Enter marks for subject 3: '))
m4 = int(input('Enter marks for subject 4: '))
m5 = int(input('Enter marks for subject 5: '))

total_marks = m1 + m2 + m3 + m4 + m5

perc = (total_marks / 500) * 100

print(f'Percentage is {perc}%.')