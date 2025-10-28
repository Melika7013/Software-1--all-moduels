import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace status: {self.name}")
        print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':<15}{'Distance (km)':<15}")
        print("-" * 52)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<15.1f}")
        print()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False


if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg_number, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hour = 0
    while not race.race_finished():
        race.hour_passes()
        hour += 1
        if hour % 10 == 0:
            print(f"After {hour} hours:")
            race.print_status()

    print(f"Race finished in {hour} hours!")
    race.print_status()
