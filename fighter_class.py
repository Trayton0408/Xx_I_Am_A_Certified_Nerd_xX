import random

class Fighter: #defined class to create fighter instances with the attributes name, health, weapon and shield
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health #using double underscore to make the health private
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name+': '+ 'Health: ' + str(self.__health)) #shows the health of the fighter

    def set_health(self, new_health): #set method to set the health of the fighter
        self.__health = new_health
        

    def get_health(self): #get method to get the health of the fighter
        return self.__health
    
    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2) #randomises attack power between half and double the weapon power
        print('Attack power: ', (attack_power)) #prints the attack power
        return attack_power #returns the attack power
    
        
you = Fighter("You", 100, 60, 20)
troll = Fighter("Troll", 200, 30, 10)

you.report()
troll.report()

while True: #loop that runs until the health of the troll is less than or equal to 0
    print("YOU ATTACK THE TROLL!")
    troll.set_health(troll.get_health() - you.random_attack()) #sets the health of the troll to the current health minus the attack power
    troll.report() #prints the health of the troll
    print('----------------------------------')
    if troll.get_health() <= 0: #checks if the health of the troll is less than or equal to 0
        print("YOU WIN!")
        break #breaks the loop if the health of the troll is less than or equal to 0    
    print("THE TROLL ATTACKS YOU!")
    you.set_health(you.get_health() - troll.random_attack()) #sets your health to the current health minus the attack power
    you.report() #prints your health
    if you.get_health() <= 0:
        print("YOU LOSE!")
        break