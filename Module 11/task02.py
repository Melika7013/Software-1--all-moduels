# --- Car Hierarchy ---

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0.0

    def accelerate(self, speed):
        """Sets the current speed, ensuring it does not exceed the maximum speed."""
        if speed < 0:
            speed = 0
        elif speed > self.maximum_speed:
            speed = self.maximum_speed
        self.current_speed = speed

    def drive(self, hours):
        """Calculates and adds the distance traveled during the given time."""
        distance = self.current_speed * hours
        self.travelled_distance += distance


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


# --- Main program ---

def main():
    # Create the cars
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Set their speeds
    electric_car.accelerate(150)
    gasoline_car.accelerate(120)

    # Drive both for 3 hours
    electric_car.drive(3)
    gasoline_car.drive(3)

    # Print out the results
    print(f"Electric car {electric_car.registration_number} has driven {electric_car.travelled_distance:.1f} km.")
    print(f"Gasoline car {gasoline_car.registration_number} has driven {gasoline_car.travelled_distance:.1f} km.")


if __name__ == "__main__":
    main()
