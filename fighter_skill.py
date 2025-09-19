import random, time 

class Fighter: #defined class to create fighter instances with the attributes name, health, weapon and shield
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health #private attribute using double underscore (unaccessible outside the class)
        self.weapon = weapon
        self.shield = shield
  
    def report(self): #method to print the health of the fighter
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self): #method to check if the fighter is dead even if the health is private as it is accessed through the method which is inside the class
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self): #method to generate a random attack power based on the weapon strength
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
    def skill_attack(self): #method to generate a skill-based attack power based on the weapon strength and user input (timed input)
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        target = random.randint(2, 6) #randomly selects a target between 2 and 6 seconds
        print("Hit the enter key in", target, "seconds to attack!")
        tic = time.time() #start time
        input() #wait for user input
        toc = time.time()
        time_taken = toc - tic #calculate time taken
        multiplier = 3 - abs(target-time_taken) #calculate multiplier based on the time taken
        if multiplier < 2:
            multiplier = 0
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power): #method to calculate the damage taken by the fighter and update the health
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


you = Fighter('You',100,60,20)
troll = Fighter('Troll',300,30,10)

you.report()
troll.report()

while True: #a loop that runs until the health of the troll is less than or equal to 0
    print("YOU ATTACK THE TROLL!")
    troll.defend(you.skill_attack()) #sets the health of the troll to the current health minus the attack power
    troll.report() #prints the health of the troll
    time.sleep(2) #pauses the program for 2 second
    print('----------------------------------')
    if troll.is_dead(): #checks if the health of the troll is less than or equal to 0
        print("YOU WIN!")
        break #breaks the loop if the health of the troll is less than or equal to 0
    print("THE TROLL ATTACKS YOU!")
    you.defend(troll.skill_attack()) #sets your health to the current health minus the attack power
    you.report() #prints health of you
    time.sleep(2)
    print('----------------------------------')
    if you.is_dead(): #checks if your health is less than or equal to 0
        print("YOU LOSE!")
        break #breaks the loop if your health is less than or equal to 0
