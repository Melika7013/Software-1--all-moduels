talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
p_t = 20
l_p = 32
g_l = 13.3
total_lots = lots + ( pounds * l_p ) + ( talents * p_t * l_p )
total_grams = total_lots * g_l
kilograms = int ( total_grams // 1000)
grams = total_grams % 1000
print("The weight in modern units:\n{} kilograms and {} grams.".format(kilograms, grams))
