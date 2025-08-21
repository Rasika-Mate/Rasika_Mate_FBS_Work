# 3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter Feet: "))
inches = float(input("Enter Inches: "))

metre = feet*0.3048
centimetre = inches*2.54

print("Feet into Metres: ",metre)
print("Inches into Centimetre: ",centimetre)