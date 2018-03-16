#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character():
    def __init__(self, name, health, power, alive):
        self.name = name
        self.health = health
        self.power = power
        self.alive = alive
    
    def is_alive(self):
        self.alive = True
        if self.health < 1:
            self.alive = False
        else:
            return True
            
    def print_status(self):
        print("{} status: {} health and {} power.".format(self.name, self.health, self.power))
        
    
    
class Hero(Character): 
        
    def attack(self, enemy):
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
        
        
        
class Goblin(Character):
    
    def attack(self, enemy):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
    
        
        
hero = Hero('hero',10,5,True)
goblin = Goblin('goblin',6,2,True)


def main():
    Hero.health = 10
    Hero.power = 5
    Goblin.health = 6
    Goblin.power = 2

    while goblin.is_alive() and hero.is_alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()

