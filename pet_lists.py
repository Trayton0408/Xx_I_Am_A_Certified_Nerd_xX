#parallel lists storing name, species, age and vaccinations status of pets
pet_name = ['Bonnie', 'Dino', 'Kiegan', 'Foxy', 'Resun']
species = ['Cat', 'Dog', 'Hamster', 'Dog', 'Dog']
age = [3, 6, 2, 4, 5]
vaccination_status = [True, True, False, True, False]

#adding a new pet and its detailts to the lists using append method
pet_name.append('Hootie')
species.append('Blowfish')
age.append(34)
vaccination_status.append(False)

#removing a pet and its details from the lists using remove method


#vaccinate every unvaccinated pet
for i in range(len(vaccination_status)): #iterates through the vaccination_status list
    if not vaccination_status[i]: #check if the pet is not vaccinated
        vaccination_status[i] = True #set the vaccination status to True for each pet in the list of objects of the class Pet to indicate that each pet is vaccinated)

#remove a pet
for i in range(len(pet_name)):
    if pet_name == 'Bonnie':
        pet_name.remove

for i in range(len(pet_name)): #prints the details of each pet in the parallel lists in order of their index
    print(f'pet name: {pet_name[i]}')
    print(f'species: {species[i]}')
    print(f'age: {age[i]}')
    print(f'vaccination status: {vaccination_status[i]}')
    print('----------------------------------') #prints a line to separate pets and their details
