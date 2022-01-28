from time import *
from ds_engine_nov_2021 import *
from ds_classes_nov_2021 import *




def intro_1():
    intro_text = [
        "                       ______  ___  ______ _   __  _____ _____ _____ _____ ___________ ",
        "                       |  _  \/ _ \ | ___ \ | / / /  ___|  ___/  __ \_   _|  _  | ___ \ ",
        "                       | | | / /_\ \| |_/ / |/ /  \ `--.| |__ | /  \/ | | | | | | |_/ /",
        "                       | | | |  _  ||    /|    \   `--. \  __|| |     | | | | | |    / ",
        "                       | |/ /| | | || |\ \| |\  \ /\__/ / |___| \__/\ | | \ \_/ / |\ \ ",
        "                       |___/ \_| |_/\_| \_\_| \_/ \____/\____/ \____/ \_/  \___/\_| \_|"
    ]
    for line in intro_text:
        print(line)
        sleep(0.2)                                                            
    sleep(1)
    prt_txt("""                                                            
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
After weeks of being confined to the detention block, you finally break free of your cell.

Outside, the lighting flickers intermittently and the burning stench of recent laser fire hangs in the air.

Beside a slaughtered guard, a weapon locker has been smashed open. You load up on what little gear and ammunition remains...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    """)
    sleep(2)
    prt_txt("LOCKER:\n\n[1] SLUG PISTOL\n[2] RAY GUN")
 
    prt_txt("\n\nWHO WILL TAKE THE SLUG PISTOL?\n[1] LT. ABBOTT\n[2] LT. MILLER")
 
    a1 = take_in("1 / 2")
    if a1 == "1":
        abbot.add_inventory(slug_pistol_opener)
        prt_txt("\nLT MILLER TAKES THE RAY GUN.")
        miller.add_inventory(ray_gun_opener)
    elif a1 == "2":
        miller.add_inventory(slug_pistol_opener)
        prt_txt("\nLT ABBOT TAKES THE RAY GUN.")
        abbot.add_inventory(ray_gun_opener)
   
    prt_txt("""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
You hear footsteps approaching; there is no time to lose. 
You must find your ship at all costs. You steel yourselves before slipping away into the gloom...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    """)
    
