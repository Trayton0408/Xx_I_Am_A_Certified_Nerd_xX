class Pet: #class Pet is defined to create a pet object with the attributes name, category, age, payment details and vaccination status.
    def __init__(self, name, category, age = 0): #init method is used to initialise the attributes of the class Pet.
        self.name = name #to store the name of the pet
        self.category = category #to store the category of the pet
        self.age = age #to store the age of the pet
        self.ccard = 'unknown' #preset the credit card to unknown value until a number is assigned to the object 
        self.vaccinated = False #preset the vaccination status to False until the the pet is vaccinated

    #a string method that contains the details of each pet instances of the class Pet, printing the name, category, age, payment details and vaccination status of each pet.
    def __str__(self): #the __str__ method is used to return a string representation of the object (instances of the pet) when it is printed.
        payment_details = 'unregistered' #payment details is set to unregistered by default until the credit card number is assigned to the object.
        if len(self.ccard) == 19:  #if loop to check if the credit card has 16 digits and 3 spaces.
            payment_details = 'registered' #will print registered if the credit card has 16 digits and 3 spaces.

        my_status =  'Name: '+self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\nPayment_status: ' + payment_details  + '\nVaccinated: '+ str(self.vaccinated)
        return my_status #mystatus is returned to be printed when the object is printed. The /n is used to print the details of each pet in a new line to make it neat/readable.
    
#objects or instanes of the class Pet
p1 = Pet('Bonnie', 'Cat', 2)
p1.ccard = '1234 5678 9012 3456' #assigning a value to the credit card number for Bonnie to make his payment details registered
p1.vaccinated = True #set the vaccinated status to True for Bonnie to indicate that he is vaccinated

p2 = Pet('Foxy', 'Dog', 4)
p2.ccard = '4321 8765 4321 6543' #assigning a value to the credit card number for Foxy to make his payment details registered
p2.vaccinated = False #set the vaccinated status to False for Foxy to indicate that he is not vaccinated
print(p1)
print(' ')# prints a blank space to separate the details of each pet in the list of objects of the class Pet
print(p2)

