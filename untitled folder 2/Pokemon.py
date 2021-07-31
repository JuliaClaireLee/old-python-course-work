# ------------------------------------------------------------------------------
#        Name: Julia Lee (I did not collaborate with anyone on this assignment.)
#    Filename: Pokemon.py
#        Date: 11/05/2018
# Description: A pokemon game                                   
# ------------------------------------------------------------------------------
from time import sleep
# Challenge 1
from random import randint
class Pokemon:
    #1. way to construct a Pokemon
    counter = 0
    def __init__(self, name):
        self.name = name #attribute
        self.pokemon_type = "NORMAL"
        self.max_hp = randint(0, 450)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.current_hp-1)
        self.defensive_power = randint(1, self.current_hp-1)
        self.fainted = False
        while self.fainted ==True :
            self.counter = counter + 1  # +1 each time the loop runs

    # 2. prints the Pokémon’s stats to the screen:
    def printStats(self):
        print(" ")
        print("Name:",self.name)
        print("Type:", self.pokemon_type)
        print("Current_hp:", self.current_hp) 
        print("Attack:",self.attack_power)
        print("Defensive:",self.defensive_power)
        print("lives left:",2-self.counter)
        print(" ")

    # 3. defend method
    def defend(self):
        self.current_hp =  self.current_hp - (self.defensive_power//2)
        if self.current_hp < 0:
            self.current_hp = 0
            self.fainted = True

    # 4.  Attack method
    def attack(self, opponent):
         opponent.defend()

    #5.  Revive method
    def revive(self):
            self.current_hp = 10
            self.fainted = False

# Challenge 2
def battle (P1, P2):
    P1.attack(P2)
    print(P2.printStats())


class Pikachu(Pokemon):
    def __init__(self, name):
        self.name = name 
        self.pokemon_type = "ELECTRIC"
        self.max_hp = randint(1, 160)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.current_hp-1)
        self.defensive_power = randint(1, self.current_hp-1)
        self.fainted = False
        while self.fainted ==True :
            self.counter = counter + 1
    def Bolt(self, opponent):
         opponent.defend()
         if opponent.current_hp > 10:
             opponent.current_hp =  10 
    def attack(self,opponent):
        if (opponent.pokemon_type == "GROUND"):
            opponent.defend()
            opponent.defend()
            self.Bolt(opponent)
            self.Bolt(opponent)
            opponent.defend()
        elif (opponent.pokemon_type == "ELECTRIC" or opponent.pokemon_type == "FLYING"):
            opponent.current_hp =  opponent.current_hp - 2
        else:
            opponent.defend()
            
     
         
class Squirtle(Pokemon):
    def __init__(self, name):
        self.name = name 
        self.pokemon_type = "WATER"
        self.max_hp = randint(0, 150)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.current_hp-1)
        self.defensive_power = randint(1, self.current_hp-1)
        self.fainted = False
        self.counter = 0
        if self.fainted ==True :
            self.counter = self.counter + 1
    def Bubbles(self, opponent):
        self.attack_power = self.attack_power**2
        opponent.current_hp = 0 
    def attack(self,opponent):
        if (opponent.pokemon_type == "ELECTRIC"):
            opponent.defend()
            opponent.defend()
            opponent.defend()
            opponent.defend()
            opponent.defend()
            self.Bubbles(opponent)
        elif (opponent.pokemon_type == "WATER" or opponent.pokemon_type == "GROUND"):
            opponent.current_hp =  opponent.current_hp -2
        else:
           opponent.defend()
   

         
class Charmander(Pokemon):
    def __init__(self, name):
        self.name = name 
        self.pokemon_type = "FIRE"
        self.max_hp = randint(0, 20)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, abs(self.current_hp-11))
        self.defensive_power = randint(1, abs(self.current_hp-11))
        self.fainted = False
        self.counter = 0
        if self.fainted ==True :
            self.counter = self.counter + 1
    def Fire(self):
        self.attack_power = self.attack_power**2 + 5  #fire makes Charmander stronger
    def attack(self,opponent):
        if opponent.pokemon_type == "GRASS" or opponent.pokemon_type == "ELECTRIC":
            opponent.defend()
            opponent.defend()
            self.Fire()
            opponent.defend() 
        else:
            opponent.defend()  

