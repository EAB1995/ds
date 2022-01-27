import random
from time import *
from random import randint

Players = ["Abbot" , "Miller"]



class Character_Class :    
    def __init__(
        self , 
        name , 
        inventory , 
        cybernetics = {} , 
        HP = 0 , 
        character_die_lst = [], 
        action = [], 
        weapon_choice = None, 
        flank = [False, False],
        drone = False
        ) :
        self.name = name
        self.inventory = {1 : "EMPTY" , 2 : "EMPTY" , 3 : "EMPTY" , 4 : "EMPTY"}
        self.cybernetics = cybernetics
        self.HP = HP
        self.character_die_lst = character_die_lst
        self.action = []
        self.weapon_choice = weapon_choice
        self.flank = flank
        self.drone = drone
    def add_inventory(self , add) :
        for slot , item in self.inventory.items() :
            if item == "EMPTY" :
                self.inventory[slot] = add
                print(f"\n{add.name.upper()} ADDED TO {self.name.upper()}'S INVENTORY")
                break
    def remove_inventory(self , remove) :
        for slot, item in self.inventory.items() :
            if item == "EMPTY":
                pass
            elif item.name == remove.name :
                self.inventory[slot] = "EMPTY"
    def show_inventory(self) :
        print(f"\n{self.name.upper()}'s INVENTORY:")
        for slot , item in self.inventory.items() :
            capacity = 4
            if item == "EMPTY" :
                print(f"\nSlot {slot} : //{item}//")
            elif item.type == "weapon" :
                print(f"\nSlot {slot} : //{item.name.upper()}// WEIGHT: {item.inv_slots} // AMMO COUNTER: {item.ammo}")
            elif item.type == "item" :
                print(f"\nSlot {slot} : //{item.name.upper()}// WEIGHT: {item.inv_slots} // {item.desc}")
        for item in self.inventory.values() :
            if item == "EMPTY" :
                capacity += 0
            else :
                capacity -= item.inv_slots
        print("\nREMANING WEIGHT CAPACITY: {capacity}".format(capacity = capacity))
    def remaining_inventory(self):
        count = 0
        for i in self.inventory.values():
            if i == "EMPTY":
                pass
            else:
                count += i.inv_slots
        remaining = 4 - count
        return remaining
    def character_die(self) :
        roll = randint(0 , 6)
        if roll == 1 :
            return self.character_die_lst[0]
        elif roll == 2 :
            return self.character_die_lst[1]
        elif roll == 3 :
            return self.character_die_lst[2]
        elif roll == 4 :
            return self.character_die_lst[3]
        elif roll == 5 :
            return self.character_die_lst[4]
        else :
            return self.character_die_lst[5]

abbot = Character_Class(
    "Lt. Abbot" , 
    {} , 
    cybernetics = {"Auto Cortex" : "Once per chapter, when not in combat, you may re-roll the crew die and apply the second result"} , 
    HP = 12 ,
    character_die_lst = ["W", "WWS", "W", "MMS", "M", "C"]
    )

miller = Character_Class(
    "Lt. Miller" , 
    {} , 
    cybernetics = {"Auto Cortex" : "Once per chapter, when not in combat, you may re-roll the crew die and apply the second result"} , 
    HP = 12 ,
    character_die_lst = ["C", "CCS", "C", "MMS", "W", "M"]
    )

class Opponent_Class :
    def __init__(self , name , HP, DMG_R, DMG_M, DMG_Pro, roll_lst, loot) :
        self.name = name
        self.HP = HP
        self.DMG_R = DMG_R
        self.DMG_M = DMG_M
        self.DMG_Pro = DMG_Pro
        roll_lst = []
        self.loot = loot
        for Player in Players :
            roll_lst.append(randint(1 , 3))
        for roll in roll_lst :
            if roll == 1 :
                self.HP.append("C")
            elif roll == 2 :
                self.HP.append("W")
            elif roll == 3 :
                self.HP.append("M")
    def Stats(self) :
        print("{Opponent}// HP: {HP} Ranged Damage: {DMG_R} Melee Damage: {DMG_M} Defence Class: {Def}".format(Opponent = str(self.name) , HP = self.HP , DMG_R = self.DMG_R , DMG_M = self.DMG_M , Def = self.DMG_Pro))
