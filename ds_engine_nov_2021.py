from random import *
from ds_classes_nov_2021 import *
from sys import stdout

def prt_txt(text):
    for i in text:
        if i is "/":
            print(f'{i}', end='', flush=True)
        else:
            print(f'{i}', end='', flush=True)
            sleep(0.05)

def take_in(accept):
    choice = str(input("\n\n--[").upper())
    if choice in accept:
        return choice
    else:
        prt_txt(f"INPUT NOT RECOGNISED.\nACCEPTED INPUTS: {accept.upper()}")
        take_in(accept)


def end_seq(ending):
    #Add check to automatically reload weapons 30/11
    if ending == "generic":
        prt_txt("END SEQ PLACEHOLDER")
    elif ending == "seq_3":
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Without looking back, the crew make for the nearest exit, 
leaving the tentacled monstrosity thrashing in the darkness
behind them...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
    elif ending == "seq_5":
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
The Cyborg collapses in a heap of severed cables and 
battered amour plates, choking on a black, tar-like fluid...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
    elif ending == "seq_6":
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Pick your way across the hangar in the wake of the firefight, 
you look around to try and find the captive that was being interrogated. 
Alas, it seems that they used the confusion of the melee to escape...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
    elif ending == "seq_8":
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
The mutant collapses in a heap, it's regenerative powers unable to heal
the damage done by the sustained attacks from the crew. 

After a bruising fight, they take a moment to collect themselves before 
moving on...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)




def Choose_Player_Ranged(Lead_1 , Follow_1 , target , acted, modifier, ending) :
    #TEST\\\\\\\\\\\\
    #print("\nTRIGGERED ------ Choose_Player_Ranged")
    #////////////////
    if len(acted) == 0 :
        prt_txt(f"\n\nCHOOSE CREW MEMBER TO TAKE THEIR TURN:\nA: {Lead_1.name.upper()}\nB: {Follow_1.name.upper()}\n")
        acting = take_in("A / B")
        #TEST\\\\\\\\\\\\\\\
        print("\t\t\t\tTEST acting -", acting)
        #TEST///////////////
        if acting == "A" :
            acting = Lead_1
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        elif acting == "B" :
            acting = Follow_1
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
    elif len(acted) == 1 :
        if acted[0].name == Lead_1.name :
            acting = Follow_1
            prt_txt(f"\n{acting.name.upper()}'S TURN\n")
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        elif acted[0].name == Follow_1.name :
            acting = Lead_1
            prt_txt(f"\n{acting.name.upper()}'S TURN\n")
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        #TEST\\\\\\\\\\\\\\\
        print("\t\t\t\tTEST acting -", acting.name)
        #TEST///////////////
    else :
        Play_Turn(Lead_1 , Follow_1 , target, False, modifier, ending)

def Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending) :
    #TEST\\\\\\\\\\\\\\\
    print("\t\t\t\tTEST acting -", acting.name)
    #TEST///////////////
    prt_txt(f"\n///{acting.name.upper()}///\nCHOOSE AN ACTION:\nA: SHOOT\nF: FLANK\nX: CHARGE\nC: TAKE COVER\nR: RELOAD \nD: DEPLOY DRONE [BUGGY] \nI: USE ITEM [UNFINISHED]\nT: TRADE\n{acting.show_inventory()}\n")
    a1 = take_in("A / F / X / C / R / D / I / T")
    if a1 == "A" :
        acting.show_inventory()
        slot_choice = input("CHOICE [ENTER 1 / 2 / 3 / 4]: ")
        slot_choice = int(slot_choice)
        acting.weapon_choice = acting.inventory.get(slot_choice)
        shots = acting.weapon_choice.rate_of_fire_1
        #TEST\\\\\\\\\\\\\
        print("\t\t\t\tacting.weapon_choice - ", acting.weapon_choice.name, acting.weapon_choice.ammo)
        #TEST//////////////
        if acting.weapon_choice.ammo < 1 :
            prt_txt("\nCLICK CLICK CLICK... YOU'RE OUT OF AMMO! CHOOSE ANOTHER WEAPON, OR RELOAD\n")
            Choose_Action_Ranged(Lead_1 , Follow_1 , target, acted , acting, modifier, ending)
        if type(acting.weapon_choice.rate_of_fire_2) == int :
            a1 = input("CHOOSE RATE OF FIRE:\nA: {rof_1}\nB: {rof_2}\n--[".format(rof_1 = acting.weapon_choice.rate_of_fire_1 , rof_2 = acting.weapon_choice.rate_of_fire_2)).upper()
            if a1 == "A" :
                shots = acting.weapon_choice.rate_of_fire_1
            elif a1 == "B" :
                shots = acting.weapon_choice.rate_of_fire_2
        if acting.weapon_choice.dmg_type == "ballistic" :
            for shot in range(0 , shots) :
                character_roll = randint(1 , 6)
                acting.weapon_choice.ammo = acting.weapon_choice.ammo - 1
                if character_roll in range(1 , 4) :
                    #dmg = target.DMG_Pro.get(acting.weapon_choice.dmg_type)
                    acting.action.append("hit")
                elif character_roll == 4 :
                    acting.action.append("jam")
                elif character_roll == 5 :
                    #acting.weapon_choice.ammo = acting.weapon_choice.ammo - 1
                    # ^^^ redundant / taking additional shots off ammo counter
                    dmg = target.DMG_Pro.get(acting.weapon_choice.dmg_type) * 2
                    acting.action.append("crit")
                elif character_roll == 6 :
                    acting.action.append("miss")
        elif acting.weapon_choice.dmg_type == "energy":
            for shot in range(0, shots) :
                character_roll = randint(1 , 6)
                acting.weapon_choice.ammo = acting.weapon_choice.ammo - shots
                if character_roll in range(1 , 5) :
                    #dmg = target.DMG_Pro.get(acting.weapon_choice.dmg_type)
                    acting.action.append("hit")
                elif character_roll == 5 :
                    acting.action.append("overheat")
                elif character_roll == 6 :
                    acting.action.append("miss")  
        elif acting.weapon_choice.dmg_type == "explosive":
             for shot in range(0, shots) :
                character_roll = randint(1 , 6)
                acting.weapon_choice.ammo = acting.weapon_choice.ammo - shots
                if character_roll in range(1 , 4) :
                    #dmg = target.DMG_Pro.get(acting.weapon_choice.dmg_type)
                    # ^^^ redundant?
                    acting.action.append("hit")
                elif character_roll == 4 :
                    acting.action.append("fault")
                elif character_roll == 5:
                    acting.action.append("missfire")
                elif character_roll == 6 :
                    acting.action.append("miss")
    elif a1 == "F" :
        #First check to see if flank action has already been performed 
        if acting.flank[1] is True:
            prt_txt("THE FLANK ACTION HAS ALREADY BEEN USED THIS ROUND!")
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        else:    
            prt_txt(f"{acting.name.upper()} DASHES AROUND THE {target.name.upper()} AND LINES UP A SHOT")
            acting.action.append("flank")
            Lead_1.flank[1], Follow_1.flank[1] = True, True 
    elif a1 == "X" :
        charge_check = input("CHARGING THE ENEMY WILL IMMEDIATELY BEGIN CLOSE COMBAT - ARE YOU SURE YOU WANT TO CHARGE?\n\nY/N\n--[").upper()
        if charge_check == "N":
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        else:
            prt_txt(f"YOU CHARGE AT THE {target.name.upper()}!")
            Choose_Player_Melee(Lead_1 , Follow_1 , target , acted, modifier, ending)
    elif a1 == "R" :
        weapon_lst = {}
        count = 0
        for i in acting.inventory :
            count += 1
            if isinstance(acting.inventory.get(i) , Ranged_Weapon) is True :
                weapon_lst[count] = acting.inventory.get(i)
        for x in weapon_lst.keys() :
            prt_txt(f"{x} : {weapon_lst.get(x).name} /// AMMO COUNT: {weapon_lst.get(x).ammo} /// MAX AMMO: {weapon_lst.get(x).max_ammo} ///")
        prt_txt("\nRELOAD - CHOOSE WEAPON")
        a2 = take_in("1 / 2 / 3 / 4")
        reload_choice = weapon_lst.get(int(a2))
        reload_choice.ammo += reload_choice.max_ammo
        prt_txt(f"\n...RELOADING {reload_choice.name.upper()}...\n///{reload_choice.name.upper()} AMMO COUNT: {reload_choice.ammo}\n")
        acting.action.append("reload")
    elif a1 == "C" :
        prt_txt(f"{acting.name} TAKES COVER, WAITING FOR THEIR MOMENT TO STRIKE...")
        acting.action.append("cover")
    elif a1 == "D" :
        if Lead_1.drone or Follow_1.drone is True:
            prt_txt("THE DRONE HAS ALREADY BEEN USED IN THIS ROUND...")
            Choose_Action_Ranged(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        else:
            Lead_1.drone, Follow_1.drone = True, True
            prt_txt(f"{acting.name.upper()} POWERS UP THEIR MEDICAL DRONE, HEALING 1HP OF DAMAGE.")
            acting.HP += 1
            acting.action.append("drone")
    elif a1 == "T" :
        if acting == Lead_1 :
            Trade_In_Combat(acting, Follow_1)
            acting.action.append("trade")
        elif acting == Follow_1 :
            Trade_In_Combat(acting, Follow_1)
            acting.action.append("trade")
    acted.append(acting)           
    Choose_Player_Ranged(Lead_1 , Follow_1 , target , acted, modifier, ending)

def Choose_Player_Melee(Lead_1 , Follow_1 , target , acted, modifier, ending) :
    if len(acted) == 0 :
        prt_txt(f"\nCHOOSE CREW MEMBER TO TAKE THEIR TURN:\nA: {Lead_1.name.upper()}\nB: {Follow_1.name.upper()}")
        acting = take_in("A / B")
        if acting == "A" :
            acting = Lead_1
            Choose_Action_Melee(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        elif acting == "B" :
            acting = Follow_1
            Choose_Action_Melee(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
    elif len(acted) == 1 :
        if acted[0].name == Lead_1.name :
            acting = Follow_1
            prt_txt(f"\n{acting.name.upper()}'S TURN\n")
            Choose_Action_Melee(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
        elif acted[0].name == Follow_1.name :
            acting = Lead_1
            prt_txt(f"\n{acting.name.upper()}'S TURN\n")
            Choose_Action_Melee(Lead_1 , Follow_1 , target , acted , acting, modifier, ending)
    else :
        Play_Turn(Lead_1 , Follow_1 , target, True, modifier, ending)

def Choose_Action_Melee(Lead_1 , Follow_1 , target , acted , acting, modifier, ending) :
    prt_txt(f"\n///{acting.name.upper()}///\nCHOOSE AN ACTION:\nA: FIGHT\n")
    a1 = take_in("A")
    if a1 == "A" :
        acting.action = acting.character_die()
    acted.append(acting)
    Choose_Player_Melee(Lead_1 , Follow_1 , target , acted, modifier, ending)


def Play_Turn(Lead_1 , Follow_1 , target, melee, modifier, ending) :
    #TEST\\\\\\\\\\\\\
    #print("BEGINNING Play_Turn")
    #print("TEST melee, modifier >>> ", melee, modifier)
    #print("TEST Lead_1, Follow_1.actions >>> ", Lead_1.action, Follow_1.action)
    #/////////////////
    action_lst = []
    for action in Lead_1.action, Follow_1.action:
        action_lst.append(action)
    
    #Opening check for forced melee 
    force_melee = True
    shoot_actions = ["hit", "miss", "crit", "jam"]
    for actions in action_lst:
        for action in actions:
            if action in shoot_actions:
                force_melee = False
    #Force melee check
    if force_melee and melee == False:
        #print("FORCE MELEE")
        Choose_Player_Melee(Lead_1, Follow_1, target, [], modifier, ending)


    if len(target.HP) > 0 and melee == False :
        #////////// LEAD RANGED ACTIONS //////////////
        if "jam" in Lead_1.action :
            prt_txt(f"\n{Lead_1.name.upper()}'S WEAPON JAMS!\n")
            #Prevents additional shots going through if weapon jams
            Lead_1.action = ["jam"]
        elif "overheat" in Lead_1.action:
            prt_txt(f"{Lead_1.name.upper()}'S WEAPON OVERHEATS, CAUSING SERIOUS BURNS! {Lead_1.name.upper()} LOSES 1 HP!\n")
            Lead_1.HP -= 1
            Lead_1.action = ["overheat"]
        elif "missfire" in Lead_1.action:
            prt_txt(f"{Lead_1.name.upper()}'S WEAPON MISSFIRES, EXPLODING IN {Lead_1.name.upper()} HANDS! {Lead_1.name.upper()} LOSES 1 HP\n")
            Lead_1.HP -= 1
            Lead_1.action = ["missfire"]
        elif "fault" in Lead_1.action:
            prt_txt(f"{Lead_1.name.upper()}'S WEAPON MALFUNCTIONS! {Lead_1.name.upper()} DISCARDS THEIR WEAPON...\n")
            #NB - must be ammended to remove the weapon carried over from previous function 
            Lead_1.remove_inventory(rocket_launcher)
            Lead_1.action = ["fault"]
        elif "flank" in Lead_1.action :
            prt_txt(f"\n{Lead_1.name.upper()} LINES UP A SHOT FROM BEHIND COVER.")
            prt_txt(f"\n{target.name.upper()} TAKES A SHOT!")
            #Flanking shots only ever do 1 damage to character
            target_roll = randint(1 , 6)
            if target_roll in range(1 , 4) :
                Lead_1.HP -= 1
                prt_txt(f"\n{target.name.upper()} HITS, AND DOES 1 DAMAGE!\n")
            else:
                prt_txt(f"\n{target.name.upper()} MISSES!\n")
        hit_count = 0
        crit_count = 0
        miss_count = 0
        for i in Lead_1.action :
            if i == "hit":
                hit_count += 1
            elif i == "crit":
                crit_count += 1
            elif i == "miss":
                miss_count += 1
        if hit_count > 0 or crit_count > 0:
            dmg = target.DMG_Pro.get(Lead_1.weapon_choice.dmg_type)
            if hit_count != 0:
                dmg = dmg * hit_count
                prt_txt(f"{Lead_1.name.upper()} SCORES {hit_count} HIT!")
            if crit_count != 0:
                dmg = dmg * (crit_count * 2)
                prt_txt(f"{Lead_1.name.upper()} SCORES {crit_count} CRITICAL HIT!")
            if miss_count != 0:
                for i in range(0, miss_count):
                    prt_txt(f"{Lead_1.name.upper()} MISSES A SHOT!")
            if dmg < 1:
                prt_txt(f"{Lead_1.name.upper()} FAILS TO DO ENOUGH DAMAGE AGAINST THE {target.name.upper()}!")
            prt_txt(f"ALLOCATE {dmg} DAMAGE TO {target.name.upper()}:\n{target.name.upper()} HEALTH PROFILE: {target.HP}\n")
            target_HP = list(input("--[").upper())
            dmg_lst = list(range(1 , (dmg + 1)))
            for x in dmg_lst :
                for z in target.HP :
                    if z in target_HP :
                        if len(target.HP) == 0 :
                            prt_txt(f"{target.name} IS DEAD!")
                            #TEST\\\\\\\\\
                            #print("TRIGGER END 1")
                            #//////////////
                            loot_target(Lead_1, Follow_1, target, target.loot)
                            return end_seq(ending)
                        target.HP.remove(z)
                        target_HP.remove(target_HP[0])
                        #MODIFIER Regen check
                        if modifier == "regen":
                            roll = randint(1, 6)
                            if roll in [1, 2]:
                                prt_txt(f"{target.name.upper()} ABSORBS THE DAMAGE FROM {Lead_1.name.upper()}'S SHOT, AND REGENERATES ONE HIT POINT!")    
                                target_HP.append("M")
                        break
            prt_txt(f"\n{target.name} HP: {target.HP}\n")

        #Return fire check - both Lead_1 and Follow_1 use same return_fire bool var
        return_fire = False
        for i in Lead_1.action :
            if i in ["hit", "crit", "miss", "jam"] :
                return_fire = True
        if return_fire == True:
            prt_txt(f"\n{target.name.upper()} RETURNS FIRE!\n")
            target_roll = randint(1 , 6)
            if target_roll in range(1 , 4) :
                Lead_1.HP -= target.DMG_R
                prt_txt(f"\n{target.name.upper()} HITS, AND DOES {target.DMG_R} DAMAGE!\n")
                #Force Field check
                for item in Lead_1.inventory.values():
                    #TEST\\\\\\\\\\\\\\\
                    #print("TRIGGER FORCE FIELD\nitem.name>>> ", item.name)
                    #///////////////////
                    if item == "EMPTY":
                        pass
                    elif item.name == "Force Field":
                        prt_txt(f"{Lead_1.name.upper()} HAS A FORCEFIELD IN THEIR INVENTORY WHICH CAN BE USED TO NEGATE INCOMING DAMAGE. WOULD YOU LIKE TO USE IT NOW?\n\n[Y/N]\n")
                        use_force_field = take_in("Y / N")
                        if use_force_field == "Y":
                            Lead_1.HP += target.DMG_R
                        elif use_force_field == "N":
                            pass
            else:
                prt_txt(f"\n{target.name.upper()} MISSES!\n")
            return_fire = False
        
        #///////// FOLLOW RANGED ACTIONS /////////////
        if "jam" in Follow_1.action :
            prt_txt(f"\n{Follow_1.name.upper()}'S WEAPON JAMS!\n")
            #Prevents additional shots going through if weapon jams
            Follow_1.action = ["jam"]
        elif "overheat" in Follow_1.action:
            prt_txt(f"{Follow_1.name.upper()}'S WEAPON OVERHEATS, CAUSING SERIOUS BURNS! {Follow_1.name.upper()} LOSES 1 HP!\n")
            Follow_1.HP -= 1
            Follow_1.action = ["overheat"]
        elif "missfire" in Lead_1.action:
            prt_txt(f"{Lead_1.name.upper()}'S WEAPON MISSFIRES, EXPLODING IN {Lead_1.name.upper()} HANDS! {Lead_1.name.upper()} LOSES 1 HP\n")
            Lead_1.HP -= 1
            Lead_1.action = ["missfire"]
        elif "fault" in Lead_1.action:
            prt_txt(f"{Lead_1.name.upper()}'S WEAPON MALFUNCTIONS! {Lead_1.name.upper()} DISCARDS THEIR WEAPON...\n")
            #MB - must be ammended to remove the weapon carried over from previous function 
            Lead_1.remove_inventory(rocket_launcher)
            Lead_1.action = ["fault"]
        elif "flank" in Follow_1.action :
            prt_txt(f"\n{Follow_1.name} LINES UP A SHOT FROM BEHIND COVER.")
            prt_txt(f"\n{target.name.upper()} TAKES A SHOT!")
            #Flanking shots only ever do 1 damage to character
            target_roll = randint(1 , 6)
            if target_roll in range(1 , 4) :
                Follow_1.HP -= 1
                prt_txt(f"\n{target.name.upper()} HITS, AND DOES 1 DAMAGE!\n")
            else:
                prt_txt(f"\n{target.name.upper()} MISSES!\n")
        hit_count = 0
        crit_count = 0
        miss_count = 0
        for i in Follow_1.action :
            if i == "hit":
                hit_count += 1
            elif i == "crit":
                crit_count += 1
            elif i == "miss":
                miss_count += 1
        if hit_count > 0 or crit_count > 0:
            dmg = target.DMG_Pro.get(Follow_1.weapon_choice.dmg_type)
            if hit_count != 0:
                dmg = dmg * hit_count
                prt_txt(f"{Follow_1.name.upper()} SCORES {hit_count} HIT!")
            if crit_count != 0:
                dmg = dmg * (crit_count * 2)
                prt_txt(f"{Follow_1.name.upper()} SCORES {crit_count} CRITICAL HIT!")
            if miss_count != 0:
                for i in range(0, miss_count):
                    prt_txt(f"{Follow_1.name.upper()} MISSES A SHOT!")
            prt_txt(f"ALLOCATE {dmg} DAMAGE TO {target.name.upper()}:\n{target.name.upper()} HEALTH PROFILE: {target.HP}\n")
            target_HP = list(input("--[").upper())
            dmg_lst = list(range(1 , (dmg + 1)))
            for x in dmg_lst :
                for z in target.HP :
                    if z in target_HP :
                        if len(target.HP) == 0 :
                            prt_txt(f"{target.name} IS DEAD!")
                            #TEST\\\\\\\\\
                            #print("TRIGGER END 1")
                            #//////////////
                            loot_target(Lead_1, Follow_1, target, target.loot)
                            return end_seq(ending)
                        target.HP.remove(z)
                        target_HP.remove(target_HP[0])
                        #MODIFIER Regen check
                        if modifier == "regen":
                            roll = randint(1, 6)
                            if roll in [1, 2]:
                                prt_txt(f"{target.name.upper()} ABSORBS THE DAMAGE FROM {Lead_1.name.upper()}'S SHOT, AND REGENERATES ONE HIT POINT!")    
                                target_HP.append("M")
                        break
            prt_txt(f"\n{target.name} HP: {target.HP}\n")
        
        for i in Follow_1.action :
            if i in ["hit", "crit", "miss", "jam"] :
                return_fire = True
        if return_fire == True:
            prt_txt(f"\n{target.name.upper()} RETURNS FIRE!\n")
            target_roll = randint(1 , 6)
            if target_roll in range(1 , 4) :
                Follow_1.HP -= target.DMG_R
                prt_txt(f"\n{target.name.upper()} HITS, AND DOES {target.DMG_R} DAMAGE!\n")
                #Force Field check
                for item in Follow_1.inventory.values():
                    #TEST\\\\\\\\\\\\\\\
                    #print("TRIGGER FORCE FIELD\nitem.name>>> ", item.name)
                    #///////////////////
                    if item == "EMPTY":
                        pass
                    elif item.name == "Force Field":
                        use_force_field = input(f"{Follow_1.name.upper()} HAS A FORCEFIELD IN THEIR INVENTORY WHICH CAN BE USED TO NEGATE INCOMING DAMAGE. WOULD YOU LIKE TO USE IT NOW?\n\n[Y/N]\n--[").upper()
                        if use_force_field == "Y":
                            Follow_1.HP += target.DMG_R
                        elif use_force_field == "N":
                            pass
            else:
                prt_txt(f"\n{target.name.upper()} MISSES!\n")
            return_fire = False
    
    #//////// LEAD MELEE ACTIONS//////
    
   

    elif len(target.HP) > 0 and melee == True:
         #TEST\\\\
        #print("\nTEST L + F .action, target.hp >>>> " , Lead_1.action, Follow_1.action, target.HP)
        #////////
        melee_result_lead = []
        if len(Lead_1.action) == 1:
            if Lead_1.action in target.HP :
                target.HP.remove(Lead_1.action)
                melee_result_lead.append("melee_hit")
            else: 
                melee_result_lead.append("melee_miss")
        elif len(Lead_1.action) > 1:
            for i in Lead_1.action:
                if i in target.HP:
                    target.HP.remove(i)
                    melee_result_lead.append("melee_hit")
                elif i == "S":
                    melee_result_lead.append("melee_dodge")
                else: 
                    melee_result_lead.append("melee_miss")
            #Rusty Pipe Re-Roll
        if "melee_miss" in melee_result_lead:    
            for item in Lead_1.inventory.values():
                if item == "EMPTY":
                        pass
                elif item.name == "Rusty Pipe":
                    #TEST\\\\\\\\\\\\\\\
                    #print("RUSTY PIPE TRIGGER REROLL\nORIGINAL ROLL >>>> ", Lead_1.action, "\nNEW ROLL >>> " )
                    #///////////////////
                    Lead_1.action = Lead_1.character_die()
                    #TEST CONT\\\\\
                    #print(Lead_1.action)
                    #//////////////
                    if len(Lead_1.action) == 1:
                        if Lead_1.action in target.HP :
                            target.HP.remove(Lead_1.action)
                            melee_result_lead.append("melee_hit")
                        else: 
                            melee_result_lead.append("melee_miss")
                    elif len(Lead_1.action) > 1:
                        for i in Lead_1.action:
                            if i in target.HP:
                                target.HP.remove(i)
                                melee_result_lead.append("melee_hit")
                            elif i == "S":
                                melee_result_lead.append("melee_dodge")
                    else:
                        melee_result_lead.append("melee_miss")

        if "melee_hit" in melee_result_lead:
            prt_txt(f"{Lead_1.name.upper()} HITS {target.name.upper()} IN CLOSE QUARTERS!")
        else:
            prt_txt(f"{Lead_1.name.upper()} MISSES!")

    
    #//////// FOLLOW MELEE ACTIONS ////////
        melee_result_follow = []
        if len(Follow_1.action) == 1:
            if Follow_1.action in target.HP :
                target.HP.remove(Follow_1.action)
                melee_result_follow.append("melee_hit")
            else: 
                melee_result_lead.append("melee_miss")
        elif len(Follow_1.action) > 1:
            for i in Follow_1.action:
                if i in target.HP:
                    target.HP.remove(i)
                    melee_result_follow.append("melee_hit")
                elif i == "S":
                    melee_result_follow.append("melee_dodge")
                else:
                    melee_result_follow.append("melee_miss")
            #Rusty Pipe Re-Roll
        if "melee_miss" in melee_result_follow:    
            for item in Follow_1.inventory.values():
                if item == "EMPTY":
                    pass
                elif item.name == "Rusty Pipe":
                    #TEST\\\\\\\\\\\\\\\
                    #print("RUSTY PIPE TRIGGER REROLL\nORIGINAL ROLL >>>> ", Follow_1.action, "\nNEW ROLL >>> " )
                    #///////////////////
                    Follow_1.action = Follow_1.character_die()
                    #TEST CONT\\\\\
                    #print(Follow_1.action)
                    #//////////////
                    if len(Follow_1.action) == 1:
                        if Follow_1.action in target.HP :
                            target.HP.remove(Follow_1.action)
                            melee_result_follow.append("melee_hit")
                    elif len(Follow_1.action) > 1:
                        for i in Follow_1.action:
                            if i in target.HP:
                                target.HP.remove(i)
                                melee_result_follow.append("melee_hit")
                            elif i == "S":
                                melee_result_follow.append("melee_dodge")
                    else:
                        melee_result_follow.append("melee_miss")
            

        if "melee_hit" in melee_result_follow:
            prt_txt(f"{Follow_1.name.upper()} HITS {target.name.upper()} IN CLOSE QUARTERS!")
        else:
            prt_txt(f"{Follow_1.name.upper()} MISSES!")


        
        #/////// TARGET MELEE RETALIATION //////

        #TEST \\\\\\\
        #print("TEST lead+follow melee reult list >>>>> ", melee_result_lead, melee_result_follow)
        #////////////
        if len(target.HP) == 0:
            prt_txt(f"{target.name.upper()} IS DEAD!")
            #TEST\\\\\\\\\
            #print("TRIGGER END 2")
            #//////////////
            loot_target(Lead_1, Follow_1, target, target.loot)
            return end_seq(ending)
        else:
            prt_txt(f"{target.name.upper()} HITS BACK!\n")
            #HIT BACK ON LEAD
            if "melee_dodge" not in melee_result_lead:
                Lead_1.HP -= target.DMG_M
                prt_txt(f"\n///{target.name.upper()} HITS BACK AND DOES {target.DMG_M} DAMAGE TO {Lead_1.name.upper()}")
            #Forcefield Check
                for item in Lead_1.inventory.values():
                    #TEST\\\\\\\\\\\\\\\
                    #print("TRIGGER FORCE FIELD\nitem.name>>> ", item.name)
                    #///////////////////
                    if item == "EMPTY":
                        pass
                    elif item.name == "Force Field":
                        prt_txt(f"{Lead_1.name.upper()} HAS A FORCEFIELD IN THEIR INVENTORY WHICH CAN BE USED TO NEGATE INCOMING DAMAGE. WOULD YOU LIKE TO USE IT NOW?\n\n[Y/N]\n")
                        use_force_field = take_in("Y / N")
                        if use_force_field == "Y":
                            Lead_1.remove_inventory(force_field)
                            Lead_1.HP += target.DMG_M
                        elif use_force_field == "N":
                            pass    
            else:
                prt_txt(f"{Lead_1.name.upper()} DODGES {target.name.upper()}'S ATTACK!")

            #HIT BACK ON FOLLOW
            if "melee_dodge" not in melee_result_follow:
                Follow_1.HP = Follow_1.HP - target.DMG_M
                prt_txt(f"\n///{target.name} HITS BACK AND DOES {target.DMG_M} DAMAGE TO {Follow_1.name}")
                for item in Follow_1.inventory.values():
                    #TEST\\\\\\\\\\\\\\\
                    #print("TRIGGER FORCE FIELD\nitem.name>>> ", item.name)
                    #///////////////////
                    if item == "EMPTY":
                        pass
                    elif item.name == "Force Field":
                        prt_txt(f"{Follow_1.name.upper()} HAS A FORCEFIELD IN THEIR INVENTORY WHICH CAN BE USED TO NEGATE INCOMING DAMAGE. WOULD YOU LIKE TO USE IT NOW?\n\n[Y/N]\n")
                        use_force_field = take_in("Y / N")
                        if use_force_field == "Y":
                            Follow_1.remove_inventory(force_field)
                            Lead_1.HP += target.DMG_M
                            pass
                        elif use_force_field == "N":
                            pass
            else:
                prt_txt(f"{Follow_1.name.upper()} DODGES {target.name.upper()}'S ATTACK!")



    if len(target.HP) == 0  :
        prt_txt(f"{target.name.upper()} IS DEAD")
        #TEST\\\\\\\\\\\\
        #print("TRIGGER END 3")
        #////////////////
        loot_target(Lead_1, Follow_1, target, target.loot)
        return end_seq(ending)
    elif len(target.HP) > 0 :
        for actions in action_lst :
            for action in actions:
                if action in ["hit" , "crit" , "jam" , "miss"] :
                    prt_txt(f"\n{target.name.upper()} IS STILL ALIVE!\nPREPARE FOR ANOTHER ROUND OF COMBAT!")
        #///////// FLANK ROUND ////////////
                    flanker = None 
                    if "flank" in Lead_1.action:
                        flanker = Lead_1
                    elif "flank" in Follow_1.action:
                        flanker = Follow_1
                    if flanker:
                        prt_txt(f"\n///AFTER DASHING TO COVER IN A SECURE VANTAGE POINT, {flanker.name.upper()} PREPARES TO ATTACK...///\nCHOOSE ACTION:\nA: SHOOT\nX: CHARGE\n")
                        a1 = take_in("A / X")
                        if a1 == "A" :
                            flanker.show_inventory()
                            slot_choice = input("CHOICE [ENTER 1 / 2 / 3 / 4]: ")
                            slot_choice = int(slot_choice)
                            flanker.weapon_choice = flanker.inventory.get(slot_choice)
                            shots = flanker.weapon_choice.rate_of_fire_1
                            flanker_action = []
                            #TEST\\\\\\\\\\\\\\\\\
                            #print(flanker.weapon_choice.name)
                            #/////////////////////
                            while flanker.weapon_choice.ammo < 1 :
                                prt_txt("CLICK CLICK CLICK... YOU'RE OUT OF AMMO! CHOOSE ANOTHER WEAPON, OR RELOAD\n")
                                flanker.show_inventory()
                                slot_choice = input("CHOICE [ENTER 1 / 2 / 3 / 4]: ")
                                slot_choice = int(slot_choice)
                                flanker.weapon_choice = flanker.inventory.get(slot_choice)
                                shots = flanker.weapon_choice.rate_of_fire_1
                            if type(flanker.weapon_choice.rate_of_fire_2) == int :
                                prt_txt("CHOOSE RATE OF FIRE:\nA: {rof_1}\nB: {rof_2}\n--[".format(rof_1 = flanker.weapon_choice.rate_of_fire_1 , rof_2 = flanker.weapon_choice.rate_of_fire_2))
                                a1 = take_in("A / B")
                                if a1 == "A" :
                                    shots = flanker.weapon_choice.rate_of_fire_1
                                elif a1 == "B" :
                                    shots = flanker.weapon_choice.rate_of_fire_2
                            if flanker.weapon_choice.dmg_type == "ballistic" :
                                for shot in range(0 , shots) :
                                    character_roll = randint(1 , 6)
                                    flanker.weapon_choice.ammo = flanker.weapon_choice.ammo - shots
                                    if character_roll in range(1 , 4) :
                                        flanker_action.append("hit")
                                    elif character_roll == 4 :
                                        flanker_action.append("jam")
                                    elif character_roll == 5 :
                                        flanker.weapon_choice.ammo = flanker.weapon_choice.ammo - 1
                                        flanker_action.append("crit")
                                    elif character_roll == 6 :
                                        flanker_action.append("miss")
                            elif flanker.weapon_choice.dmg_type == "energy":
                                #TEST\\\\\\
                                #print("TRIGGER==========================")
                                #//////////
                                for shot in range(0, shots) :
                                    character_roll = randint(1 , 6)
                                    flanker.weapon_choice.ammo = flanker.weapon_choice.ammo - shots
                                    if character_roll in range(1 , 5) :
                                        dmg = target.DMG_Pro.get(flanker.weapon_choice.dmg_type)
                                        flanker_action.append("hit")
                                    elif character_roll == 5 :
                                        flanker_action.append("overheat")
                                    elif character_roll == 6 :
                                        flanker_action.append("miss")
                            #TEST\\\\\\\\\\\\\\\
                            #print("TEST flanker_action++++++++++++", flanker_action)
                            #///////////////////
                            for result in flanker_action :
                                if result == "jam" :
                                    prt_txt(f"\n{flanker.name.upper()}'S WEAPON JAMS!\n")
                                    #Prevents additional shots going through if weapon jams
                                    result = ["jam"]
                                elif "overheat" in flanker_action:
                                    prt_txt(f"{flanker.name.upper()}'S WEAPON OVERHEATS, CAUSING SERIOUS BURNS! {flanker.name.upper()} LOSES 1 HP!\n")
                                    flanker.HP -= 1
                                    result = ["overheat"]
                                if result is "hit" :
                                    #Flanking shots do one extra damage
                                    dmg = target.DMG_Pro.get(flanker.weapon_choice.dmg_type) + 1
                                    prt_txt(f"\n{flanker.name.upper()} HITS! ALLOCATE {dmg} DAMAGE TO {target.name.upper()}:\n{target.name.upper()} HEALTH PROFILE: {target.HP}\n")
                                    target_HP = list(input().upper())
                                    dmg_lst = list(range(1 , (dmg + 1)))
                                    for x in dmg_lst :
                                        for z in target.HP :
                                            if z in target_HP :
                                                if len(target.HP) == 0 :
                                                    prt_txt(f"{target.name} IS DEAD!")
                                                    #TEST\\\\\\\\\\\\\
                                                    #print("TRIGGER END 4")
                                                    #/////////////////
                                                    loot_target(Lead_1, Follow_1, target, target.loot)
                                                    return end_seq(ending)
                                                target.HP.remove(z)
                                                target_HP.remove(target_HP[0])
                                                break
                                elif result is "crit" :
                                    dmg = target.DMG_Pro.get(flanker.weapon_choice.dmg_type) * 2 + 1
                                    prt_txt(f"\n{Lead_1.name.upper()} SCORES A CRITICAL HIT! ALLOCATE {dmg} DAMAGE TO {target.name.upper()}:\n{target.name.upper()} HEALTH PROFILE: {target.HP}\n")
                                    target_HP = list(input().upper())
                                    dmg_lst = list(range(1 , (dmg + 1)))
                                    for x in dmg_lst :
                                        for z in target.HP :
                                            if z in target_HP :
                                                target.HP.remove(z)
                                                target_HP.remove(target_HP[0])
                                                break
                                    prt_txt(f"\n{target.name} HP: {target.HP}\n")
                                elif result is "miss" :
                                    prt_txt(f"\n{Lead_1.name.upper()} MISSES!\n")
                        elif a1 == "X" :
                            #In flank melee, attacker removes one extra wound from target, and suffers no return damage
                            prt_txt(f"\n{flanker.name.upper()} CHARGES HEADLONG INTO THE {target.name.upper()}, TAKING IT COMPLETELY BY SURPRISE!")
                            character_roll = flanker.character_die()
                            for i in character_roll :
                                melee_result = []
                                if i in target.HP :
                                    target.HP.remove(i)
                                    melee_result.append("hit")
                                elif i == "S":
                                    melee_result.append("dodge")
                                else:
                                    melee_result.append("miss")
                            if "hit" in melee_result:
                                prt_txt(f"{flanker.name.upper()} HITS {target.name.upper()} IN CLOSE QUARTERS!")
                                prt_txt(f"\nALLOCATE 1 ADDITIONAL DAMAGE TO {target.name.upper()}\nHEALTH PROFILE: {target.HP}\n")
                                target_HP = input("--[").upper()
                                for hp in target.HP :
                                    if hp == target_HP :
                                        target.HP.remove(hp)
                                prt_txt(f"\nNEW {target.name.upper()} HP: {target.hp}")
                            else:
                                prt_txt(f"{flanker.name.upper()} MISSES!")
                    if len(target.HP) > 0:
                        Lead_1.action = []
                        Follow_1.action = []
                        Choose_Player_Ranged(Lead_1 , Follow_1 , target , [], modifier, ending)
                    else:
                        prt_txt(f"{target.name.upper()} IS DEAD")
                        #TEST\\\\\\\\\\
                        #print("TRIGGER END 5")
                        #//////////////
                        loot_target(Lead_1, Follow_1, target, target.loot)
                        return end_seq(ending)        
        #//////// CLOSE COMBAT CHECK ////////
        #/////// END OF TURN MODIFIER CHECK////////
        if modifier == "tentacles":
            prt_txt(f"CONTINUE FIGHTING {target.name.upper()}?\n[1] RUN\n[2] CONTINUE FIGHTING")
            a1 = take_in("1 / 2")
            if a1 == "1":
                prt_txt("THE CREW PULL THEMSELVES FREE FROM THE ABOMINATION, BUT LOSE 1HP IN THE PROCESS!")
                Lead_1.HP -= 1
                Follow_1.HP -= 1
                end_seq(ending)
                return
            elif a1 == "2":
                prt_txt("THE CREW PILE IN TO DEFEAT THE ABOMINATION!")
                pass
        # Forces close combat if no shooting found in action_lst             
        prt_txt(f"\n{target.name.upper()} CLOSES IN! PREPARE FOR CLOSE COMBAT!")
        Lead_1.action = []
        Follow_1.action = []
        Choose_Player_Melee(Lead_1 , Follow_1 , target , [], modifier, ending)


def Trade_In_Combat(trader, giver) :
    trader.show_inventory()
    giver.show_inventory()
    prt_txt(f"""
CHOOSE AN ITEM FROM {giver.name.upper()}'S INVENTORY TO GIVE TO {trader.name.upper()}
    """)
    prt_txt("[SLOT NO.]")
    a1 = int(take_in("1 / 2 / 3 / 4"))
    for slot in giver.inventory.keys():
        if a1 == slot:
            trade_item = giver.inventory.get(slot)
            trader.add_inventory(trade_item)
            giver.remove_inventory(trade_item)
            if trade_item.type == "item" :
                prt_txt(f"WOULD YOU LIKE TO USE {trade_item.name} NOW?\n[Y/N]")
                a2 = take_in("Y / N")
                if a2 == "Y" : 
                    trade_item.use(trader)



   