def seq_1(player_1, player_2):
    intermission(player_1, player_2)
   
    prt_txt(
        """
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
You enter a room lined with magnetically sealed deposit boxes, filled with contraband
confiscated from detention block prisoners...

CHOOSE:
[1] MOVE ON
[2] ATTEMPT TO HACK
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """
    )
    a1 = take_in("1 / 2")
    
    if a1 == "1":
       
        prt_txt("You continue your journey into the depths of the station - time is of the essence!")
    elif a1 == "2":
     
        prt_txt("""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
The boxes appear to be secured with security shock-nodes...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
      
        prt_txt("\nYOUR CHARACTER WILL NEED TO SCORE A W ON AN ATTRIBUTE TEST TO SUCCESSFULLY HACK THE BOXES")
      
        prt_txt("\nLT. ABBOT'S CHANCE OF SUCCESS:")
        count = 0
        #TEST\\\\\\\\\\\\\\\\\\
        #prt_txt(abbot.character_die_lst, miller.character_die_lst)
        #TEST//////////////////
        for i in abbot.character_die_lst:
            if "W" in i:
                count += 1
        percent = (round((count / 6) * 100, 0))
        prt_txt(f" {str(percent)}%")
        prt_txt("\nLT. MILLER'S CHANCE OF SUCCESS:")
        count = 0
        for i in miller.character_die_lst:
            if "W" in i:
                count += 1
        percent = (round((count / 6) * 100, 0)) 
        prt_txt(f" {str(percent)}%")
        prt_txt("\nARE YOU SURE YOU WANT TO CONTINUE? Y/N\n")
        a2 = take_in("Y / N")
        if a2 == "N" :
           
            prt_txt("""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
You continue your journey into the depths of the station - time is of the essence!
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////            
            """)
        if a2 == "Y":
            prt_txt("\nNOMINATE A CREWMEMBER TO ATTEMPT THE HACK:\n[1] LT. ABBOT\n[2] LT. MILLER\n")
            a3 = take_in("1 / 2")
            if a3 == "1":
                acting = abbot
                seq_1_hack(abbot)
            elif a3 == "2":
                acting = miller
                seq_1_hack(miller)
            
def seq_2(player_1, player_2):
    #Below should be replaced by intermission() function
    intermission(player_1, player_2)
    
    prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
You pass a room where an engineer is repairing droids.
She is so absorbed in the work that you spot an opportunity to steal from her...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 
CHOOSE:
[1] MOVE ON
[2] ATTEMPT TO STEAL
    """)
   
    a1 = take_in("1 / 2")
    if a1 == "1":
        
        prt_txt("""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
You continue your journey into the depths of the station - time is of the essence!
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
    elif a1 == "2":
        
        prt_txt("\nYOUR CHARACTER WILL NEED TO SHOW CUNNING ON AN ATTRIBUTE TEST TO SUCCESSFULLY HACK THE BOXES")
        prt_txt("\nLT. ABBOT'S CHANCE OF SUCCESS:")
        count = 0
        #TEST\\\\\\\\\\\\\\\\
        #prt_txt(abbot.character_die_lst, miller.character_die_lst)
        #////////////////////
        for i in abbot.character_die_lst:
            if "C" in i:
                count += 1
        percent = (round((count / 6) * 100, 0))
        prt_txt(f"{str(percent)}%")
        prt_txt("\nLT. MILLER'S CHANCE OF SUCCESS:")
        count = 0
        for i in miller.character_die_lst:
            if "C" in i:
                count += 1
        percent = (round((count / 6) * 100, 0)) 
        prt_txt(f"{str(percent)}%")
        a2 = str(input("\nARE YOU SURE YOU WANT TO CONTINUE? Y/N\n--[")).upper()
        if a2 == "N" :
           
            prt_txt("""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
You continue your journey into the depths of the station - time is of the essence!
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////            
            """)
        if a2 == "Y":
            prt_txt("\nNOMINATE A CREWMEMBER TO ATTEMPT TO STEAL:\n[1] LT. ABBOT\n[2] LT. MILLER\n")
            a3 = take_in("1 / 2")
            if a3 == "1":
                acting = abbot
                seq_2_steal(abbot)
            elif a3 == "2":
                acting = miller
                seq_2_steal(miller)
            
def seq_3(player_1, player_2):
    a1 = input(f"\nCHOOSE A PLAYER TO LEAD\nA: {player_1.name.upper()}\nB: {player_2.name.upper()}\n--[").upper()
    if a1 == "A":
        Lead_1 = player_1
        Follow_1 = player_2
    elif a1 == "B":
        Follow_1 = player_1
        Lead_1 = player_2
    prt_txt(f"{Lead_1.name.upper()} LEADS THE GROUP INTO THE DARKNESS...\n")
    prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
As the doors ahead hiss open, slimy tentacles fly out and seize {Lead_1.name},
dragging them into the darkness beyond...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

{Lead_1.name.upper()} LOSES 1 HP!

YOU MUST PLAY ONE ROUND OF CLOSE COMBAT TO FREE YOURSELVES!

    """)
    Choose_Player_Melee(Lead_1, Follow_1, tentacles, [], "tentacles", "seq_3")

def seq_4(player_1, player_2):
    intermission(player_1, player_2)
    player_1_chance = [chance_calculator(player_1, "C"), chance_calculator(player_1, "W")]
    player_2_chance = [chance_calculator(player_2, "C"), chance_calculator(player_2, "W")]
    prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
The way forward is blocked by an ever-shifting
lasergrid - a perplexing pattern of buzzing, burning beams...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

EACH MEMBER OF THE CREW MUST ATTEMPT TO CROSS THE LASERGRID USING EITHER THEIR CUNNING, OR SPEED.

{player_1.name.upper()}'S CHANCES:
CUNNING: {player_1_chance[0]}
WISDOM:  {player_1_chance[1]}

{player_2.name.upper()}'S CHANCES
CUNNING: {player_2[0]}
WISDOM:  {player_2[1]}
    """)
    a2 = input(f"CHOOSE {player_1.name.upper()}'S ATTEMPT:\n[1] CUNNING\n[2] WISDOM\n--[")
    if a2 == "1":
        player_1.action = "C"
    elif a2 == "2":
        player_1.action = "W"
    a3 = input(f"CHOOSE {player_2.name.upper()}'S ATTEMPT:\n[1] CUNNING\n[2] WISDOM\n--[")
    if a3 == "1":
        player_2.action = "C"
    elif a3 == "2":
       player_2.action = "W"
    seq_4_lasergrid(player_1, player_2)


def seq_5(player_1, player_2):
    Lead_1, Follow_1 = intermission(player_1, player_2)
    prt_txt(f"""\n
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
The battle-broken limbs of a cyborg guard hiss and whine as it falters towards you,
a singular directive still coursing through its fried circuits; "SURRENDER. OR. DIE."
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