engineer = Opponent_Class("Engineer" , HP = ["M" , "M" , "C" , "C"] , DMG_R = 1 , DMG_M = 2 , DMG_Pro = {"ballistic" : 1 , "energy" : 1 , "explosive" : 3}, roll_lst = [], loot = 2)
tentacles = Opponent_Class("Tentacles", ["M", "M", "C", "W"], DMG_R=0, DMG_M=1, DMG_Pro={"ballistic" : 0 , "energy" : 0 , "explosive" : 0}, roll_lst = [], loot = 3)
cyborg = Opponent_Class("Cyborg", HP = ["M", "M", "W"], DMG_R=1, DMG_M=1, DMG_Pro={"ballistic" : 1 , "energy" : 2 , "explosive" : 3}, roll_lst = [], loot = 2)
lizardmen = Opponent_Class("Lizardmen", HP = ["M", "M", "W"], DMG_R = 2, DMG_M=2, DMG_Pro={"ballistic" : 0.5 , "energy" : 1 , "explosive" : 2}, roll_lst=[], loot=2)
alien = Opponent_Class("Alien", ["M", "M", "M", "C"], None, 2, None, None, 2)
mutant = Opponent_Class("Mutant", ["M", "M", "M", "C"], DMG_R=1, DMG_M=2, DMG_Pro={"ballistic" : 1 , "energy" : 1 , "explosive" : 3}, roll_lst=[], loot=1)
character_roster = {"abbot" : abbot , "miller" : miller}

class Ranged_Weapon:
    def __init__(
        self , 
        name , 
        dmg_type , 
        ammo , 
        max_ammo , 
        extra_damage , 
        special_roll , 
        rate_of_fire_1 , 
        rate_of_fire_2 , 
        max_dmg , 
        inv_slots
    ) :
        self.Ranged_Weapon = self
        self.type = "weapon"
        self.name = name
        self.dmg_type = dmg_type
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.extra_damage = extra_damage
        self.special_roll = special_roll
        self.rate_of_fire_1 = rate_of_fire_1
        self.rate_of_fire_2 = rate_of_fire_2
        self.max_dmg = max_dmg
        self.inv_slots = inv_slots

class Unmarked_Pills:
    def __init__(
        self,
        name,
    ) :
        self.name = "Unmarked Pills"
        self.type = "item"
        self.inv_slots = 1
        self.desc = "HEAL 1 HP"
    def use(self, user):
        user.HP += 1
        print(f"{user.name.upper()} GAINS 1 HP BY SWALLOWING A CAPSULE OF {self.name.upper()}")
        user.remove_inventory(unmarked_pills)    

class Alien_Sludge:
    def __init__(
        self,
        name,
    ) :
        self.name = "Alien Sludge"
        self.type = "item"
        self.inv_slots = 1
        self.desc = "HEAL 1 HP"
    def use(self, user):
        user.HP += 1
        print(f"{user.name.upper()} GAINS 1 HP BY SWALLOWING A PACKET OF {self.name.upper()}")
        user.remove_inventory(unmarked_pills)  

class Trigger_Item:
    def __init__(
        self,
        name,
        type,
        inv_slots,
        desc, 
        trigger
    ) :
        self.name = name
        self.type = type
        self.inv_slots = inv_slots
        self.desc = desc
        self.trigger = trigger


