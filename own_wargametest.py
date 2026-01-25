from vikingsClasses import Soldier, Viking, Saxon, War
import random

viking_names = [
    "Ragnar", "Bjorn", "Ivar", "Ubbe", "Halfdan",
    "Harald", "Leif", "Erik", "Sigurd", "Hakon",
    "Floki", "Torsten", "Sven", "Olaf", "Knut",
    "Einar", "Gunnar", "Arne", "Sten", "Ulf",
    "Asbjorn", "Hjalmar", "Trygve", "Vidar", "Skarde",
    "Rollo", "Hrothgar", "Balder", "Tyr", "Odin",
    "Thor", "Freyr", "Heimdall", "Skoll", "Fenrir",
    "Yngvar", "Rurik", "Ingvar", "Sigrid", "Astrid",
    "Gudrun", "Freya", "Helga", "Yrsa", "Kara",
    "Thora", "Ingrid", "Solveig", "Alfhild", "Brynhild"
] # List of 50 Viking names



while True: # Ask user for number of soldiers to spawn
    try:
        soldiers_count = int(input('Enter the number of soldiers to spawn for each army: '))
        soldier_names = random.sample(viking_names, soldiers_count) # Select unique random names
        break
    except:
        print('Odin will not tollarate data type confusion. Enter an intager or pray for yoyr life!') # Error handling for non-integer input


new_war = War()

for soldier in soldier_names:

    new_war.addViking(Viking(soldier, 100, random.randint(1, 100))) # Add a Viking with random strength & name
    new_war.addSaxon(Saxon(100, random.randint(1, 100))) # Add a Saxon with random strength
  

vikings_total_health = 0
vikings_total_strength = 0 

print("Viking's army composition")
for viking in new_war.vikingArmy:
    print(f'{viking.name} has {viking.health} health and {viking.strength} strength')
    vikings_total_health += viking.health
    vikings_total_strength += viking.strength

print(f"Vikings' army totals: health = {vikings_total_health}, strength = {vikings_total_strength}")
print('\n')


saxons_total_health = 0
saxons_total_strength = 0

print("Saxon's army composition")
for i, saxon in enumerate(new_war.saxonArmy):
    print(f'Nameless saxon # {i + 1} has {saxon.health} health and {saxon.strength} strength')
    saxons_total_health += saxon.health
    saxons_total_strength += saxon.strength

print(f"Saxon's army totals: health = {saxons_total_health}, strength = {saxons_total_strength}")
print('\n')

round = 1

while True:
    print(f'Round {round}')
    
    if len(new_war.vikingArmy) > 0:
        new_war.vikingAttack()
    else:
        print(new_war.showStatus())
        break

    if len(new_war.saxonArmy) > 0:
        new_war.saxonAttack()
    else:
        print(new_war.showStatus())
        break

    print(f'Viking Army has {len(new_war.vikingArmy)} warriors left')
    print(f'Saxon Army has {len(new_war.saxonArmy)} warriors left')

    round += 1

    


















    
