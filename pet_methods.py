class Pet: #defined class Pet to create pet objects with the attributes name, category, age, payment details and vaccination status.
    def __init__(self, name, category, age = 0, account_balance = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = account_balance
    
    def have_birthday(self):
        self.age += 1 #this method increments the age of the pet by 1
    
    def have_vaccination(self):
        self.vaccinated = True #this method sets the vaccinated status of the pet to True

    def clear_account(self):
        self.account_balance = 0

    def age_in_human_years(self): #method to convert the age of the pet to human years
        if self.category == 'Dog':
           self.age = self.age * 7 
        elif self.category == 'Cat':
            self.age = self.age * 6
        else:
            return self.age #if pet not dog or cat, return the age of the pet

    def __str__(self): #string method to print each details of the pet
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered' #makes the payment status registered if the credit card has 16 digits and 3 spaces.

        #my_status is a string that contains the details of each pet instances of the class Pet, printing the name, category, age, payment details and vaccination status of each pet.
        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nPayment_status: ' + payment_status  + '\nVaccinated: '+ str(self.vaccinated) + '\nAccount_balance: ' + str(self.account_balance)
        return my_status


p1 = Pet('Bonnie', 'Cat', 3, 100,) #creates an instance of the Pet class with name Bonnie, category Cat and age 3
p1.ccard = '1234 5678 9012 3456' 
p1.have_birthday()
p1.have_vaccination()
p1.clear_account()
p1.age_in_human_years()
p2 = Pet('Foxy', 'Dog', 4, 200) #creates an instance of the Pet class with name Foxy, category Dog and age 4
p2.ccard = '4321 8765 4321 6543'
p2.have_birthday()
p2.have_vaccination()
p2.clear_account()
p2.age_in_human_years()

pets = [p1, p2]  # list of objects of the class Pet
for pet in pets:
    print(pet)  # prints the details of each pet in the list of objects of the class Pet
    print('----------------------------------')  # prints a line to separate the details of each pet in the list of objects of the class Pet