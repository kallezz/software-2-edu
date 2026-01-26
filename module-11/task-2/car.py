class Car:
    def __init__(self, license_plate: str, maximum_speed: int):
        self.license_plate: str = license_plate
        self.maximum_speed: int = maximum_speed
        self.current_speed: int = 0
        self.travelled_distance: int = 0


    def accelerate(self, speed: int) -> None:
        if self.current_speed + speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speed


    def drive(self, time: int) -> None:
        self.travelled_distance += self.current_speed * time


class ElectricCar(Car):
    def __init__(self, license_plate: str, maximum_speed: int, battery_capacity: float):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity: float = battery_capacity


class GasolineCar(Car):
    def __init__(self, license_plate: str, maximum_speed: int, tank_volume: float):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume: float = tank_volume


# Debug
car = Car("TEST-123", 150)
print(f"Car created: {car.license_plate}, max speed: {car.maximum_speed}")

electric = ElectricCar("ELEC-123", 200, 75.0)
print(f"Electric car: {electric.license_plate}, max speed: {electric.maximum_speed}, battery: {electric.battery_capacity} kWh")

gasoline = GasolineCar("GAS-123", 180, 50.0)
print(f"Gasoline car: {gasoline.license_plate}, max speed: {gasoline.maximum_speed}, tank: {gasoline.tank_volume} l")

electric.accelerate(100)
gasoline.accelerate(80)
print(f"After acceleration - Electric: {electric.current_speed} km/h, Gasoline: {gasoline.current_speed} km/h")

electric.drive(2)
gasoline.drive(2)
print(f"After 2 hours - Electric: {electric.travelled_distance} km, Gasoline: {gasoline.travelled_distance} km")