CHOOSE:

[1] ATTACK
[2] EVADE
    """)
    a1 = take_in("1 / 2")
    if a1 == "1":
        Choose_Player_Ranged(Lead_1, Follow_1, cyborg, [], None, "seq_5")
    elif a1 == "2":
        prt_txt(f"AS YOU SCRAMBLE TO DOUBLE BACK, THE CYBORG UNLEASHES A VOLLEY OF LASER-FIRE AT {Lead_1.name}")

def seq_6(player_1, player_2):
    Lead_1, Follow_1 = intermission(player_1, player_2)
    prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
As you enter a disused hangar, you notice a two lizardmen carrying out a brutal
interrogation on a pleading hostage. You won't be able to make it through without
them noticing you, and they don't seem like they would take kindly to your intrusion...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

CHOOSE:

[1] ATTACK
[2] INTIMIDATE
    """)
    a1 = take_in("1 / 2")
    if a1 == "1":
        prt_txt("\nGIVE 'EM HELL!")
        Choose_Player_Ranged(Lead_1, Follow_1, lizardmen, [], None, seq_6)
    elif a1 == "2":
        prt_txt(f"""
NOMINATE A CREW MEMBER TO TRY AND INTIMIDATE THE LIZARDMEN:

[1] {Lead_1.name.upper()}'S CHANCE OF SUCCESS: {chance_calculator(Lead_1, "W")}
[2] {Follow_1.name.upper()}'S CHANCE OF SUCCESS: {chance_calculator(Follow_1, "W")}
        """)
        a2 = take_in("1 / 2")
        if a2 == "1":
            result = story_character_roll(Lead_1, "W", 1)
        elif a2 == "2":
            result = story_character_roll(Follow_1, "W", 1)
        if result == "success":
            item = loot_gen(1)
            prt_txt("\nTHE LIZARDMEN BACK OFF, OFFERING YOU AN ITEM TO APPEASE YOUR THREAT")
            prt_txt(f"--[SALVAGE:\n-{item.name.upper()}")
            prt_txt(f"ASSIGN A MEMBER OF THE CREW TO RECIEVE {item.name.upper()}")
            prt_txt(f"--[ABBOT [1]\n--[MILLER [2]")
            a1 = take_in(1 / 2)
            if a1 == "1" :
                abbot.add_inventory(item)
            elif a1 == "2" :
                miller.add_inventory(item)
        elif result == "fail":
            prt_txt(f"""
THE LIZARDMEN LAUGH IN YOUR FACE AS THEY DRAW THEIR WEAPONS AND OPEN FIRE ON THE CREW!
            """)
            lizardmen_roll = randint(1, 6)
            if lizardmen_roll in range(1, 4):
                prt_txt(f"\n{Lead_1.name.upper()} IS HIT!")
                Lead_1.HP -= 2
            else:
                prt_txt("\nTHE CREW DIVE INTO COVER JUST IN TIME TO AVOID THE INCOMING FIRE!")
            Choose_Player_Ranged(Lead_1, Follow_1, lizardmen, [], None, "seq_6")

def seq_7(player_1, player_2):
    Lead_1, Follow_1 = intermission(player_1, player_2)
    prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
