import random
party_member = [""] # put here your own party members

# Roll the main dice for the main decision what will happen
def roll_dice(sides=12):
    return random.randint(1, sides)

# Roll for the d4 results
def roll_d4():
    return random.randint(1,4)

# Roll for the d10 results
def roll_d10():
    return random.randint(1,10)

# Get the main dice roll result
roll = roll_dice()

# Day and night have different chances on the enemies and even a bit of different enemies. Chooses which one.
time_of_day = input("Is it Day or Night?> ")


if time_of_day == "Day":
    if roll <= 2:
       outcome_d4 =  roll_d4() + 2
       print(f"You encounter {outcome_d4} stirges")

    elif roll <= 4:
        print("You encounter an Ogre")

    elif roll <= 6:
        outcome_goblin_band = roll_d4() + roll_d4()
        outcome_sp = roll_d10()
        outcome_cp = roll_d10()
        print(f"You encounter a goblin warband consisting of {outcome_goblin_band} and a warchief.")
        print(f"They carry {outcome_sp} Silver Pieces and {outcome_cp} Coppier Pieces.")
        print("When captured and threatenend they know the exact location of Cragmaw Castle")

    elif roll <= 8:
        outcome_hobgoblin_squad = roll_d4()
        random_party_member = random.choice(party_member)
        print(f"You encounter a Hobgoblin squad of {outcome_hobgoblin_squad} Hobgoblins")
        print(f"One Hobgoblin carries a crude sketch of {random_party_member} and 20 Gold Pieces")

    elif roll <= 10:
        print("You encounter two Bugbear Scouts")

    elif roll == 11:
        outcome_wolves = roll_d4() + 2
        print(f"You encounter {outcome_wolves} wolves")

    elif roll == 12:
        print("You encounter an owlbear")
        
elif time_of_day == "Night":
    if roll <= 3:
        outcome_d4 =  roll_d4() + 2
        print(f"You encounter {outcome_d4} stirges")
    
    elif roll == 4:
        outcome_ghouls = roll_d4 + 1
        print(f"You encounter {outcome_ghouls} Ghouls!")
         
    elif roll == 5:
        outcome_goblin_band = roll_d4() + roll_d4()
        outcome_sp = roll_d10()
        outcome_cp = roll_d10()
        print(f"You encounter a goblin warband consisting of {outcome_goblin_band} and a warchief.")
        print(f"They carry {outcome_sp} Silver Pieces and {outcome_cp} Coppier Pieces.")
        print("When captured and threatenend they know the exact location of Cragmaw Castle")
        
    elif roll == 6:
        outcome_hobgoblin_squad = roll_d4()
        random_party_member = random.choice(party_member)
        print(f"You encounter a Hobgoblin squad of {outcome_hobgoblin_squad} Hobgoblins")
        print(f"One Hobgoblin carries a crude sketch of {random_party_member} and 20 Gold Pieces")
        
    elif roll <= 8:
        print("You encounter two Bugbear Scouts")

    elif roll <= 10:
        outcome_wolves = roll_d4() + 2
        print(f"You encounter {outcome_wolves} wolves")
        
    elif roll <= 12:
        print("You encounter an owlbear")
    
else: "Something went wrong!?"
