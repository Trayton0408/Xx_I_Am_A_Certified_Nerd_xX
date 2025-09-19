pet1 = { 
'name' : 'Bonnie',
'animal category' : 'Cat',
'age' : 3,
'vaccinated' : True,
'credit card' : '3423 2326 7543 1234',
'billing address' : '17 Park Drive, The Shire 3695',
'owner name' : 'Annie Jenkins',
'account balance' : 129.95, 
}

pet1.update({'name' : 'Miss Bonnie'}) #change the name of pet1 to Miss Bonnie
pet1.update({'age' : pet1['age'] + 1}) #increment the age of pet1 by 1

pet2 = {
'name' : 'Dino',
'animal category' : 'Dog',
'age' : 6,
'vaccinated' : True,
'credit card' : '1234 5678 9012 3456',
'billing address' : '123 Avenue, ABC City 2090',
'owner name' : 'Resun',
'account balance' : 200.00,
}

print(pet1['name'] + "'s vaccination status is " + str(pet1['vaccinated']) + ".") #prints the vaccination status of pet1 Miss Bonnie
print(pet2['name'] + "'s vaccination status is " + str(pet2['vaccinated']) + ".") #prints the vaccination status of pet2 Dino