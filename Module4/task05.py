# Correct credentials
correct_username = "melika"
correct_password = "1234"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. Attempts left: {max_attempts - attempts}")
if attempts == max_attempts:
    print("Access denied")
