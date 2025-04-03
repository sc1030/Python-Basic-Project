'''text = input("Enter text: ")
shift = int(input("Enter shift value: "))
encrypted = ""

for char in text:
    if char.isalpha():
        shifted = ord(char) + shift
        if char.islower():
            if shifted > ord('z'):
                shifted -= 26
        elif char.isupper():
            if shifted > ord('Z'):
                shifted -= 26
        encrypted += chr(shifted)
    else:
        encrypted += char
    
print("Encrypted: " , encrypted)
'''

from typing import Tuple
import string

class CaesarCipher:
    def __init__(self):
        self.alphabet_lower = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase
    
    def validate_shift(self, shift: str) -> int:
        """Validate and convert shift value to integer"""
        try:
            shift_val = int(shift)
            return shift_val % 26  # Normalize shift to 0-25 range
        except ValueError:
            raise ValueError("Shift must be an integer")
    
    def process_text(self, text: str, shift: int, decrypt: bool = False) -> str:
        """Encrypt or decrypt text using Caesar cipher"""
        if decrypt:
            shift = -shift  # Reverse shift for decryption
            
        result = ""
        for char in text:
            if char in self.alphabet_lower:
                base = ord('a')
                shifted = (ord(char) - base + shift) % 26 + base
                result += chr(shifted)
            elif char in self.alphabet_upper:
                base = ord('A')
                shifted = (ord(char) - base + shift) % 26 + base
                result += chr(shifted)
            else:
                result += char  # Preserve non-alphabetic characters
        return result
    
    def analyze_frequency(self, text: str) -> dict:
        """Basic frequency analysis of encrypted text"""
        freq = {}
        for char in text.lower():
            if char in self.alphabet_lower:
                freq[char] = freq.get(char, 0) + 1
        return freq

def get_user_input() -> Tuple[str, int, bool]:
    """Get and validate user input"""
    while True:
        try:
            text = input("Enter text: ").strip()
            if not text:
                print("Text cannot be empty!")
                continue
                
            shift = CaesarCipher().validate_shift(input("Enter shift value: "))
            
            mode = input("Encrypt (e) or Decrypt (d)? ").lower()
            if mode not in ['e', 'd']:
                raise ValueError("Please choose 'e' for encrypt or 'd' for decrypt")
                
            return text, shift, (mode == 'd')
        except ValueError as e:
            print(f"Error: {str(e)}")

def main():
    cipher = CaesarCipher()
    
    print("Welcome to Enhanced Caesar Cipher!")
    print("----------------------------------")
    
    while True:
        try:
            # Get user input
            text, shift, decrypt = get_user_input()
            
            # Process text
            result = cipher.process_text(text, shift, decrypt)
            action = "Decrypted" if decrypt else "Encrypted"
            
            # Display results
            print(f"\nOriginal text: {text}")
            print(f"Shift value: {shift}")
            print(f"{action} text: {result}")
            
            # Show frequency analysis for encrypted text
            if not decrypt:
                freq = cipher.analyze_frequency(result)
                print("\nLetter frequency in encrypted text:")
                for char, count in sorted(freq.items()):
                    print(f"{char}: {count}")
            
            # Ask to continue
            again = input("\nTry again? (y/n): ").lower()
            if again != 'y':
                print("Thanks for using Caesar Cipher!")
                break
            print("\n" + "-" * 40)
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue

if __name__ == "__main__":
    main()