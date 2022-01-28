HOW TO PLAY

-Run play_ds.py in terminal

COMBAT

In the boardgame, both player characters and enemy types share four key attributes: Might, Cunning, Wisdom and Strength. 

For now, these are represented simply as M, C, W, and S respectively. 

When an enemy is loaded, their 'health' is composed of a given number of 'blocks', each assigned a value of M/C/W/S, plus at least two more which are randomly generated form the same traits.

In ranged combat, players that score a hit can remove one 'block' for each point of 'damage' they do. 

In melee combat, players must 'roll' their 'character die' to try and match one of the 'blocks' on the enemy's list. Characters have varying chances of doing so depending on their attributes. 

DEV NOTES

#TO BE ADDED - 
#Player death when no HP

#BUGS 
#Check that items in the items roster cannot be assigned twice - starting weapons should
#be duplicated / registered separately 
#Weapons shooting on empty not triggering reload prompt 
#Scripting loop issue after engineer is killed
