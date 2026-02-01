import random
import time
from vikingsClasses import Viking, Saxon, War
import winsound
import os


# sounds functions

base = os.path.dirname(__file__) # get the directory of the current script

def play_background_music():
    sound_path = os.path.join(base, "vikings_at_shore.wav") # construct the full path to the sound file
    winsound.PlaySound(
        sound_path,
        winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
    ) # background music


def play_battle_sound():
    sound_path = os.path.join(base, "something_approaches.wav") 
    winsound.PlaySound(
        sound_path,
        winsound.SND_FILENAME | winsound.SND_ASYNC
    ) # battle sound effect

def victory_sound():
    sound_path = os.path.join(base, "victory_sound.wav")
    winsound.PlaySound(
        sound_path,
        winsound.SND_FILENAME | winsound.SND_ASYNC
    ) # victory sound effect

def loss_sound():
    sound_path = os.path.join(base, "loss_sound.wav")
    winsound.PlaySound(
        sound_path,
        winsound.SND_FILENAME | winsound.SND_ASYNC
    ) # defeat sound effect

def jackpot_sound():
    sound_path = os.path.join(base, "jackpot.wav")
    winsound.PlaySound(
        sound_path,
        winsound.SND_FILENAME
    ) # jackpot sound effect



# player
class Player:
    def __init__(self, coins=100):
        self.coins = coins

# facts about vikings and saxons
FACTS = [
    "Vikings never actually wore horned helmets — that image was invented in the 1800s for opera costumes.",
    "Some Vikings were buried with cats — not for food, but as beloved companions.",
    "The word 'berserk' comes from Viking warriors who fought in trance-like fury.",
    "Viking longships were so light they could be carried over land between rivers.",
    "Vikings reached North America almost 500 years before Columbus.",
    "Not all Vikings were men — shieldmaidens existed, and at least one was confirmed by DNA.",
    "Viking children played board games very similar to chess.",
    "Many Vikings bathed weekly — which was considered extremely clean at the time.",
    "Anglo-Saxons believed words spoken before battle could shape fate itself.",
    "Some Saxon warriors carried small charms sewn into their clothes for protection.",
    "The Saxons feared Viking ships so much they called them 'dragons from the sea'.",
    "Old English sounded so different that modern English speakers wouldn’t understand a single sentence.",
    "Saxons believed certain days were cursed for battle — and would delay fighting because of it.",
    "The famous Bayeux Tapestry is over 70 meters long — longer than a football field.",
    "Some warriors believed dying with a weapon in hand affected their afterlife.",
    "Viking nicknames were brutal — names like 'Bone-Crusher' and 'Blood-Axe' were real.",
    "Viking laws allowed women to divorce their husbands — extremely rare for the time.",
    "Anglo-Saxon kings often ruled from wooden halls, not castles.",
    "Battle horns weren’t just noise — they signaled commands across the battlefield.",
    "Many warriors believed ravens flying overhead were signs from the gods."
]

# build fact deck
def build_fact_deck():
    """
    Creates a shuffled list of facts for ONE war.
    We will later pop() facts from it so they never repeat.
    """
    deck = FACTS[:]          
    random.shuffle(deck)     
    return deck

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
                f"Saxon_{len(war.saxonArmy) + 1}",   # Raya added random Saxon name
                s_health,
                random.randint(30, 80)
            )
        )

    return war, number_of_soldiers

