# With a correction already implemented: dont forget to initialize an instance of Class "War"

from vikingsClasses import Soldier, Viking, Saxon, War
import random

soldier_names = ["Gabriel","Alex","Jovana","Susobhan","Paria","Andrii","Rizki","Zoé","Bright","Theo","Nacho","Jonathan","Chinonso"]
great_war = War()

def pick_viking_contingent():
    while True:
        try:
            num_vikings = int(
                input(f"Please enter the number of soldiers in the Viking army from 1 to {len(soldier_names)}: ")
            )

            if 1 <= num_vikings <= len(soldier_names):
                return num_vikings

            print(f"Enter a number between 1 and {len(soldier_names)}.")

        except ValueError:
            print("Invalid input. Enter a whole number.")
    

def pick_saxon_contingent():
    while True:
        try:
            num_saxons = int(
                input(f"Please enter the number of soldiers in the Saxon army: ")
            )

            if num_saxons:
                return num_saxons

            print(f"Enter a positive number.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def play_game():

    num_vikings = pick_viking_contingent()

    selected_names = random.sample(soldier_names, num_vikings)

    for name in selected_names:
        great_war.addViking(
            Viking(name, 100, random.randint(0, 100))
        )

    vikingArmy_list = sorted([viking.name for viking in great_war.vikingArmy])
    vikingArmy_print = ", ".join(vikingArmy_list[:-1]) + " and " + vikingArmy_list[-1]

    print(f"The Viking soldiers recruited for the Great War against the were {vikingArmy_print}.")

    num_saxons = pick_saxon_contingent()
    for i in range(0,num_saxons):
        great_war.addSaxon(Saxon(100,random.randint(0,100)))
    
    round = 1
    while len(great_war.vikingArmy) != 0 and len(great_war.saxonArmy) != 0:
        print(f"\n>>>>>>>>>>>>>>> Round {round} <<<<<<<<<<<<<<<")
        print(f"Viking army: {len(great_war.vikingArmy)} warrior(s) \nSaxon army: {len(great_war.saxonArmy)} warrior(s)")
        print("---------------------------------------")
        print("The Vikings go for the attack!")
        print(great_war.vikingAttack())
        print("---------------------------------------")

        if len(great_war.saxonArmy) == 0:
            print(great_war.showStatus())
            break

        print("The Saxons go for the counterattack!")
        print(great_war.saxonAttack())
        print("\n"+great_war.showStatus())
        round += 1

play_game()