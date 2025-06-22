import random

# Define the encounter table
encounter_table = {
    1: {
        "name": "The Watcher on the Road",
        "type": "Roleplay / Foreshadowing",
        "description": "A blind old man sits at a crossroads shrine, whispering Dhuron's true name in his sleep. "
                       "Waking him causes him to speak in tongues before vanishing into ash."
    },
    2: {
        "name": "Carrion Reclaimers",
        "type": "Combat / Mystery",
        "description": "Giant black crows peck at a shattered war banner bearing the Pendragon crest. "
                       "They become hostile if approached. One has a signet ring in its nest."
    },
    3: {
        "name": "Memory Leak",
        "type": "Psychic Hazard",
        "description": "As the party camps, each wakes in a different part of the forest—none remember setting camp. "
                       "Dhuron dreams of binding an oath in blood… and breaking it."
    },
    4: {
        "name": "The Root-Rot Grove",
        "type": "Puzzle / Exploration",
        "description": "Trees here grow in a perfect spiral, bark etched with old Pendragon war poems. "
                       "A sigil puzzle at the center suppresses the necklace's aura—if solved."
    },
    5: {
        "name": "Pendragon Remnant Patrol",
        "type": "Combat / Revelation",
        "description": "Ghostly soldiers rise from the fog, locked in a patrol loop. They attack unless Dhuron "
                       "speaks a command phrase—one he shouldn't know."
    },
    6: {
        "name": "The Silent Herald",
        "type": "Roleplay / Clue",
        "description": "A mute traveler passes them, dragging a coffin labeled “Here lies he who left us”. "
                       "Inside: a mirror that shows Dhuron in blackened armor, weeping blood."
    }
}

# Define the whispers table
whispers_table = {
    1: "A voice whispers a name from Dhuron’s past.",
    2: "The necklace glows faintly and feels heavier.",
    3: "A random PC sees a shadowy figure mimicking Dhuron’s movements.",
    4: "A memory returns to Dhuron—brief, painful, and wrong."
}

# Function to roll a travel encounter
def roll_travel_encounter():
    roll = random.randint(1, 6)
    whisper_roll = random.randint(1, 4)
    encounter = encounter_table[roll]
    whisper = whispers_table[whisper_roll]

    return {
        "Encounter Roll": roll,
        "Encounter Name": encounter["name"],
        "Encounter Type": encounter["type"],
        "Description": encounter["description"],
        "Whisper Effect": whisper
    }

# Roll and display the result
encounter_result = roll_travel_encounter()
encounter_result
