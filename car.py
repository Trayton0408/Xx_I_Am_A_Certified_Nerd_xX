class Car: #defined a class named Car to create a car object with the attributes male, model and year.
    def __init__(self, make, model, year): #init method is used to initialise the attributes of the class Car.
        self.make = make #to store the make of the car
        self.model = model #to store the model of the car
        self.year = year #to store the year the car was made
        print(f"Car {self.make} {self.model} {self.year} has spawned.")

    #drive method is used to print if the car is driving or not
    def drive(self):
        print(' ')
        print(f"The {self.year} {self.make} {self.model} is driving.")
        print(' ')
    #stop method is used to print if the car has stopped or not
    def stop(self):
        [print(' ')] 
        print(f"The {self.year} {self.make} {self.model} has stopped.")
        print(' ')
    #honk method is used to print if the car is honking or not
    def honk(self):
        print(' ')
        print(f"The {self.year} {self.make} {self.model} is honking.")
        print(' ')

car1 = Car("Lamborghini", "Huracan", 2023)
car2 = Car("BMW", "M3", 2022)


car1.drive()
car2.stop()