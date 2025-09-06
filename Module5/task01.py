import random
num_dice = int(input("How many dice do you want to roll? "))
dice_results = []
for _ in range(num_dice):
    roll = random.randint(1, 6)
    dice_results.append(roll)

print("Results of each die:", dice_results)
print("Total of dice:", sum(dice_results))


