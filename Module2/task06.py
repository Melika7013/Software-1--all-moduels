import random
print("3-digit code (0-9):", *[random.randint(0,9) for _ in range(3)])
print("4-digit code (1-6):", *[random.randint(1,6) for _ in range(4)])