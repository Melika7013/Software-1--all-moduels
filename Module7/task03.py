airports = {}

while True:
    choice = input("Enter 'new' to add airport, 'fetch' to get info, or 'quit' to exit: ").lower()

    if choice == "new":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
    elif choice == "fetch":
        icao = input("Enter ICAO code: ")
        print(airports.get(icao, "Airport not found."))
    elif choice == "quit":
        break
