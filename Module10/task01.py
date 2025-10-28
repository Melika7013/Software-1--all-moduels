class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # starts at the bottom floor
        print(f"Elevator initialized at floor {self.current_floor}.")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}.")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}.")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Invalid floor number.")
            return

        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator has arrived at floor {self.current_floor}.")


# --- Testing the class ---
if __name__ == "__main__":
    # Create an elevator that goes from floor 1 to 10
    h = Elevator(1, 10)

    # Move to a chosen floor (e.g., 5)
    h.go_to_floor(5)

    # Then return to the bottom floor
    h.go_to_floor(1)