The crew move on into the next hangar, hoping to find a ship to 
escape from the station. Unfortunately, they all appear to be in a state of disrepair,
or stripped of vital components, presumably by scavangers.
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """)
    prt_txt(f"\nAS {Lead_1.name.upper()} ENTERS ONE OF THE DOCKED SHIPS TO INSPECT IT, A SCREECHING ALIEN POUNCES FROM THE DARKNESS,\nIT'S HOOKED LIMBS PULLING {Lead_1.name.upper()} TOWARDS IT's GAPING MAW...")
    result = story_character_roll(Lead_1, "C", 1)
    if result == "success":
        prt_txt(f"{Lead_1.name.upper()} STARTLES THE ALIEN WITH A BURST OF LIGHT FROM HIS VISOR-MOUNTED FLASHLIGHT BEFORE DIVING INTO COVER!")
    elif result == "fail":
        prt_txt(f"{Lead_1.name.upper()} SCREAMS AS THE ALIEN TEARS INTO HIS SUIT WITH IT'S RAZOR SHARP MANDIBLES!")
        Lead_1.HP -= 2
    prt_txt("CHOOSE:\n[1] ATTACK\n[2] FLEE")
    a1 = take_in("1 / 2")
    if a1 == "1":
        prt_txt(f"THE CREW PILE IN TO SAVE {Lead_1.name.upper()}!")
        Choose_Player_Melee(Lead_1, Follow_1, alien, [], None, seq_7)
    elif a1 == "2":
        prt_txt(f"{Lead_1.name.upper()} MANAGES TO ESCAPE THE CLUTCHES OF THE ALIEN,\nBUT NOT BEFORE IT SKEWERS HIS ARM WITH ONE OF IT'S RAZOR-SHARP LIMBS!")
        Lead_1.HP -= 1
        prt_txt("\nTHE CREW FLEE THE HANGAR IN A PANIC!")

def seq_8(player_1, player_2):
    Lead_1, Follow_1 = intermission(player_1, player_2)
    prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
After abandonning the search for a workable ship in the hangar bays, 
the crew decide to make for the escape pods and try their luck on the planet below.
As they enter the chamber housing the escape pods, a gutteral roar stops the crew dead in their tracks...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

HEAVY FOOTSTEPS ARE HEARD AS A LUMBERING MUTANT ENTERS THE CHAMBER TO CONFRONT THE CREW...
    """)
    Choose_Player_Ranged(Lead_1, Follow_1, mutant, [], "regen", "seq_8")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#///////////////// SEQUENCE FUNCTIONS /////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#///////////////// SEQUENCE FUNCTIONS /////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def intermission(player_1, player_2):
    prt_txt(f"CHOOSE A PLAYER TO LEAD THE GROUP TO THE NEXT AREA\n\n[1] {player_1.name.upper()}\n[2] {player_2.name.upper()}")
    a1 = take_in("1 / 2")
    if a1 == "1":
        Lead_1 = player_1
        Follow_1 = player_2
    else:
        Lead_1 = player_2
        Follow_1 = player_1
    return Lead_1, Follow_1

def story_character_roll(character, target, attempts):
    success_rolls = 0
    rolls = []
    for roll in range(0, attempts):
        #TEST\\\\\\\\\\\\\\\\\\\\\\\\\\\
        prt_txt("TEST ATTEMPT>>> ", roll)
        #///////////////////////////////
        rolls.append(character.character_die())
    for result in rolls:
        for letter in result:
            if letter == target:
                success_rolls += 1
                break
    #TEST\\\\\\\\\\\\\
    prt_txt("story_character_roll results success_rolls, rolls>>>>>", success_rolls, rolls)
    #/////////////////
    if success_rolls > 0:
        return "success"
    else:
        return "fail"

#WIP simplified story roll
def story_character_roll_2(character, aim, tries):
    #chance from one roll
    while tries > 0:
        roll = character.character_die()
        for letter in roll:
            if letter == aim:
                prt_txt("WIN")
            else:
                tries -= 1
    prt_txt("FAIL")

def chance_calculator(character, aim):
    success_rolls = 0
    for value in character.character_die_lst:
        for letter in value:
            if letter == aim:
                success_rolls += 1
                break
    chance = round(success_rolls/6, 2)
    perc = str(chance * 100) + "%"
    return perc

def seq_1_hack(acting):
    character_roll = [acting.character_die()]
    #TEST \\\\\\\\\\\\\\
    #prt_txt(character_roll)
    #////////////////////
    W_count = 0
    #TEST\\\\\\
    #prt_txt(W_count)
    #//////////
    for roll in character_roll:
        for letter in roll:
            if letter == "W":
                W_count += 1
    if W_count == 1:
        items = loot_gen(1)
        taker = None
        prt_txt(f"""
{acting.name} has opened the safe! 
You peer in and see what you can salvage...

--[SALVAGE
-{items[0].name}
-
-
-
        """)
        while len(items) > 0:
            for item in items:
                prt_txt(f"ASSIGN A MEMBER OF THE CREW TO RECIEVE {item.name.upper()}")
                prt_txt(f"--[ABBOT [1]\n--[MILLER [2]")
                a1 = take_in("1 / 2")
                if a1 == "1" :
                    abbot.add_inventory(item)
                    items.remove(item)
                elif a1 == "2" :
                    miller.add_inventory(item)
                    items.remove(item)
        prt_txt("""

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
After gathering your items, you proceed into the depths of the station...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        """)

    elif W_count == 2:
        items = loot_gen(2)
        taker = None
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
{acting.name} finds more than one box with the same unlock sequence!
You prise open several boxes to see what's inside...

