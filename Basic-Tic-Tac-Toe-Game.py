'''borad =[" " for _ in range(9)]

def print_board():
    for i in range(0 , 9 , 3):
        print(f"{borad[i]} | {borad[i+1]} | {borad[i+2]}")
        if i < 6:
            print("---|---|---")
            
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(borad[i] == player for i in condition):
            return True
        return False
    
current_player = "X"
while True: 
    print_board()
    move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
    
    if borad[move] == " ":
        borad[move] = current_player
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} Wins! ")
            break
        if " " not in borad:
            print_board()
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid move! Try again.")
            
    '''
    
    
import random
from typing import List, Optional
from enum import Enum

class GameState(Enum):
    ONGOING = "ongoing"
    WIN = "win"
    TIE = "tie"

class TicTacToe:
    def __init__(self):
        self.board: List[str] = [" " for _ in range(9)]
        self.players = {"X": "Player 1", "O": "Player 2/AI"}
        self.scores = {"X": 0, "O": 0}
        self.current_player = "X"
        self.ai_mode = False
    
    def print_board(self):
        """Display the game board with numbers for empty spots"""
        print("\nCurrent Board:")
        for i in range(0, 9, 3):
            row = [f"{self.board[i+j] if self.board[i+j] != ' ' else (i+j+1)}" 
                  for j in range(3)]
            print(" | ".join(row))
            if i < 6:
                print("-----------")
        print()

    def check_game_state(self) -> GameState:
        """Check if there's a winner or tie"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for condition in win_conditions:
            if all(self.board[i] == self.current_player for i in condition):
                return GameState.WIN
        return GameState.TIE if " " not in self.board else GameState.ONGOING
    
    def get_ai_move(self) -> int:
        """Simple AI: Try to win, block, or random move"""
        # Check for winning move
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                if self.check_game_state() == GameState.WIN:
                    self.board[i] = " "
                    return i
                self.board[i] = " "
        
        # Block player's winning move
        temp_player = self.current_player
        self.current_player = "X"
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "X"
                if self.check_game_state() == GameState.WIN:
                    self.board[i] = " "
                    self.current_player = temp_player
                    return i
                self.board[i] = " "
        self.current_player = temp_player
        
        # Random available move
        available = [i for i in range(9) if self.board[i] == " "]
        return random.choice(available)
    
    def make_move(self, position: int) -> bool:
        """Attempt to make a move, return success status"""
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

def main():
    game = TicTacToe()
    
    print("Welcome to Enhanced Tic-Tac-Toe!")
    game.ai_mode = input("Play against AI? (y/n): ").lower() == 'y'
    
    while True:
        game.board = [" " for _ in range(9)]
        game.current_player = "X"
        
        while True:
            game.print_board()
            
            if game.ai_mode and game.current_player == "O":
                print("AI is thinking...")
                move = game.get_ai_move()
                print(f"AI chose position {move + 1}")
            else:
                try:
                    move = int(input(f"{game.players[game.current_player]}, enter position (1-9): ")) - 1
                except ValueError:
                    print("Please enter a number between 1 and 9!")
                    continue
            
            if game.make_move(move):
                state = game.check_game_state()
                
                if state == GameState.WIN:
                    game.print_board()
                    print(f"{game.players[game.current_player]} wins!")
                    game.scores[game.current_player] += 1
                    break
                elif state == GameState.TIE:
                    game.print_board()
                    print("It's a tie!")
                    break
                game.current_player = "O" if game.current_player == "X" else "X"
            else:
                print("Invalid move! Position already taken or out of range.")
        
        # Show scores
        print(f"\nScores - Player 1 (X): {game.scores['X']} | Player 2/AI (O): {game.scores['O']}")
        
        # Play again?
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()