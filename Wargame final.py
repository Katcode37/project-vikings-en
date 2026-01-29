import random
import time
from vikingsClasses import Viking, Saxon, War


# player
class Player:
    def __init__(self, coins=100):
        self.coins = coins


# setup war
def setup_war():
    soldier_names = [
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
    ]

    war = War()

    # number of soldiers
    while True:
        raw = input("Enter the number of soldiers to spawn for each army (1-20): ")
        try:
            number_of_soldiers = int(raw)
            if number_of_soldiers > 20:
                print("Let's keep it under 20. Odin has other events to attend to...")
            elif number_of_soldiers <= 0:
                print("Enter a positive integer (1-20).")
            else:
                break
        except ValueError:
            print("Enter a real number.")

    #Kate_randomize health
    while True:
        ans = input("Would you like to randomize health values? Yes/No > ").strip().lower()
        if ans in ("yes", "y"):
            random_health = True
            break
        elif ans in ("no", "n"):
            random_health = False
            break
        else:
            print("Please type Yes or No.")

    # spawn Vikings + Saxons (SAME count for both)
    for _ in range(number_of_soldiers):
        v_health = random.randint(20, 100) if random_health else 100
        s_health = random.randint(20, 100) if random_health else 100

        war.addViking(
            Viking(
                random.choice(soldier_names),
                v_health,
                random.randint(30, 80)
            )
        )

        war.addSaxon(
            Saxon(
                s_health,
                random.randint(30, 80)
            )
        )

    return war, number_of_soldiers


# run war
def run_war(war, number_of_soldiers):
    round_num = 1
    print("\nThe war begins!\n")

    viking_total_health = sum(v.health for v in war.vikingArmy)
    viking_total_strength = sum(v.strength for v in war.vikingArmy)

    saxons_total_health = sum(s.health for s in war.saxonArmy)
    saxon_total_strength = sum(s.strength for s in war.saxonArmy)

    print(f"Vikings' stats: total health: {viking_total_health}, total strength: {viking_total_strength}")
    print(f"Saxons' stats: total health: {saxons_total_health}, total strength: {saxon_total_strength}\n")
    time.sleep(1.5)

    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"--- Round {round_num} ---")

        if war.saxonArmy:
            print(war.vikingAttack())
            time.sleep(0.5)

        if war.vikingArmy and war.saxonArmy:
            print(war.saxonAttack())
            time.sleep(0.5)

        print(f"Vikings: {len(war.vikingArmy)} | Saxons: {len(war.saxonArmy)}\n")
        round_num += 1

    vikings_leftover_health = sum(v.health for v in war.vikingArmy)
    saxons_leftover_health = sum(s.health for s in war.saxonArmy)

    print("WAR OVER")
    status = war.showStatus()
    print(status)

    # IMPORTANT: use the original sizes, not number_of_soldiers for Vikings if you ever change counts
    killed_saxons = number_of_soldiers - len(war.saxonArmy)
    killed_vikings = number_of_soldiers - len(war.vikingArmy)

    print(f"Vikings have dealt total damage of {saxons_total_health - saxons_leftover_health} and killed {killed_saxons} saxons")
    print(f"Saxons have dealt total damage of {viking_total_health - vikings_leftover_health} and killed {killed_vikings} vikings")

    return status


# casino game
def casino_game():
    player = Player()
    print("WELCOME TO VIKING WAR CASINO")

    num_bets = 0

    while player.coins > 0:
        print(f"\nCoins: {player.coins}")
        print("Bet on:")
        print("1. Vikings (x2.0)")
        print("2. Saxons (x2.0)")
        print("3. Quit")

        choice = input("> ").strip()

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

        num_bets += 1

        # jackpot trigger after 5 bets
        if num_bets == 5:
            print("\nJACKPOT! You win the grand prize!")
            player.coins += 1_000_000
            break

        war, number_of_soldiers = setup_war()
        result = run_war(war, number_of_soldiers)

        winner = "vikings" if "Vikings have won" in result else "saxons"

        if (choice == "1" and winner == "vikings") or (choice == "2" and winner == "saxons"):
            multiplier = 2.0
            winnings = int(bet * multiplier)
            player.coins += winnings
            print(f"YOU WON {winnings} COINS!")
        else:
            player.coins -= bet
            print(f"YOU LOST {bet} COINS.")

    print("\nGame over.")
    print(f"Final coins: {player.coins}")


if __name__ == "__main__":
    casino_game()