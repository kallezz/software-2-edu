class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor


    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            return

        if self.current_floor < floor:
            for i in range(floor - self.current_floor):
                self.floor_up()
                print(f"Current floor: {self.current_floor}")
        elif self.current_floor > floor:
            for i in range(self.current_floor - floor):
                self.floor_down()
                print(f"Current floor: {self.current_floor}")
        else:
            print(f"Current floor: {self.current_floor}")
            return


    def floor_up(self):
        self.current_floor += 1


    def floor_down(self):
        self.current_floor -= 1


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_count = elevator_count

        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for i in range(elevator_count)
        ]


    def run_elevator(self, index, floor):
        print(f"-- Running elevator {index}")
        self.elevators[index].go_to_floor(floor)


    def fire_alarm(self):
        print("-- Fire alarm")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


# Debug
building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)
building.fire_alarm()
