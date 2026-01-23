import random


class Car:
    def __init__(self, license_plate: str, maximum_speed: int):
        self.license_plate: str = license_plate
        self.maximum_speed: int = maximum_speed
        self.current_speed: int = 0
        self.travelled_distance: int = 0


    def accelerate(self, speed):
        if self.current_speed + speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speed


    def drive(self, time):
        self.travelled_distance += self.current_speed * time

class Race:
    def __init__(self, name: str, distance: int, cars: list[Car]):
        self.name: str = name
        self.distance: int = distance
        self.cars: list[Car] = cars


    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)


    def print_status(self):
        for car in self.cars:
            print(f"License plate: {car.license_plate} | maximum speed: {car.maximum_speed} km/h | current speed: {car.current_speed} km/h | travelled distance: {car.travelled_distance} km")
            print("-------------------------------------------------------------------------------------------------------")


    def race_finished(self) -> bool:
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True

        return False


# Debug
cars = []
for i in range(10):
    car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

print(f"\nRace finished initially: {race.race_finished()}")

for hour in range(5):
    race.hour_passes()
    if hour == 2:
        print(f"After {hour + 1} hours, race finished: {race.race_finished()}")

race.print_status()
