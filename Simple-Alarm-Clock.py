'''import time
import winsound

alarm_time = int(input("Enter alarm time in seconds: "))
time.sleep(alarm_time)
winsound.Beep(1000,1000)
print("Wake up!")
'''

import time
import sys

try:
    if sys.platform.startswith("win"):
        import winsound  # Windows only
    else:
        from playsound import playsound  # type: ignore # Cross-platform alternative
except ImportError:
    print("Missing sound library. Install 'playsound' for non-Windows systems.")
    sys.exit(1)

def set_alarm():
    """Enhanced alarm with real-time countdown, validation, and cross-platform support."""
    while True:
        try:
            alarm_time = int(input("Enter alarm time in seconds: ").strip())
            if alarm_time <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f"Alarm set for {alarm_time} seconds. Counting down...")
    for remaining in range(alarm_time, 0, -1):
        sys.stdout.write(f"\rTime left: {remaining} seconds")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\nTime's up! Wake up!")
    
    if sys.platform.startswith("win"):
        winsound.Beep(1000, 1000)  # Windows beep sound
    else:
        playsound("/System/Library/Sounds/Sosumi.aiff")  # macOS default sound
    
    # Logging the alarm trigger
    with open("alarm_log.txt", "a") as log_file:
        log_file.write(f"Alarm triggered after {alarm_time} seconds.\n")

if __name__ == "__main__":
    set_alarm()
