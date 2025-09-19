class Pet: #defined class Pet to create pet objects with the attributes name, category, age, payment details and vaccination status
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name #using single underscore to make the name protected
        self.__category = category #using double underscore to make the category private
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False 

    def have_birthday(self): #this method increments the age of the pet by 1
        self.age += 1

    def __str__(self): #string method to print each details of the pet
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

#object or instance of the class Pet with name Bonnie, category Cat and age 10
p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10, breed = 'Siamese') #Category here is private and cannot be accessed outside the class but it still prints as the string method which is inside the class is called
p1.__category = 'Dog' #this will not work because __category is private. It will still print the category as Cat as tested
print(p1.__category) #this will not work because __category is private. It will raise an error as it is outside the class
print(p1) #prints the details of the pet instance p1