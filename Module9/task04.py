import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def main():
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(reg_num, max_speed)
        cars.append(car)

    race_over = False
    hour = 0

    while not race_over:
        hour += 1
        for car in cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

            if car.travelled_distance >= 10000:
                race_over = True

    print(f"\nRace finished after {hour} hours!\n")
    print(f"{'Registration':<10} {'Max Speed':<10} {'Current Speed':<15} {'Distance (km)':<15}")
    print("-" * 55)
    for car in cars:
        print(f"{car.registration_number:<12} {car.max_speed:<10} {car.current_speed:<15} {car.travelled_distance:<15.1f}")


if __name__ == "__main__":
    main()
