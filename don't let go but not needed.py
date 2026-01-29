
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        great_war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for i in range(0,5):
    if i:
        great_war.addSaxon(Saxon(100,random.randint(0,100)))
    
round = 1
while len(great_war.saxonArmy) > 0 and len(great_war.vikingArmy) > 0:
    great_war.vikingAttack()
    if len(great_war.saxonArmy) == 0:
        print(great_war.showStatus())
        break
    great_war.saxonAttack()
    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    round += 1


# casino game
def casino_game():
    player = Player()
    print(" WELCOME TO VIKING WAR CASINO ")

    num_bets = 0
    jackpot_triggered = False

    while player.coins > 0:
        num_bets += 1
        print(f"\n Coins: {player.coins}")
        print("Bet on:")
        print("1. Vikings (x2.0)")
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

        #yazan: Jackpot trigger after 5 bets
        if num_bets == 5:
            print("\n JACKPOT! You win the grand prize! ")
            jackpot_triggered = True
            player.coins += 1000000  # optional jackpot amount
            break  # end the game immediately

        war = setup_war()
        result = run_war(war)

        if "Vikings have won" in result:
            winner = "vikings"
        else:
            winner = "saxons"

        if (choice == "1" and winner == "vikings") or (choice == "2" and winner == "saxons"):
            multiplier = 2.0 
            winnings = int(bet * multiplier)
            player.coins += winnings
            print(f" YOU WON {winnings} COINS!")
        else:
            player.coins -= bet
            print(f" YOU LOST {bet} COINS.")

    print("\n Game over.")
    print(f"Final coins: {player.coins}")


# start game

casino_game()
Collapse




