import random

# Define the memory fragments
memory_table = {
    1: {
        "title": "A blood-soaked oath",
        "type": "Guilt / Betrayal",
        "description": "Dhuron kneels before a dying man, swearing vengeance—but the man calls him 'traitor' as he dies."
    },
    2: {
        "title": "Swords clash under a red moon",
        "type": "War / Identity",
        "description": "A battlefield littered with Pendragon banners burning. Dhuron is shouting—but not in his current voice."
    },
    3: {
        "title": "A child’s hand in his",
        "type": "Loss / Duty",
        "description": "He’s fleeing the Keep’s collapse, holding a young noble's hand. He lets go to fight. He never finds the child again."
    },
    4: {
        "title": "The Mirror Pact",
        "type": "Arcane / Curse Origin",
        "description": "Dhuron signs a deal with a robed figure whose face is… his own."
    },
    5: {
        "title": "A knight kneeling before him",
        "type": "Leadership / Consequence",
        "description": "“For Pendragon. For the Blood.” Then impaled from behind. Dhuron may have watched—or given the order."
    },
    6: {
        "title": "A cracked crown",
        "type": "Power / Temptation",
        "description": "He’s holding it, but it burns his hands. In the mirror behind him stands the BBEG—wearing the crown with ease."
    },
    7: {
        "title": "A song in the dark",
        "type": "Humanity / Hope",
        "description": "Someone sings the Pendragon lullaby. He sees his younger self dancing with a woman he cannot name."
    },
    8: {
        "title": "A sealed room",
        "type": "The Truth",
        "description": "Screaming, chains, and chanting. The necklace is placed on a pedestal. Dhuron says: 'Lock it. Bury me with it.'"
    }
}

# Corruption tracker function
def corruption_effect():
    roll = random.randint(1, 4)
    if roll <= 2:
        return "Dhuron gains insight (advantage on next Wisdom/save)."
    else:
        return "The spirit gains influence (disadvantage on Charisma saves, whispers intensify)."

# Roll function for a memory
def roll_memory():
    roll = random.randint(1, 8)
    memory = memory_table[roll]
    corruption = corruption_effect()
    return {
        "Memory Roll": roll,
        "Title": memory["title"],
        "Type": memory["type"],
        "Description": memory["description"],
        "Corruption Effect": corruption
    }

# Execute and return the memory roll
memory_result = roll_memory()
memory_result
