def gallons_to_liters(gallons):
    return gallons * 3.78541
while True:
    gallons = float(input("Enter volume in gallons (negative to quit): "))
    if gallons < 0:
        print("Negative value entered. Exiting the program.")
        break
    else:
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters} liters")

