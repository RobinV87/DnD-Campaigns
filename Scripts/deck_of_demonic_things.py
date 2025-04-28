import random

# Ghostroot Black Deck (52 cards)
cards = [
    # Minor (~20)
    ("Wormtongue", "Speech fails randomly (-1 CHA)", "Gain Message cantrip"),
    ("Rusted Coin", "Carries cursed coin attracting undead", "Gain random magic trinket"),
    ("Spider's Kiss", "Hands deform (-1 Sleight of Hand)", "Gain climbing speed 10ft"),
    ("Silent Mourner", "Voice cuts out randomly", "Disguise Self once per long rest"),
    ("Mark of Thirst", "Always thirsty, minor exhaustion", "+1 temp HP per long rest"),
    ("Cracked Mask", "Reflection flickers", "+1 to Deception"),
    ("Dagger Root", "Bleed 1 HP when attacking", "+1 damage once per turn"),
    ("Dust Skin", "Skin cracks (-1 Persuasion)", "Resistance to necrotic for 24 hrs"),
    ("Bleeding Star", "Nosebleeds at random", "Advantage on Survival checks"),
    ("Black Marrow", "Joints stiff (-1 Acrobatics)", "Gain Feather Fall once/day"),
    ("Ashen Veins", "Pale skin shows in light", "+1 Stealth in darkness"),
    ("Eclipsed Eye", "Vision dims (-5 passive Perception)", "+10ft Darkvision"),
    ("Bitter Ink", "Hands leave black stains", "Write hidden messages instantly"),
    ("Phantom Nail", "Phantom limb pains", "Advantage to resist grapple"),
    ("Crumbling Grip", "Weakens touch (-1 Athletics)", "Mage Hand cantrip"),
    ("Shard Breath", "Coughing blood intermittently", "1d4 necrotic breath attack 1/day"),
    ("Cold Halo", "Skin temperature drops", "Resistance to cold damage"),
    ("Splinter Mind", "Brief headaches (-1 Investigation)", "Advantage vs illusions"),
    ("Flickering Voice", "Sometimes speaks backwards", "+1 to Intimidation"),
    ("Haunted Steps", "Leaves faint black footprints", "Silent walking advantage 1/day"),

    # Moderate (~20)
    ("Crown of Bone", "Wears visible bone crown (-2 Initiative)", "Command undead once/day"),
    ("Grave Oath", "Must kill weekly or madness", "Advantage on Intimidation 7 days"),
    ("Dagger Pact", "Bleed when hurting others", "Magic dagger +1"),
    ("Hollow Eyes", "Eyes glow faintly (-2 Deception)", "Gain 30ft Darkvision extension"),
    ("Red Hunger", "Crave raw flesh daily", "Heal 1d6 HP per kill"),
    ("Festered Wound", "Wounds fester (-1 healing)", "Absorb 1d4 temp HP on kill"),
    ("Spectral Chain", "Arms chained in visions (-1 STR checks)", "Teleport 10ft once/day"),
    ("Black Thorn", "Pierced heart: no natural healing 1 day", "Deal extra piercing damage"),
    ("Rotten Halo", "Rotting smell (-2 Persuasion)", "Frighten humanoid once/day"),
    ("Howling Blood", "Blood screams audibly", "Gain Thunderwave once/day"),
    ("Shattered Bone", "Random minor fractures", "Resistance to bludgeoning damage"),
    ("Ash Walk", "Leaves trail of ash", "Ignore non-magical difficult terrain"),
    ("Wither Veins", "Blood vessels show black", "Advantage to resist necrotic spells"),
    ("Broken Sight", "Partial blindness in one eye", "Blindsight 5ft radius"),
    ("Death's Mark", "Marked by otherworldly forces", "Cast Bane once/day"),
    ("Carrion Tongue", "Taste of death in mouth", "Speak with Dead once/week"),
    ("Mourning Cloak", "Smells like a funeral", "Immunity to fear for 1 hour"),
    ("Ebon Shard", "Black crystal grows on hand (-1 STR)", "Cast Magic Missile once/day"),
    ("Bone Fissure", "Painful cracking sounds", "+2 to Insight"),
    ("Pit Whisper", "Hears whispers from Patron", "Advantage vs lies (Insight checks)"),

    # Major (~8)
    ("Lich Seed", "Turning into undead lord", "Gain minor lich traits early"),
    ("Black Throne", "Haunt gains control if loyalty falters", "Control haunted mini-kingdom"),
    ("Shattered Fate", "No natural 20s for a week", "Force one crit attack"),
    ("Void Chain", "Lose soul piece unless sacrifice", "Summon fiend once"),
    ("Plague's Favor", "Spreads disease passively", "Immunity to disease and poison"),
    ("Blood Eclipse", "World darkens for 1 minute", "Cast Darkness once/day"),
    ("Flesh Harvest", "Rise as revenant if killed", "+5 necrotic resistance bonus"),
    ("Necrotic Bloom", "Black flowers bloom from skin", "Regenerate minor wounds 1 min"),

    # Wild (~4)
    ("Chains of the Pit", "Patron physically manifests nearby", "Force boon or punishment of Patron's choice"),
    ("Grave Mirage", "Reality warps temporarily", "Massive spell free cast"),
    ("Death's Court", "Must stand trial by spirits", "Gain deathless resistance if passed"),
    ("Crimson Spiral", "Time loops briefly", "Reroll event with worse outcome")
]

def draw_card():
    card = random.choice(cards)
    print("\n===== Card Drawn =====")
    print(f"Card Name: {card[0]}")
    print(f"Punishment (Bound to Finos): {card[1]}")
    print(f"Reward (Keep or Give Away): {card[2]}")
    print("======================\n")

if __name__ == "__main__":
    draw_card()

