'''import time

seconds = int(input("Enter time in seconds: "))

for i in range(seconds , 0 , -1):
    print (f"Time remaining: {i} seconds")
    time.sleep(1)

print("Time's up!")
'''

import time
import sys
import threading
import os

def clear_console():
    """Clears the console screen for better UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate():
    """Displays a smooth loading animation while the timer is running."""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for char in chars:
        sys.stdout.write(f"\r{char} Counting down...")
        sys.stdout.flush()
        time.sleep(0.1)

def countdown_timer():
    """Runs an advanced countdown timer with improved user experience."""
    try:
        clear_console()
        seconds = int(input("Enter countdown time in seconds: "))
        if seconds <= 0:
            print("Please enter a positive number.")
            return
        
        for i in range(seconds, 0, -1):
            animation_thread = threading.Thread(target=animate)
            animation_thread.start()
            sys.stdout.write(f"\r⏳ Time remaining: {i} seconds ")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write("\r" + " " * 30 + "\r")  # Clear line
            animation_thread.join()
        
        clear_console()
        print("\n🚀 Time's up! 🎉")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    countdown_timer()