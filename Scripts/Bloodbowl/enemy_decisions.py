#!/usr/bin/env python3

import random

# D&D Blood Bowl Enemy Action Rolltable
actions = [
    "Charge at a random player!",
    "Defend their goal fiercely!",
    "Pass the ball randomly across the field!",
    "Attempt a dirty trick (mud throw, trip)!",
    "Tackle the closest player!",
    "Move toward the ball!",
    "Dance confusedly and lose their action!",
    "Throw the ball at a random target!"
]

# Roll and output
enemy_action = random.choice(actions)
print(f"Enemy Team Action: {enemy_action}")

