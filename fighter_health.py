import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self): #method to check if the fighter is dead even if the health is private as it is accessed through the method which is inside the class
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)

you.report()
troll.report()

while True: #a loop that runs until the health of the troll is less than or equal to 0
    print("YOU ATTACK THE TROLL!")
    troll.defend(you.random_attack()) #sets the health of the troll to the current health minus the attack power
    troll.report() #prints the health of the troll
    time.sleep(2) #pauses the program for 2 second
    print('----------------------------------')
    if troll.is_dead(): #checks if the health of the troll is less than or equal to 0
        print("YOU WIN!")
        break #breaks the loop if the health of the troll is less than or equal to 0
    print("THE TROLL ATTACKS YOU!")
    you.defend(troll.random_attack()) #sets your health to the current health minus the attack power
    you.report() #prints health of you
    time.sleep(2)
    print('----------------------------------')
    if you.is_dead(): #checks if your health is less than or equal to 0
        print("YOU LOSE!")
        break #breaks the loop if your health is less than or equal to 0