class Bulbasaur(Pokemon):
    def __init__(self, name):
        self.name = name 
        self.pokemon_type = "GRASS"
        self.max_hp = randint(0, 300)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.current_hp-1)
        self.defensive_power = randint(1, self.current_hp-1)
        self.fainted = False
        while self.fainted ==True :
            self.counter = self.counter + 1
    def attack(self,opponent):
        if opponent.pokemon_type == "GROUND":
            for i in range (randint(1,10)):
                opponent.defend()
                
        else:
           opponent.defend()  

class Geodude(Pokemon):
    def __init__(self, name):
        self.name = name 
        self.pokemon_type = "GROUND"
        self.max_hp = randint(0, 100)
        self.current_hp = self.max_hp
        self.attack_power = randint(1, self.current_hp-1)
        self.defensive_power = randint(1, self.current_hp-1)
        self.fainted = False
        while self.fainted ==True :
            self.counter = counter + 1
    def attack(self,opponent):
        if opponent.pokemon_type == "FIRE":
          for i in range(abs(opponent.current_hp - opponent.defensive_power)):
              opponent.defend()
        elif opponent.pokemon_type == "GROUND":
            opponent.current_hp = opponent.current_hp - 10
        else:
            opponent.defend()        
def main():
    one = input( "Player 1 choose your Pokemon (Geodude, Bulbasaur, Charmander, Squirtle, Pikachu):")
    two = input( "Player 2 choose your Pokemon (Geodude, Bulbasaur, Charmander, Squirtle, Pikachu):")
    if one.upper().strip() == "BULBASAUR":
        P1 = Bulbasaur(one)
    elif one.upper().strip() == "CHARMANDER":
        P1 = Charmander(one)
    elif one.upper() .strip()== "SQUIRTLE":
        P1 = Squirtle(one)
    elif one.upper().strip() == "GEODUDE":
        P1 = Geodude(one)
    elif one.upper().strip() == "PIKACHU":
        P1 = Pikachu(one)
    elif two.upper().strip() not in ["GEODUDE","PIKACHU", "SQUIRTLE", "CHARMANDER", "BULBASAUR"]:
        P1 = Pokemon(one)
    if two.upper().strip() == "BULBASAUR":
        P2 = Bulbasaur(two)
    elif two.upper().strip() == "CHARMANDER":
        P2 = Charmander(two)
    elif two.upper().strip() == "SQUIRTLE":
        P2 = Squirtle(two)
    elif two.upper().strip() == "GEODUDE":
        P2 = Geodude(two)
    elif two.upper().strip() == "PIKACHU":
        P2 = Pikachu(two) 
    elif two.upper().strip() not in ["GEODUDE","PIKACHU", "SQUIRTLE", "CHARMANDER", "BULBASAUR"]:
        P2 = Pokemon(two)
    Ans = input("Are you ready to Battle? (enter NO to end):")
    P1.printStats()
    P2.printStats()
    while Ans.upper() != "NO":
        while P1.current_hp > 0 and P2.current_hp > 0  :
            battle(P2, P1)
            sleep(2)
            if P1.current_hp > 0 and P2.current_hp > 0  :
                battle (P1, P2)
                sleep(2)
        if P2.current_hp <=0 and P1.counter < 3:
            two_dies = two + " "+ "fainted"
            print("+" +'*'*(len(two_dies)+1)+"+")
            print('|', two_dies, "|")
            print("+"+'*'*(len(two_dies)+1)+"+")
            answer = input("Hey, Player 2 do you want to revive ? :")
            if answer.upper().strip() != "NO":
                P2.revive()
                P2.printStats()
                Ans = input("Are you ready to Battle again? (enter NO to end):")
            else:
                wins = "Player 1 wins"
                print("#" +'#'*(len(wins)+1)+"#")
                print('|', wins, "|")
                print("#"+'#'*(len(wins)+1)+"#")
        elif P1.current_hp <=0 and P1.counter < 3:
            one_dies = one + " "+ "fainted"
            print("+" +'*'*(len(one_dies)+1)+"+")
            print('|', one_dies, "|")
            print("+"+'*'*(len(one_dies)+1)+"+")
            answer = input("Hey, Player 1 do you want to revive ? :")
            if answer.upper().strip() != "NO":
                P1.revive()
                P1.printStats()
                Ans = input("Are you ready to Battle again? (enter NO to end):")
        else:
            wins = "Player 2 wins"
            print("#" +'#'*(len(wins)+1)+"#")
            print('|', wins, "|")
            print("#"+'#'*(len(wins)+1)+"#")
            
if __name__ == "__main__":
    main()

# REFRENCES:
# I did not utilize any external resources in completing this assignment.
