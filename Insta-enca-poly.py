class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

class ElectricCar(Car):
    def __init__(self, make, model, year, colour, battery_size=75):
        super().__init__(make, model, year, colour)
        self.battery_size = battery_size
    
    def charge(self):
        print(f"{self.make} {self.model} is charging.")


electric1 = ElectricCar("Tesla", "Model S", 2023, "Red")

print(f"Electric Car: {electric1.make} {electric1.model}, Year: {electric1.year}, Colour: {electric1.colour}, Battery Size: {electric1.battery_size} kWh")

electric1.start()
electric1.stop()
electric1.charge()