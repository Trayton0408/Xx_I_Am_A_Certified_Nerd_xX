class Car: #class Car is defined to create a car object with the attributes make, model, year, price and for_sale.
    def __init__(self,make, model, year, price = None, for_sale = False): #init method is used to initialise the attributes of the class Car.
        self.make = make #to store the make of the car
        self.model = model #to store the model of the car
        self.year = year #to store the year the car was made
        self.price = price #to store the price of the car
        self.for_sale = for_sale #to store the for sale status of the car

    def __str__(self): #string method that contains the details of each car instances of the class Car, printing the make, model, year, price and for sale status of each car.
        return f"{self.year} {self.make} {self.model} - ${self.price if self.price else 'N/A'} - {'For Sale' if self.for_sale else 'Not For Sale'}"

c1 = Car('Mazda', '6', 2005, 15000, True) #first instance of the class Car with make Mazda, model 6, year 2005, price 15000 and for sale status True which prints that the car is for sale.
c2 = Car('BMW', 'M3', 2022, 50000, False) #second instance of the class Car with make BMW, model M3, year 2022, price 50000 and for sale status False which prints that the car is not for sale.
c3 = Car('Toyota', 'Corolla', 2020, 12000, True) #third instance of the class Car with make Toyota, model Corolla, year 2020, price 20000 and for sale status True which prints that the car is for sale.
c4 = Car('Honda', 'Civic', 2018, 18000, False) #fourth instance of the class Car with make Honda, model Civic, year 2018, price 18000 and for sale status False which prints that the car is not for sale.

cars = [c1, c2, c3, c4] #stores the instances of the class Car in a list called cars
for car in cars: #for loop to iterate through the list of cars and print the details of each car in the list of objects of the class Car
    print(car)

