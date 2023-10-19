import os
from dataclasses import dataclass
import random

class Character:
    name: str
    weapon: str
    health: int
    mana: int
    cost: int
    dodge_chance: int
    weapon_damage: int
    base_damage: 5
    xp: 0
    
    def check_mana():
        if Character.mana < Character.cost:
            print(f'Not enough mana! \nYou have {mana}mp.')
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
        cost = 45
        Mage.check_mana()
        # if Mage.mana <= 44:
            # print(f'You don\'t have enough mana to cast this!')
        # else:
        # enemy.health -= 30
        mana -= 45
        print(f'{Mage.name} casts Fireball!! \nIt does 30 damage!')
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
        enemy.health -= Archer.weapon_damage * 1.6
    def throw_dagger():
        pass
    def triple_shot():
        pass

# inventory + checker

player_inventory = {
'potion': 2,
'mana potion': 2
}

def check_inventory(player_inventory):
    for key, value in player_inventory.items():
        if value >= 1:
            # use item
            player_inventory[f'{key}'] -=1
        else:
            print(f'no more {key} left')

print(check_inventory(player_inventory))
# health + mana checker

def check_health():
    if Character.health <= 0:
        print(game_over())

        # make a 'cost' dataclass for Character and change the value with each available move. should look like this:


# maybe a function that takes you back to the fight menu/txt

# max health
def fireball():
        cost = 45
        Mage.check_mana()
        # if Mage.mana <= 44:
            # print(f'You don\'t have enough mana to cast this!')
        # else:
        # enemy.health -= 30
        mana -= 45
        print(f'{Mage.name} casts Fireball!! \nIt does 30 damage!')

print(fireball())