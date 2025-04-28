import random


def roll_dice(dice):
    """Rolls a dice given in the format XdY (e.g., 2d6)"""
    num, sides = map(int, dice.lower().split('d'))
    return sum(random.randint(1, sides) for _ in range(num))


def weighted_roll(weighted_options):
    """Selects an option based on weighted probabilities."""
    choices, weights = zip(*weighted_options.items())
    return random.choices(choices, weights=weights, k=1)[0]


# Treasure Tables
CURRENCY_WEIGHTS = {
    "Copper Pieces": 80,
    "Silver Pieces": 50,
    "Electrum Pieces": 10,
    "Gold Pieces": 30,
    "Platinum Pieces": 1,
}

CURRENCY = {}
for coin, weight in CURRENCY_WEIGHTS.items():
    if random.randint(1, 100) <= weight:  # Roll percentage chance
        CURRENCY[coin] = (
            roll_dice("5d10") if coin == "Copper Pieces"
            else roll_dice("3d8") if coin == "Silver Pieces"
            else roll_dice("1d6") if coin == "Electrum Pieces"
            else roll_dice("1d4") if coin == "Gold Pieces"
            else roll_dice("1d2")
        )

GEMS = ["Small Ruby", "Emerald Shard", "Sapphire Chip", "Amethyst", "Topaz"]

USEFUL_MAGIC_ITEMS = [
    "Potion of Healing", "+1 Weapon", "Cloak of Protection", "Bag of Holding",
    "Ring of Jumping", "Wand of Magic Missiles", "Boots of Elvenkind",
    "Bracers of Defense", "Amulet of the Devout", "Gloves of Thievery", "Ring of Water Walking",
    "Quiver of Ehlonna", "Goggles of Night", "Periapt of Wound Closure", "Driftglobe",
    "Broom of Flying", "Slippers of Spider Climbing", "Hat of Disguise", "Cloak of the Manta Ray",
    "Winged Boots", "Lantern of Revealing", "Helm of Comprehending Languages", "Heward's Handy Haversack"
]

USELESS_MAGIC_ITEMS = [
    "Cursed Spoon (always tastes like dirt)", "Unbreakable Toothpick", "Ring of Slightly Cold Fingers",
    "Bag of Endless Feathers", "Wand of Mild Static Shock", "Hat of Minor Inconveniences",
    "Boots of Squeaky Steps", "Gloves of Slightly Itchy Fabric", "Candle of Dim Light",
    "Socks of Perpetual Dampness", "Comb of Unruly Hair", "Glasses of Useless X-ray Vision",
    "Belt of Slightly Tight Fit", "Earrings of Constant Whistling", "Coin that Always Lands on its Side",
    "Pen that Writes Only Backwards", "Scroll of Mildly Interesting Facts", "Mirror that Reflects 5 Seconds Late",
    "Fork that Bends When Used", "Cup That Slowly Leaks", "Tunic of Minor Itchiness",
    "Hat That Shrinks Slightly When Worn", "Gloves That Smell Like Onions", "Ring That Makes Your Shadow Wave at You",
    "Book That Changes Its Title Randomly", "Wand That Emits a Puff of Glitter", "Cloak That Dramatically Billows on Its Own",
    "Broom That Sweeps But Not Where You Want", "Candle That Smells Like Burnt Popcorn", "Necklace That Glows Dimly in Daylight",
    "Boots That Leave No Tracks, Except in Mud", "Coin That Hums Softly at Night", "Stone That Warms Up When Hugged",
    "Feather That Writes in an Unknown Language", "Belt That Snaps Open Randomly", "Ring That Vibrates When Near Cheese",
    "Scarf That Tangles Itself", "Spoon That Stirs on Its Own but Only Counterclockwise", "Chair That Wobbles More Than Expected",
    "Whistle That Summons Mice, But They Ignore You", "Hat That Repels Butterflies", "Dagger That Looks Sharp but is Dull",
    "Bag That Always Weighs Slightly More Than It Should", "Earrings That Whisper Your Name but Get It Wrong",
    "Shoes That Make a Squeaky Noise on Stone", "Quill That Writes in Unreadable Cursive", "Rock That Slowly Changes Colors",
    "Cup That Always Tips Over When Placed Down", "Wand That Sparks But Does Nothing Else", "Map That Moves Landmarks Slightly",
    "Pocket Watch That Runs Backwards", "Mirror That Reflects an Older Version of You", "Ink That Disappears After an Hour",
    "Statue That Whispers When No One is Around", "Feather Duster That Attracts More Dust"
]

COMMON_ITEMS = [
    "Rope", "Candle", "Flint and Steel", "Backpack", "Waterskin", "Iron Pot", "Fishing Hook", "Hammer", "Chalk", "Empty Bottle",
    "Wooden Bowl", "Spoon", "Fork", "Clay Mug", "Lantern", "Torch", "Small Knife", "Piece of Cloth", "Leather Strap", "Metal Chain",
    "Sewing Needle", "Thread Spool", "Carved Wooden Figurine", "Small Bell", "Dice Set", "Playing Cards", "Old Key", "Feather Quill", "Ink Bottle",
    "Scroll Case", "Simple Lock", "Tin Whistle", "Wooden Comb", "Shaving Razor", "Hand Mirror", "Wooden Plate", "Straw Hat", "Woolen Blanket"
]


def generate_treasure():
    """Generates a random treasure pile for a level 5 party."""
    treasure = {}

    # Currency
    treasure["Currency"] = {coin: amount for coin, amount in CURRENCY.items() if amount > 0}

    # Gems (1d6, only if 6 is rolled)
    if roll_dice("1d6") == 6:
        treasure["Gems"] = random.sample(GEMS, 1)

    # Useful Magic Items (1d6, only if 6 is rolled)
    if roll_dice("1d6") == 6:
        treasure["Useful Magic Items"] = random.sample(USEFUL_MAGIC_ITEMS, 1)
    
    # Useless Magic Items (1d6, only if 1 is rolled)
    if roll_dice("1d6") == 1:
        treasure["Useless Magic Items"] = random.sample(USELESS_MAGIC_ITEMS, 1)

    # Common Items (at least 3, rolling 1d4+2)
    num_common_items = roll_dice("1d4") + 2
    treasure["Common Items"] = random.sample(COMMON_ITEMS, min(num_common_items, len(COMMON_ITEMS)))

    return treasure


# Run the generator
treasure = generate_treasure()
for key, value in treasure.items():
    print(f"{key}: {value}")
