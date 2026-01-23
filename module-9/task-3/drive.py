class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def accelerate(self, speed):
        if self.current_speed + speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speed


    def drive(self, time):
        self.travelled_distance += self.current_speed * time


# car = Car("ABC-123", 142)
# print(f"Initial distance: {car.travelled_distance} km")
# car.current_speed = 60
# car.drive(1.5)
# print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")
