import random


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


cars = [
    Car("ABC-001", 200),
    Car("ABC-002", 200),
    Car("ABC-003", 200),
    Car("ABC-004", 200),
    Car("ABC-005", 200)
]

def race(car_list):
    for car in car_list:
        car.accelerate(60)

    while True:
        for car in car_list:
            car.drive(1)

            # Debug
            # print(f"Car {car.license_plate} distance {car.travelled_distance} km, current speed {car.current_speed} km/h")

            if car.travelled_distance >= 10000:
                return car_list

            car.accelerate(random.randint(-10, 15))



race(cars)
