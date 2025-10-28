# 2. Create class television that has members to hold the model number ,screen size and price. 
# Take a member function to take input from user, If more than 4 digits are entered for model number, if screen size is smaller than 12 inches or greater than 70 inches or if the price is negative or greater than 5000 Rs, then throw an exception.
# Write a main() that instantiates an object and allows the user to enter and display data. If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model = 0
        self.size = 0
        self.price = 0

    def get_data(self):
        try:
            self.model = int(input("Enter model number: "))
            self.size = int(input("Enter screen size (in inches): "))
            self.price = float(input("Enter price (Rs): "))

            if self.model > 9999:
                raise Exception("Model number should be up to 4 digits only!")
            if self.size < 12 or self.size > 70:
                raise Exception("Screen size must be between 12 and 70 inches!")
            if self.price < 0 or self.price > 5000:
                raise Exception("Price must be between 0 and 5000 Rs!")

        except Exception as e:
            print("Error:", e)
            print("Setting all values to 0.")
            self.model = 0
            self.size = 0
            self.price = 0

    def display(self):
        print("\nModel Number:", self.model)
        print("Screen Size:", self.size, "inches")
        print("Price: Rs.", self.price)

tv = Television()
tv.get_data()
tv.display()