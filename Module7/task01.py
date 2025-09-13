seasons = ("Winter", "Spring", "Summer", "Autumn")
month = int(input("Enter the number of a month (1-12): "))
if month < 1 or month > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    if month == 12 or month == 1 or month == 2:
        season = seasons[0]
    elif 3 <= month <= 5:
        season = seasons[1]
    elif 6 <= month <= 8:
        season = seasons[2]
    else:
        season = seasons[3]
    print(f"The season is {season}.")