--[SALVAGE
-{items[0]}
-{items[1]}
-
-
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
        while len(items) > 0:
            for item in items:
                prt_txt(f"ASSIGN A MEMBER OF THE CREW TO RECIEVE {item.name.upper()}")
                prt_txt(f"--[ABBOT [1]\n--[MILLER [2]")
                a1 = take_in("1 / 2")
                if a1 == "1" :
                    abbot.add_inventory(item)
                    items.remove(item)
                    prt_txt(items)
                elif a1 == "2" :
                    miller.add_inventory(item)
                    items.remove(item)
        prt_txt("""

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
After gathering your items, you proceed into the depths of the station...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        """)
    elif W_count == 0:
        acting.HP - 2
        prt_txt(f"\n{acting.name.upper()} FAILS TO BYPASS THE BOX'S SECURITY AND RECIEVES A LESS_THAN_LETHAL ELECTRIC SHOCK, LOSING 2 HP")

        
def seq_2_steal(acting):
    character_roll = [acting.character_die()]
    #TEST \\\\\\\\\\\\\\
    #prt_txt(character_roll)
    #////////////////////
    C_count = 0
    #TEST\\\\\\
    #prt_txt(W_count)
    #//////////
    for roll in character_roll:
        for letter in roll:
            if letter == "C":
                C_count += 1
    #TEST\\\\\\\\\\\\\
    #prt_txt(C_count)
    #/////////////////
    if C_count > 0:
        items = loot_gen(2)
        taker = None
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
{acting.name} deftly crawls amongst the disused workbenches, and avoids attracting the engineer's attention.
Some likely salvage catches their eye and they quickly retrieve it before returning to their party. 

--[SALVAGE
-{items[0].name}
-{items[1].name}
-
-
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        """)
        while len(items) > 0:
            for item in items:
                prt_txt(f"ASSIGN A MEMBER OF THE CREW TO RECIEVE {item.name.upper()}")
                prt_txt(f"--[ABBOT [1]\n--[MILLER [2]")
                a1 = take_in("1 / 2")
                if a1 == "1" :
                    abbot.add_inventory(item)
                    items.remove(item)
                elif a1 == "2" :
                    miller.add_inventory(item)
                    items.remove(item)
        prt_txt("""

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
After gathering your items, you proceed into the depths of the station...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        """)
    elif C_count == 0:
        prt_txt(f"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
{acting.name} triggers an alarm as they step into the room where the engineer is working.
As they engineer looks up, they quickly draw a holstered pistol and take aim...
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

BEGIN COMBAT
        """)
        Choose_Player_Ranged(abbot, miller, engineer, [], None, "seq_2")

def seq_4_lasergrid(Lead_1, Follow_1):
    lead_roll = Lead_1.character_die()
    follow_roll = Follow_1.character_die()
    #LEAD
    for value in lead_roll:
        if value == Lead_1.action:
            prt_txt(f"{Lead_1.name.upper()} GETS THROUGH THE LASERGRID UNHARMED")
            break
        else:
            prt_txt(f"{Lead_1.name.upper()} TRIPS AND IS BURNT BY THE LASERGRID, LOSING 2 HP")
            Lead_1.HP -= 2
            break
    #FOLLOW
    for value in follow_roll:
        if value == Follow_1.action:
            prt_txt(f"{Follow_1.name.upper()} GETS THROUGH THE LASERGRID UNHARMED")
            break
        else:
            prt_txt(f"{Follow_1.name.upper()} TRIPS AND IS BURNT BY THE LASERGRID, LOSING 2 HP")
            Follow_1.HP -= 2
            break
    prt_txt("YOU MARCH OFF INTO THE DARKNESS...")


    