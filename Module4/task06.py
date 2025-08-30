import random
def approximate_pi(num_points):
    inside_circle = sum(
        1 for _ in range(num_points)
        if random.uniform(-1, 1) ** 2 + random.uniform(-1, 1) ** 2 < 1
    )
    return 4 * inside_circle / num_points
N = int(input("Enter number of random points: "))
print(f"Approximation of pi: {approximate_pi(N)}")
