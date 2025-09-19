class Pet: #class Pet to create pet instances with attributes - name, category, breed, age, credit card, vaccination status and weight
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def set_name(self,new_name): #set method to set a new name for a pet instance
        if type(new_name) == str: #checks if the new name is a string
            self._name = new_name
        else:
            print('Please use a string as a name attribute')
    
    def get_name(self): #get method to get the name of the pet (prints it out) when get_name() is called
        return self._name

    def get_weight(self): #get method to get the weight of the pet (prints it out) when get_weight() is called
        return self.weight

    def get_category(self): #get method to get the category of the pet (prints it out) when get_category() is called
        return self.__category
    
    def set_weight(self, new_weight): #set method to set a new weight for a pet instance
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')
        else:
            print('Please enter a number for weight')

    def __str__(self): #str method to print each details of the pet
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name='Bonnie', category='Dog')
p2 = Pet('Clyde','Cat','Persian',12)
p3 = Pet('Cindy', 'Dog',age = 3)
p4 = Pet('Chris' , 'Gorilla' , age = 6)
p5 = Pet('Resun', 'Dog', age = 2)

pets = [p1,p2,p3, p4] # list of objects of the class Pet
for pet in pets: #iterates through the list of pets
    pet.age += 1 #increments the age of each pet instance by 1
    if pet.get_category() == 'Dog': #checks if the pet is a dog and only prints out details of dogs
        print(pet)    
