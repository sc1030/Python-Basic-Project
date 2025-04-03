'''import random 

choices = ["rock ", "paper" , "scissors"]
computer =random.choice(choices)
player = input("Choose  rock , paper , or scissors: ").lower()

print(f"Computer chose: {computer}" )
if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
    (player == "scissors" and computer == "paper") or \
    (player == "paper" and computer == "rock"):
    print("Player wins!")
else:
    print("Player loses!")
    '''
    
import random
from typing import Optional
from enum import Enum

class Move(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

class GameResult(Enum):
    WIN = "You win!"
    LOSS = "You lose!"
    TIE = "It's a tie!"

class RockPaperScissors:
    def __init__(self):
        self.valid_moves = [move.value for move in Move]
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 0
    
    def get_player_move(self) -> Optional[str]:
        """Get and validate player's move"""
        attempts = 3
        while attempts > 0:
            move = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower().strip()
            if move == 'quit':
                return None
            if move in self.valid_moves:
                return move
            attempts -= 1
            print(f"Invalid move! Please choose rock, paper, or scissors. {attempts} attempts remaining.")
        print("Too many invalid attempts!")
        return None
    
    def get_computer_move(self) -> str:
        """Generate computer's move"""
        return random.choice(self.valid_moves)
    
    def determine_winner(self, player: str, computer: str) -> GameResult:
        """Determine the game result"""
        if player == computer:
            return GameResult.TIE
        
        winning_combinations = {
            Move.ROCK.value: Move.SCISSORS.value,
            Move.PAPER.value: Move.ROCK.value,
            Move.SCISSORS.value: Move.PAPER.value
        }
        
        if winning_combinations[player] == computer:
            return GameResult.WIN
        return GameResult.LOSS
    
    def play_round(self) -> bool:
        """Play a single round and return if game should continue"""
        print(f"\nRound {self.rounds + 1}")
        print("-" * 20)
        
        player_move = self.get_player_move()
        if player_move is None:
            return False
            
        computer_move = self.get_computer_move()
        
        print(f"\nYou chose: {player_move}")
        print(f"Computer chose: {computer_move}")
        
        result = self.determine_winner(player_move, computer_move)
        print(result.value)
        
        # Update scores
        if result == GameResult.WIN:
            self.player_score += 1
        elif result == GameResult.LOSS:
            self.computer_score += 1
            
        self.rounds += 1
        return True

def main():
    game = RockPaperScissors()
    
    print("Welcome to Rock Paper Scissors!")
    print("Beat the computer if you can!")
    
    while True:
        if not game.play_round():
            break
            
        # Show current score
        print(f"\nScore - You: {game.player_score} | Computer: {game.computer_score}")
        
    # Show final results
    print("\nGame Over!")
    print(f"Final Score:")
    print(f"You: {game.player_score}")
    print(f"Computer: {game.computer_score}")
    print(f"Total Rounds: {game.rounds}")
    
    if game.player_score > game.computer_score:
        print("Congratulations! You won the match!")
    elif game.player_score < game.computer_score:
        print("Better luck next time! Computer wins!")
    else:
        print("It's a tie match!")

if __name__ == "__main__":
    main()