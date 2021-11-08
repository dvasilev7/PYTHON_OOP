class Vehicle:
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        litres = distance * self.fuel_consumption
        if litres <= self.fuel_quantity:
            self.fuel_quantity -= litres

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption += 0.9
        litres = distance * self.fuel_consumption
        if litres <= self.fuel_quantity:
            self.fuel_quantity -= litres

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption += 1.6
        litres = distance * self.fuel_consumption
        if litres <= self.fuel_quantity:
            self.fuel_quantity -= litres

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)

