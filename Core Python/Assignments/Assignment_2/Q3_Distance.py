# 3. Convert distant given in feet and inches into meter and centimeter.
# 1 feet = 0.3048 meter
# 1 inch = 0.0254 meter
# 1 meter = 100 cm

feet = float(input("Enter Feet: "))
inches = float(input("Enter Inches: "))

# convert feet and inches both into meters 
m = feet * 0.3048 + inches * 0.0254
cm = m * 100

print(f"Total distance in Metres: {m}")
print(f"Total distance in Centimetres: {cm}")
