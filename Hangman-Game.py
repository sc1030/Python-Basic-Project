'''import random

words = ["Python", "hangman" , "programming" , "computer"]
word = random.choice(words)
guesses = ""
attempts = 6

while attempts > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nyou win! ")
        break
    
    guess = input("\nGuess a letter: ").lower()
    guesses += guess
    
    if guess not in word:
        attempts -= 1
        print(f"Worng! {attempts} attempts left. ")
else:
    print(f"\nYou lost! The word was {word}. ")
    '''
    
import random
import string

def hangman():
    """Ultimate Hangman Game with input validation, dynamic visuals, and improved logic."""
    words = ["python", "hangman", "programming", "computer", "developer", "algorithm", "software"]
    word = random.choice(words)
    guesses = set()
    attempts = 6
    
    print("\nWelcome to Hangman! Try to guess the word.")
    
    def display_word():
        return " ".join([char if char in guesses else "_" for char in word])
    
    while attempts > 0:
        print("\nWord: ", display_word())
        
        if "_" not in display_word():
            print("\nCongratulations! You guessed the word! 🎉")
            break
        
        guess = input("\nGuess a letter: ").lower().strip()
        
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guesses:
            print("You've already guessed that letter! Try again.")
            continue
        
        guesses.add(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
        else:
            print("Good guess!")
    else:
        print(f"You lose! The word was: {word} 😢")
    
if __name__ == "__main__":
    hangman()
