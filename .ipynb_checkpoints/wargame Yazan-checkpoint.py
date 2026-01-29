# yazan casino addition
import random
import time
from vikingsClasses import Viking, Saxon, War


#  player 
class Player:
    def __init__(self, coins=100):
        self.coins = coins


# setup war 
def setup_war():
    names = [
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
    war = War()

    

    while True:
        number_of_soldiers = input('Enter the number of soldiers to spawn for each army: ')
        try:
            number_of_soldiers = int(number_of_soldiers)
            if number_of_soldiers > 20:
                print("Let's keep it under 20. Odin has othre events to attend to...")
            elif number_of_soldiers < 0:
                print("Odin doubts you are sane enough to paricipate...Enter a postive intager")
            else:
                break
        except:
            print("Cut the retarded mode and enter a real number")

    for i in range(number_of_soldiers):
        war.addViking(
            Viking(
                random.choice(names),
                100,
                random.randint(30, 80)
            )
        )

    for i in range(number_of_soldiers):
        war.addSaxon(
            Saxon(
                100,
                random.randint(30, 80)
            )
        )

    return war, number_of_soldiers


# run war 
def run_war(war, number_of_soldiers):
    round_num = 1
    print("\n The war begins!\n")
    
    # caclulating totals using generator + sum 
    # same as for loop but shorter & faster here
    viking_total_health = sum(viking.health for viking in war.vikingArmy)
    viking_total_strength = sum(viking.strength for viking in war.vikingArmy)
    
    saxons_total_health = sum(saxon.health for saxon in war.saxonArmy)
    saxon_total_strength = sum(saxon.strength for saxon in war.saxonArmy)

    print(f"Vikings' stats: total health: {viking_total_health}, total strength: {viking_total_strength}")
    print(f"Saxons' stats: total health: {saxons_total_health}, total strength: {saxon_total_strength}")
    print('\n')
    time.sleep(4)
        
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"--- Round {round_num} ---")

        if war.saxonArmy: # empty list = False & non-empty list = True
            print(war.vikingAttack())
            time.sleep(1.5)

        if war.vikingArmy and war.saxonArmy:
            print(war.saxonAttack())
            time.sleep(1.5)

        print(
            f"Vikings: {len(war.vikingArmy)} | Saxons: {len(war.saxonArmy)}\n"
        )

        round_num += 1
    
    vikings_leftover_health = sum(viking.health for viking in war.vikingArmy)
    saxons_leftover_health = sum(saxon.health for saxon in war.saxonArmy)

    print(" WAR OVER ")
    print(war.showStatus())
    print(f'Vikings have dealt total damage of {saxons_total_health - saxons_leftover_health} and killed {len(war.saxonArmy)} saxons')
    print(f'Saxons have dealt total damage of {viking_total_health - vikings_leftover_health} and killed {len(war.vikingArmy)} vikings')
    return war.showStatus()
    


# casino game
def casino_game():
    player = Player()
    print(" WELCOME TO VIKING WAR CASINO ")

    while player.coins > 0:
        print(f"\n Coins: {player.coins}")
        print("Bet on:")
        print("1. Vikings (x1.5)")
        print("2. Saxons (x2.0)")
        print("3. Quit")

        choice = input("> ")

        if choice == "3":
            break

        if choice not in ("1", "2"):
            print("Invalid choice.")
            continue

        try:
            bet = int(input("How many coins do you bet? > "))
        except ValueError:
            print("Invalid bet.")
            continue

        if bet <= 0 or bet > player.coins:
            print("Invalid amount.")
            continue

        war = setup_war()
        result = run_war(war, number_of_soldiers)

        if "Vikings have won" in result:
            winner = "vikings"
        else:
            winner = "saxons"

        if (choice == "1" and winner == "vikings") or (choice == "2" and winner == "saxons"):
            multiplier = 1.5 if winner == "vikings" else 2.0
            winnings = int(bet * multiplier)
            player.coins += winnings
            print(f" YOU WON {winnings} COINS!")
        else:
            player.coins -= bet
            print(f" YOU LOST {bet} COINS.")

    print("\n Game over.")
    print(f"Final coins: {player.coins}")


# start game
if __name__ == "__main__":
    casino_game()