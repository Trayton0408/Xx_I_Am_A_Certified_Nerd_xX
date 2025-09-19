import random, time 

class Fighter: #defined class to create fighter instances with the attributes name, health, weapon and shield
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self): #method to print the health of the fighter
        print(self.name+': '+ 'Health: ' + str(self.health))
    
    def random_attack(self): #method to randomise the attack power of the fighter
        attack_power = random.randint(self.weapon/2, self.weapon*2) 
        print('Attack power: ', (attack_power))
        return attack_power
    
    def defend(self, attack_power): #method to calculate the damage taken by the fighter and update the health
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage 
            print("Damage taken: ", damage)
        else:
            print("No damage taken")

#instances of the class Fighter with name, health, weapon and shield
you = Fighter("You", 100, 60, 20)
troll = Fighter("Troll", 200, 30, 10)

you.report() #prints your health
troll.report() #prints the health of the fighter troll

while True: #a loop that runs until the health of the troll is less than or equal to 0
    print("YOU ATTACK THE TROLL!")
    troll.defend(you.random_attack()) #sets the health of the troll to the current health minus the attack power
    troll.report() #prints the health of the troll
    time.sleep(2) #pauses the program for 2 second
    print('----------------------------------')
    if troll.health <= 0: #checks if the health of the troll is less than or equal to 0
        print("YOU WIN!")
        break #breaks the loop if the health of the troll is less than or equal to 0
    print("THE TROLL ATTACKS YOU!")
    you.defend(troll.random_attack()) #sets your health to the current health minus the attack power
    you.report() #prints health of you
    time.sleep(2)
    print('----------------------------------')
    if you.health <= 0: #checks if your health is less than or equal to 0
        print("YOU LOSE!")
        break #breaks the loop if your health is less than or equal to 0