# ASCII art
ascii_art = {
    "war_begins": r"""
 ⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀
⠀⠀⠹⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠏⠀⠀
⠀⠀⠀⠙⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⡉⠻⣷⣤⡀⠀⠀⢀⣴⣾⠟⢉⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡈⠻⣿⣦⣀⠻⠟⢁⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡈⠻⣿⣷⣄⠙⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⣀⠙⢿⣿⣦⡈⠻⣿⣷⣄⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀
⠀⠀⠀⠘⢿⣷⡄⠀⣠⣾⣿⠗⠀⠙⢿⣿⣦⡈⠻⣿⣷⣄⠀⢠⣾⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣾⣿⠟⢁⣴⣿⡷⠀⠙⢿⣿⣦⡈⠻⣿⣷⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣶⣿⡿⠋⠀⠀⠀⠀⠙⢿⣿⣶⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⠟⠉⠙⢿⣷⣄⡀⠀⠀⢀⣠⣾⡿⠋⠉⠻⣿⣆⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⠋⠀⠀⠀⠀⠀⠙⢿⡿⠂⠐⢿⡿⠋⠀⠀⠀⠀⠀⠙⣷⣦⡀⠀⠀
⠀⠸⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "jackpot": r"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣔⣶⣶⣶⣶⣿⣿⣿⡿⠿⢿⣿⣿⣿⡻⠛⠛⢯⣿⣿⣿⠛⠉⠻⣿⣿⣿⡻⠛⠛⢿⣿⣿⡿⡿⠿⢿⣿⣿⣿⣶⣶⣶⣶⣦⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣰⣶⣾⣿⣟⠟⠛⠻⣿⣿⣻⠏⠀⠀⢹⣟⣯⣯⠀⠀⠀⣿⣿⣽⡅⠀⠀⢸⣿⣯⣿⡀⠀⢀⣿⣽⣿⣇⠀⠀⢨⣿⣯⢿⠀⠀⠀⣿⣻⡽⡏⠀⠀⢹⣿⣿⣟⠟⠛⠻⣿⣿⣷⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠛⢻⣿⣿⣿⠀⠀⢀⣿⣿⣽⣧⣄⣠⣾⣟⣿⣽⣷⣶⣾⣿⣿⣏⣾⣷⣾⣯⣽⢿⣯⢿⡿⣿⢿⡿⣯⣿⣷⣾⣿⣟⣯⣿⣷⣶⣾⣟⣯⣿⢷⣄⣠⣼⣿⣻⣿⡀⠀⠀⣿⣿⣞⡹⠚⠓⢏⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⢀⣿⡿⣯⣿⣶⣿⡯⢿⡿⣞⣻⣛⡽⣫⡽⣭⢯⣝⣶⣱⢦⣏⣷⣚⣶⢳⣖⣶⣜⣶⢳⣜⣶⣲⣳⣞⣼⣷⡳⣞⣴⣒⣦⢣⡽⣭⣏⣯⣻⣿⣿⣿⣿⣿⣷⣿⣶⣿⣟⣷⢯⣇⠀⠀⢨⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣾⣿⣿⣿⣟⣿⣿⣿⣽⣷⣻⣷⣻⡾⠝⠓⠻⣯⣿⣞⣷⠟⠉⠉⠀⠀⠈⣹⡇⠀⠀⣿⡟⠀⠀⢠⡞⠀⠀⠉⠉⠙⠺⣿⣾⡿⠛⠋⠛⠛⢿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣻⢾⣯⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠛⠻⢯⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⠀⠀⠀⠀⢿⣿⣿⠀⠀⠀⣠⣶⣦⣄⣿⡅⠀⠀⣟⠀⠀⣰⣿⡇⠀⠀⣠⣤⠀⠀⣼⡏⠀⢀⢠⣄⡀⠀⢘⣿⠀⠀⠀⠉⠉⠙⠛⣿⣿⣿⣷⠟⠛⢯⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⠇⠀⣸⡆⠀⠘⣿⡟⠀⠀⢰⣿⣿⣿⣿⣿⡆⠀⠀⠏⢠⣶⣿⣿⡇⠀⠀⢿⡿⠀⠀⣿⠀⠀⣬⣿⣿⣷⠀⠈⣿⣷⣶⠀⠀⠀⣤⣄⣿⣿⣿⣧⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⡿⠀⠀⣻⣷⠀⠀⢿⡇⠀⠀⢸⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠹⣿⣿⡇⠀⠀⠀⠀⠀⢀⣽⠀⠀⣿⣿⣿⣿⠆⠀⠙⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⠿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠈⢿⣿⣿⡿⣿⡇⠀⠀⣆⠀⠀⢻⣿⣗⠀⠀⢰⣴⣶⣿⣿⡄⠀⠀⢿⣿⡿⠀⠀⢰⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⠾⠻⢽⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⡟⠀⢀⣰⣶⣶⣧⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⣿⣆⠀⠀⠹⡇⠀⠀⣸⣿⣿⣿⣿⣷⡀⡀⠀⠉⠁⠀⢠⣾⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣏⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣶⣶⣿⣿⣿⣿⣧⣤⣤⣶⣿⣧⣤⣭⣿⣿⣿⣿⣶⣦⣴⣿⣿⣶⣤⣤⣤⣾⣾⣷⣶⣤⣿⣿⣶⣶⣬⣼⣶⣮⣽⣿⣿⣿⣿⣿⣿⣾⣤⣤⣴⣾⣿⣿⣿⣿⣦⣶⣶⣿⣿⣿⣿⣿⣿⢷⣶⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⡿⢶⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣛⣻⣟⣛⣛⣛⣛⣻⣟⣛⣛⣛⣛⣻⣟⣛⣛⣛⣛⣛⣛⣛⣛⣟⣛⣛⣻⣛⣛⣻⣛⣟⣻⣛⣛⣛⣻⣛⣻⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣻⣛⣻⣟⣻⣻⣿⣻⣿⣛⣟⣛⡛⣞⣛⢻⣙⣿⣧⣤⣤⣤⡀⠀⠀⣼⣿⣿⣿⣷⣼⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠋⠉⠙⣿⣿⡟⠁⠀⠙⣿⣿⣿⠋⠀⠈⢻⣿⣿⠏⠁⠈⢻⣿⣿⡞⠁⠀⠹⣟⡿⡟⠉⠀⠙⣿⡿⣿⠉⠀⠉⣿⢯⣻⠊⠀⠈⢫⣝⣣⠏⠁⠈⢹⣻⣟⡟⠁⠈⠹⣿⣿⡟⠁⠀⠙⣿⡽⣲⠊⠀⠈⢲⢯⣷⡟⠉⠉⢻⣿⠀⠀⠹⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣷⣀⠀⣠⣿⣾⣷⣄⣀⣴⣿⣿⣟⣦⣀⣠⣾⣿⣿⣧⣀⣀⣼⣿⣟⢣⣄⣀⣔⢿⣟⣷⣄⣀⣴⣿⣻⣟⣄⣀⣠⠿⣯⡽⣦⣀⣠⡾⣜⢶⣣⣀⣀⣼⣳⣯⣷⣀⣀⣼⣿⡿⣷⣄⣀⣴⣿⣻⣍⢢⣀⣠⢚⣿⡿⣆⡀⣀⣼⣿⠀⠀⠀⠈⣻⠻⠛⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣻⣷⣿⡿⣿⡿⣿⢿⡿⣿⢿⡿⣿⢯⡿⢿⢿⡿⢿⠿⢾⠿⡿⢿⠿⡾⠽⠿⡽⠿⢯⠿⡽⢾⠿⡿⢿⠿⠿⠽⠷⠯⠷⠿⠽⠾⠧⠿⠽⠷⢯⠿⠿⠿⡿⠿⠿⡽⠿⢿⠿⢿⠾⠷⠽⢯⠾⣽⢷⣞⣻⣽⣿⣿⣿⣿⠀⠀⠀⢠⠿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣯⡷⠿⢯⣟⣿⣷⣿⣳⣿⣽⣳⣟⣾⣳⢿⣼⣳⡽⣯⣞⡽⣎⡿⣭⢷⣫⡽⣮⡽⣹⢮⡵⣛⢮⡳⣝⣎⢷⣙⢮⡝⣎⡳⣍⢶⡹⣜⡧⣛⣬⢣⡞⣱⢎⡞⣭⢳⣜⣹⣎⣵⣯⣾⣾⣷⣿⣿⣿⣯⣿⣭⣿⣿⡿⣽⠟⠿⣳⣿⠀⠀⠀⡿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣻⣭⣿⣭⣿⣭⣽⣭⣽⣭⣽⣭⣿⣭⣯⣽⣯⣽⣭⣽⣯⣽⣭⣯⣭⣽⣬⣯⣭⣯⣭⣿⣭⣿⣭⣿⣼⣿⣽⣭⣽⣯⣽⣯⣽⣭⣭⣭⣭⣭⣽⣭⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⡁⠀⠀⢸⣿⠀⠀⣼⠻⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣷⣶⣾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣻⣶⣶⣿⣿⣀⣀⡏⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⢷⣛⣾⣳⣿⡟⣼⢸⡇⠀⠀⠀⠀⠀⠀
""",
    "war_casino": r"""
▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖     ▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖    ▗▖ ▗▖ ▗▄▖ ▗▄▄▖      ▗▄▄▖ ▗▄▖  ▗▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▖ 
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌      █  ▐▌ ▐▌▐▌       ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌    ▐▌   ▐▌ ▐▌▐▌     █  ▐▛▚▖▐▌▐▌ ▐▌
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌      █  ▐▛▀▜▌▐▛▀▀▘    ▐▌ ▐▌▐▛▀▜▌▐▛▀▚▖    ▐▌   ▐▛▀▜▌ ▝▀▚▖  █  ▐▌ ▝▜▌▐▌ ▐▌
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘      █  ▐▌ ▐▌▐▙▄▄▖    ▐▙█▟▌▐▌ ▐▌▐▌ ▐▌    ▝▚▄▄▖▐▌ ▐▌▗▄▄▞▘▗▄█▄▖▐▌  ▐▌▝▚▄▞▘                                                                                                                                                                                                                       
    """,

    "win_battle": r"""
⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀
⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠃⠀⠀⠀⠀⠀⠀
""",
    "game_over": r"""
   _____          __  __ ______          ______      ________ _____     
  / ____|   /\   |  \/  |  ____|        / __ \ \    / /  ____|  __ \    
 | |  __   /  \  | \  / | |__          | |  | \ \  / /| |__  | |__) |   
 | | |_ | / /\ \ | |\/| |  __|         | |  | |\ \/ / |  __| |  _  /    
 | |__| |/ ____ \| |  | | |____        | |__| | \  /  | |____| | \ \    
  \_____/_/    \_\_|  |_|______|        \____/   \/   |______|_|  \_\   
                                                                                                                                                                                                            
""",
"you_won": r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
"""
}

    

# run war
def run_war(war, number_of_soldiers):
    play_battle_sound()
    round_num = 1
    print("\nThe war begins!\n")
    print(ascii_art["war_begins"])
    time.sleep(2)
    
    fact_deck = build_fact_deck()
    FACT_CHANCE_PER_ROUND = 1 / 3   # about once every 3 rounds
    MIN_FACTS_PER_WAR = 2
    facts_shown = 0

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
            time.sleep(1.5)

        if war.vikingArmy and war.saxonArmy:
            print(war.saxonAttack())
            time.sleep(1.5)

        print(f"Vikings: {len(war.vikingArmy)} | Saxons: {len(war.saxonArmy)}\n")
        round_num += 1
    # random chance to show a fact
        if random.random() < FACT_CHANCE_PER_ROUND and fact_deck:
            fact = fact_deck.pop()   # REMOVE fact so it can't repeat
            print(f"\n📜 FUN FACT: {fact}\n")
            facts_shown += 1
            time.sleep(0.5)

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
    while facts_shown < MIN_FACTS_PER_WAR and fact_deck:
        fact = fact_deck.pop()
        print(f"\n📜 FUN FACT: {fact}\n")
        facts_shown += 1
        time.sleep(0.5)
    
    if (choice == "1" and "Vikings" in status) or (choice == "2" and "Saxons" in status):
        victory_sound()
    else:
        loss_sound()
    time.sleep(8)  # wait for victory or loss  sound to finish
    play_background_music()

    play_background_music()
    return status


# casino game
def casino_game():
    
    player = Player()
    # remember starting coins so we only show the trophy if the player finished ahead
    starting_coins = player.coins
    # print("\nWELCOME TO VIKING WAR CASINO\n")
    print(ascii_art["war_casino"])
    num_bets = 0

    while player.coins > 0:
        print(f"\nCoins: {player.coins}")
        print("Bet on:")
        print("1. Vikings (x2.0)")
        print("2. Saxons (x2.0)")
        print("3. Quit")

        global choice
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
            print(ascii_art["jackpot"])
            player.coins += 1_000_000
            # If jackpot is hit, end the casino immediately and don't show
            # the regular end-game trophy or 'game over' flow.
            print(f"\nFinal coins: {player.coins}")
            jackpot_sound()
            return

        war, number_of_soldiers = setup_war()
        result = run_war(war, number_of_soldiers)

        winner = "vikings" if "Vikings have won" in result else "saxons"

        if (choice == "1" and winner == "vikings") or (choice == "2" and winner == "saxons"):
            multiplier = 2.0
            winnings = int(bet * multiplier)
            player.coins += winnings
            print(f"YOU WON {winnings} COINS!")
            print(ascii_art["you_won"])
        else:
            player.coins -= bet
            print(f"YOU LOST {bet} COINS.")

    # Game finished — show trophy only if the player ended with more coins
    #print("\nGame over.")
    print(ascii_art["game_over"])
    if player.coins > starting_coins:
        print("\nCongratulations — you finished with more coins than you started!")
        print(ascii_art["win_battle"])  # trophy
    print(f"Final coins: {player.coins}")


if __name__ == "__main__":
    play_background_music()
    casino_game()

