class Pet: #class Pet is defined to create a pet object with the attributes name, category, age, payment details and vaccination status.
    def __init__(self, name, category, age = 0):
        self.name = name #to store the name of the pet
        self.category = category #to store the category of the pet
        self.age = age #to store the age of the pet
        self.ccard = 'unknown' #preset the credit card to unknown lue is assigned to it yet
        self.vaccinated = False #preset the vaccination status to False 

    #a string method that contains the details of each pet instances of the class Pet, printing the name, category, age, payment details and vaccination status of each pet.
    #the __str__ method is used to return a string representation of the object (instances of the pet) when it is printed.
    def __str__(self):
        payment_details = 'unregistered'
        if len(self.ccard) == 19:  #if loop to check if the credit card has 16 digits and 3 spaces.
            payment_details = 'registered' #will print registered if the credit card has 16 digits and 3 spaces.

        my_status =  'Name: '+self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nPayment_status: ' + payment_details  + '\nVaccinated: '+ str(self.vaccinated)
        return my_status  #mystatus is returned to be printed when the object is printed. The /n is used to print the details of each pet in a new line to make it neat/readable.
    
# objects of the class Pet
p1 = Pet('Bonnie', 'Cat', 3)
p1.ccard = '1111 1111 1111 1111' #credit card number for Bonnie to make his payment details registered
p2 = Pet('Resun', 'Dog', 6)
p2.ccard = '2222 2222 2222 2222' #credit card number for Resun to make his payment details registered
p3 = Pet('Kiegan', 'Hamster', 2)
p3.ccard = '3333 3333 3333 3333' #credit card number for Kiegan to make his payment details registered


pets = [p1, p2, p3]  # list of objects of the class Pet
for pet in pets:
    pet.vaccinated = True #set the vaccinated status to True for each pet in the list of objects of the class Pet to indicate that each pet is vaccinated
    print(pet)  # prints the details of each pet in the list of objects of the class Pet
    print('----------------------------------')  # prints a line to separate the details of each pet in the list of objects of the class Pet