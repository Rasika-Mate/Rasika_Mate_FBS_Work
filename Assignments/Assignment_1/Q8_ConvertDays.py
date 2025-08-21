# WAP to convert days into years, weeks and days

day = int(input('Enter Days: '))

year = day // 365 # Calculate Year
day = day % 365
week = day // 7 # Calculate Weeks
day = day % 7 # Calculate Day

print(f"Conversion of Days into 'Years: {year}, Weeks: {week}, Days:{day}'")