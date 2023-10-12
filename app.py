import os
from dataclasses import dataclass
import random

    # create character object that  holds  attributes and types
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
        if Enemy.health >= 100:
            Enemy.health = 100 
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
        else:
            enemy.health -= 30
            mana -= 45
            print(f'{Mage.name} casts Fireball!!')
            print(f'It does 30 damage!')
    def heal():
        Mage.health = 125 if Mage.health >= 125 else Mage.health + 25
        print(f'You healed 25hp! Current hp is {Mage.health}')
    def arise():
        revive_chance = random.randint(100)
        if revive_chance <= 10:
            Mage.health = 125 * 0.5
            Mage.mana = 150 * 0.5
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
    def rage():
        if Barbarian.health <= 90:
            enemy.health -= Barbarian.weapon_damage + 15
        else:
            enemy.health -= Barbarian.weapon_damage + 5
class Archer(Character):
    health = 105
    mana = 100
    weapon = f'Hunting Bow'
    daggers = 30
    weapon_damage = 20
    dodge_chance = .15
    def crit_attack():
        enemy.health -= weapon_damage * 1.6
    def throw_dagger():
        pass
    def triple_shot():
        pass

def intro_text():
    with open('intro.txt', 'w') as file:
        file.write(f'Welcome to the mystical realm of adventure, where heroes are born, and epic quests await. \nIn this world, you\'ll step into a realm filled with magic, monsters, and untold treasures. \nYour journey begins in a land teeming with possibilities, and your destiny is yours to \nshape. Choose your path wisely, for the choices you make will determine the fate of your \ncharacter and the world around you. Will you be a cruel barbarian, a cunning archer, \na wise wizard, or something entirely unique? The challenges and excitement lie ahead as \nyou set forth on a grand quest to vanquish evil, uncover hidden secrets, and become a \nlegendary figure in a realm of endless possibilities. The adventure is yours to embark \nupon, so prepare to explore, battle, and conquer in this captivating realm!\n \nNow what is the name of our brave adventurer?')
    with open('intro.txt', 'r') as file:
        content = file.read()
        print(content)
def get_char_type(): 
    print(f'Please choose a character type:\nBarbarian -- Archer -- Mage')
    char_type = input()
    match char_type:
        case "barbarian":
            char_type = Barbarian()
        case "archer":
            char_type = Archer()
        case "mage":
            char_type = Mage()

character = Character()
mage = Mage()
barbarian = Barbarian()
archer = Archer()
enemy = Enemy()




class Main:
    print(intro_text())
    name = input(' ')
    if name.isdigit():
        print('Haha nice try!')
        name = input('I need a real name: ')
    if name == True:
        print(get_char_type())
        os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Welcome {name} the {char_type}! Now before we partake on this perilous journey, I must know what sort of warrior you are!')
    print(get_char_type())
    print(f'So you are {name} the {char_type} then?')
    
class Fight:
    def enemy_turn():
        enemy_skills = [enemy.attack(), enemy.potion()] # other skills]
        
        atk_chance = random.randint(10)
        if atk_chance <= 6:
            enemy.attack()
            print(random.choice(enemy_skills))