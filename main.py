def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

base1 = get_input("Enter the length of base 1: ")
base2 = get_input("Enter the length of base 2: ")
height = get_input("Enter the height: ")

area = 0.5 * (base1 + base2) * height

print("The area of the trapezoid is:", area)
