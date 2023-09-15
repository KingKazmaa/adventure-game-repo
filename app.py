
import os
from dataclasses import dataclass
import random


class Start:
    name = input(f'Welcome traveler! What is the name of our brave adventurer?  ')
    if name.isdigit():
        print('Haha nice try!')
        name = input('I need a real name: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    # FIND AN EASIER WAY TO GIVE PROMPTS THAN JUST SPAMMING PRINT
    # MAYBE INSERT TXT FILES ?
    print(f'Now let us partake on this perilous journey {name}!')

class Character:
    # Class for each playable character type
    species = 'Human'
    health: int
    weapon: str
    weapon_damage: int
    base_damage: 5
    dodge_chance: .05
    xp: 0
    
    def walk():
        print(f'Onward to glory!!!!')
        
    # MAKE SOME KINDA SYSTEM FOR RANDOM OCCURENCES AND PROMPTS
        
    # REDUCES ENEMY HEALTH
    def attack():
        # enemy.health -= 5
        print(f'{name} attacks using bare hands! it isn't very effective')
        
    def gain_xp():
        xp += 50
        print(f'You have gained +50xp')
        print(f'current xp: {xp})
    
    def faint():
        if health <= 0:
            print(f'{name} has fainted...)
            

class Mage(Character):
    health = 125
    mana = 150
    dodge_chance: .10
    weapon = f'Magic Staff'
    weapon_damage = 15
    
    def fireball():
        if mana <= 44:
            print(f'You don't have enough mana to cast this!')
            # return to fight menu
        # enemy.health -= 30
        mana -= 45
        print(f'{name} casts Fireball!!')
        print(f'It does 30 damage!')

    def heal():
        health = 125 if health >= 125 else health += 25
        print(f'You healed 25hp! Current hp is {health}')
    
    
    # GIVES A 10% CHANCE TO SAVE THE PLAYER FROM DYING
    def arise():
        revive_chance = random.randint(100)
        if revive_chance <= 10:
            health = 125 * 0.5
            mana = 150 * 0.5
          # RETURN TO BATTLE SEQUENCE
        
class Barbarian(Character):
    pass

class Archer(Character):
    pass

class Enemy():
    species: 'monster'
    health: 100
    weapon: 'axe'
    weapon_damage: 25 # or int
    
    attack():
        pass
    
    potion():
        Enemy.health = 100 if Enemy.health >= 100
        Enemy.health += 20
        
    faint():
        True if Enemy.health <= 0:
            Print(f'enemy has fainted')
            character.gain_xp()

# class Fight():?


# class Main():