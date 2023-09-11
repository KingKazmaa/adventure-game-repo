
import os
from dataclasses import dataclass


class Start:
    name = input(f'Welcome traveler! What is the name of our brave adventurer?  ')
    if name.isdigit():
        print('Haha nice try!')
        name = input('I need a real name: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    # FIND AN EASIER WAY TO GIVE PROMPTS THAN JUST SPAMMING PRINT
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
        
        pass

    #   
    def heal():
        pass

    def gain_xp():
        pass
    
    def faint():
        pass

class Mage(Character):
    health = 125
    dodge_chance: .10
    weapon = f'Magic Staff'
    weapon_damage = 15
    
    # REDUCES ENEMY HP
    def fireball():
        
        pass
    fire = fireball
    
    # ADDS HP 
    def add_hp():
        health = 125 if health >= 125 else health += 25
        print(f'You healed 25hp! Current hp is {health}')
    heal = add_hp
    
    
    # GIVES A 10% CHANCE TO SAVE THE PLAYER FROM DYING
    def arise():
        
        pass

# class Enemy():


# class Fight():?


# class Main():