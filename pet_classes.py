class Pet:
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.vaccinated = False
        self.ccard = "Unknown"
        self.billing_address = "Unknown"
        self.owner_name = "Unknown"
        self.account_balance = 0

pet1 = Pet('Bonnie', 'Cat', 3)
pet2 = Pet('Foxy', 'Dog', 4)

print(f"{pet1.name}'s vaccination status is {pet1.vaccinated}.")

    