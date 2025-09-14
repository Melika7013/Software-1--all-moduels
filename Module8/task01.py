import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="airport_db",
    port=3306
)

cursor = conn.cursor()

icao_code = input("Enter ICAO code: ").strip().upper()

query = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao_code,))

result = cursor.fetchone()

if result:
    ident, name, municipality = result
    print(f"ICAO Code: {ident}")
    print(f"Airport Name: {name}")
    print(f"Location: {municipality}")
else:
    print("No airport found with that ICAO code.")

cursor.close()
conn.close()