#////////////// RANGED WEAPON INSTANTIATION ////////////////
slug_pistol = Ranged_Weapon("Slug Pistol" , "ballistic" , 1 , 1 , 2 , "jam" , 1 , None , 2 , 1)
slug_pistol_1 = Ranged_Weapon("Slug Pistol" , "ballistic" , 1 , 1 , 2 , "jam" , 1 , None , 2 , 1)
battle_rifle = Ranged_Weapon("Battle Rifle" , "ballistic" , 2 , 2 , 2 , "jam" , 1 , 2 , 4 , 2)
battle_rifle_1 = Ranged_Weapon("Battle Rifle" , "ballistic" , 2 , 2 , 2 , "jam" , 1 , 2 , 4 , 2)
beam_emitter = Ranged_Weapon("Beam Emitter" , "energy" , 3 , 3 , None , "overheat" , 3 , None , 3 , 2)
ray_gun = Ranged_Weapon("Ray Gun", "energy", 1, 1, None, "overheat", 1, None, 1, 1)
rocket_launcher = Ranged_Weapon("Rocket Launcher", "explosive", 1, 1, None, "fault", 1, None, 1, 2)

#///////////// MELEE WEAPON INSTATIATION ////////////////
rusty_pipe = Trigger_Item("Rusty Pipe", "melee", 1, "Re-Roll", "trigger")

#///////////// ITEM INSTANTIATION //////////////////
unmarked_pills = Unmarked_Pills("Unmarked Pills")
alien_sludge = Alien_Sludge("Alien Sludge")
force_field = Trigger_Item("Force Field", "item", 1, "Negate Damage", "trigger")

item_roster = [
    slug_pistol,
    slug_pistol_1,
    battle_rifle,
    battle_rifle_1,
    beam_emitter,
    ray_gun,
    rocket_launcher,
    unmarked_pills,
    alien_sludge,
    force_field
]

def loot_gen(number):
    loot_items = []
    while number > 0:
        for item in range(0, number):
            rng = randint(0, len(item_roster) - 1)
            loot_items.append(item_roster[rng])
            number -= 1
    return loot_items

def loot_target(Lead_1, Follow_1, target, number):
    sleep(2)

    items = loot_gen(number)
    sleep(1)
    print("""
                                 _____ _   _  ________  ____   __ ______ ___________ _____  ___ _____ ___________ 
                                |  ___| \ | ||  ___|  \/  \ \ / / |  _  \  ___|  ___|  ___|/ _ \_   _|  ___|  _  \ 
                                | |__ |  \| || |__ | .  . |\ V /  | | | | |__ | |_  | |__ / /_\ \| | | |__ | | | |
                                |  __|| . ` ||  __|| |\/| | \ /   | | | |  __||  _| |  __||  _  || | |  __|| | | |
                                | |___| |\  || |___| |  | | | |   | |/ /| |___| |   | |___| | | || | | |___| |/ / 
                                \____/\_| \_/\____/\_|  |_/ \_/   |___/ \____/\_|   \____/\_| |_/\_/ \____/|___/  
                                                                                  
                                                                                  
    """)
    sleep(1)
    print(f"\nYOU SCAVANGE WHAT YOU CAN BEFORE MOVING ON...\n--[SALVAGE")
    for item in items:
        print(f"\n-{item.name.upper()}")
    while len(items) > 0:
        for item in items:
            print(f"ASSIGN A MEMBER OF THE CREW TO RECIEVE {item.name.upper()}")
            print(f"--[{Lead_1.name.upper()} // INVENTORY SLOTS AVAILABLE: {Lead_1.remaining_inventory()} [1]\n--[{Follow_1.name.upper()} // INVENTORY SLOTS AVAILABLE: {Follow_1.remaining_inventory()} [2]\n--[DISCARD [3]")
            a1 = input("--[")
            if a1 == "1" :
                abbot.add_inventory(item)
                items.remove(item)
                item_roster.remove(item)
                print(items)
            elif a1 == "2" :
                miller.add_inventory(item)
                items.remove(item)
                item_roster.remove(item)