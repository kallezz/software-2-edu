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


# Debug
# h = Elevator(1, 10)
# print("Basic elevator test:")
# h.go_to_floor(5)
# h.go_to_floor(1)
