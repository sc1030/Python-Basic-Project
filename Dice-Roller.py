'''import random

dice  = random.randint(1 , 6)
print(f"you rolled a {dice}! ")
'''

import random
import time

def roll_dice():
    """Simulates rolling a dice with an animation."""
    print("Rolling the dice... 🎲")
    time.sleep(1)
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}! 🎉")

if __name__ == "__main__":
    while True:
        roll_dice()
        play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! 👋")
            break


    
    