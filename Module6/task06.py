import math
def unit_price(diameter_cm, price_eur):
    return price_eur / (math.pi * (diameter_cm / 200) ** 2)
d1 = float(input("Diameter of pizza 1 (cm): "))
p1 = float(input("Price of pizza 1 (EUR): "))
d2 = float(input("Diameter of pizza 2 (cm): "))
p2 = float(input("Price of pizza 2 (EUR): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

print(f"Pizza 1: {u1:.2f} EUR/m², Pizza 2: {u2:.2f} EUR/m²")

if u1 < u2:
    print("Pizza 1 provides better value for money.")
elif u2 < u1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value for money.")
