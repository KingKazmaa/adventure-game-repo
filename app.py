
import os
from dataclasses import dataclass
import random


class Character:
    name: str
    health: int
    weapon: str
    mana: int
    weapon_damage: int
    base_damage: 5
    dodge_chance: int
    xp: 0
    
    def walk():
        print(f'Onward to glory!!!!')
        
    # MAKE SOME KINDA SYSTEM FOR RANDOM OCCURENCES AND PROMPTS
        
    # REDUCES ENEMY HEALTH
    def attack():
        # enemy.health -= 5
        print(f'{Character.name} attacks using bare hands! it isn\'t very effective')
        
    def gain_xp():
        xp += 50
        print(f'You have gained +50xp')
        print(f'current xp: {xp}')
    
    def faint():
        if Character.health <= 0:
            print(f'{Character.name} has fainted...')

class Enemy:
    health = 100
    weapon = f'dagger'
    weapon_damage = 20
    xp_gain = int
    
    def attack():
        print(f'The enemy attacks! It does 20 damage')
        Character.health -= 25
        print(f'{Character.health}')
    
    def potion():
        Enemy.health = 100 if Enemy.health >= 100
        Enemy.health += 20
        
    def faint():
        if Enemy.health <= 0:
            print(f'enemy has fainted...')

class Mage(Character):
    health = 125
    mana = 150
    dodge_chance = .10
    weapon = f'Magic Staff'
    weapon_damage = 15
    
    def fireball():
        if Mage.mana <= 44:
            print(f'You don\'t have enough mana to cast this!')
            # return to fight menu
        else:
            enemy.health -= 30
            mana -= 45
            print(f'{Mage.name} casts Fireball!!')
            print(f'It does 30 damage!')

    def heal():
        Mage.health = 125 if Mage.health >= 125 else Mage.health + 25
        print(f'You healed 25hp! Current hp is {Mage.health}')
    
    
    # GIVES A 10% CHANCE TO SAVE THE PLAYER FROM DYING
    def arise():
        revive_chance = random.randint(100)
        if revive_chance <= 10:
            Mage.health = 125 * 0.5
            Mage.mana = 150 * 0.5
            # RETURN TO BATTLE SEQUENCE

class Barbarian(Character):
    health = 180
    mana = 75
    weapon = f'Double Axe'
    weapon_damage = 35
    
    def double_strike():
        double_chance = random.randint(10)
        if double_chance <= 7:
            enemy.health -= Barbarian.weapon_damage * 2
        else:
            enemy.health -= Barbarian.weapon_damage

    # if health is lower than threshold, deal bonus damage
    def rage():
        if Barbarian.health <= 100:
            enemy.health -= (Barbarian.weapon_damage + 15)
        else:
            enemy.health -= Barbarian.weapon_damage
            

class Archer(Character):
    health = 105
    mana = 100
    weapon = f'Hunting Bow'
    weapon_damage = 20
    dodge_chance = .15



character = Character()
mage = Mage()
barbarian = Barbarian()
enemy = Enemy()

class Start:

    def get_name():
        name = input(f'Welcome traveler! What is the name of our brave adventurer?  ')
        if name.isdigit():
            print('Haha nice try!')
            name = input('I need a real name: ')
        return name
    
    def get_char_type(): 
        print(f'Now choose a character type:')
        print(f'Barbarian -- Archer -- Mage')
        char_type = input()
        match char_type:
            case "barbarian":
                char_type = Barbarian()
                print(f' You are {Start.name} the {char_type}')
                
            case "archer":
                char_type = Archer()
                print(f' You are {Start.name} the {char_type}')
                
            case "mage":
                char_type = Mage()
                print(f' You are {Start.name} the {char_type}')
        return char_type

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'Now let us partake on this perilous journey {name}!')
    
    # CREATE THIS FILE AND SEE HOW IT LOADS ONCE READ USING THE READ METHOD BELOW
with open('intro.txt', 'r') as file:
        content = file.read()
        print(content)
        

# class Fight:


# class Main: