class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator created at floor {self.current_floor}.")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"  ↑ Elevator now at floor {self.current_floor}")
        else:
            print("  Already at top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"  ↓ Elevator now at floor {self.current_floor}")
        else:
            print("  Already at bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("  Invalid floor.")
            return
        print(f"Moving from floor {self.current_floor} to {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"  ✅ Arrived at floor {self.current_floor}\n")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            print(f"\nCreating elevator #{i + 1}:")
            self.elevators.append(Elevator(bottom_floor, top_floor))
        print(f"\n🏢 Building ready with {num_elevators} elevators "
              f"(floors {bottom_floor}–{top_floor}).\n")

    def run_elevator(self, elevator_number, destination_floor):
        if 1 <= elevator_number <= len(self.elevators):
            print(f"=== Elevator #{elevator_number} in action ===")
            self.elevators[elevator_number - 1].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")


# --- Testing the classes ---
if __name__ == "__main__":
    # Create a building with 3 elevators between floors 1–10
    b = Building(1, 10, 3)

    # Move each elevator
    b.run_elevator(1, 6)
    b.run_elevator(2, 3)
    b.run_elevator(3, 10)

    # Bring the first elevator back to the bottom
    b.run_elevator(1, 1)
