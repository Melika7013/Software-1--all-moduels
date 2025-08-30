gender = input("Enter your biological gender (male/female): ").strip().lower()
hb = float(input("Enter your hemoglobin value (g/l): "))
if gender == "female":
    low, high = 117, 155
elif gender == "male":
    low, high = 134, 167
else:
    print("Invalid gender input. Please enter 'male' or 'female'.")
    exit()
if hb < low:
    status = "low"
elif hb > high:
    status = "high"
else:
    status = "normal"
print(f"Hemoglobin is {status}.")
