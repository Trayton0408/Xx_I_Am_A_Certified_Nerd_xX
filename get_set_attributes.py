class Pet: #defined class Pet to create pet objects with attributes - name, category, breed, age, credit card, vaccination status and weight
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0 #sets the weight of the pet to 0 initially

    #set method to set a new name for the pet
    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print("Name must be a string")
    
    #get method to get the name of the pet (prints it out) when get_name() is called
    def get_name(self):
        return self._name
    
    #get method to get the weight of the pet (prints it out) when get_weight() is called
    def get_weight(self):
        return self.weight
    
    #set method to set a new weight for the pet
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float: #checks if the weight is a number either an integer or a float
            if new_weight > 0: #checks if the weight is a positive number
                self.weight = new_weight
            else:
                print("Weight must be a positive number")
        else: print("Weight must be a number")
    
    def __str__(self): #string method to print each details of the pet
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'
        
        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated) + '\nWeight: ' + str(self.weight)
        return my_status
    
#object or instance of the class Pet with name Bonnie, category Cat and age 10
p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10,)
p1.set_weight(5) #sets the weight of the pet instance p1 to 5
print(p1)