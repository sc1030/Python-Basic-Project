'''import random 
import string

length = int(input("Enter Password Length: "))
chars = string.ascii_letters + string.digits + "!@#$%^&*"

password = "".join(random.choice(chars) for _ in range(length))
print(f"Your Password: {password}")
'''

import random
import string
import secrets  # For cryptographically strong random selection

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    # Define character sets
    upper = string.ascii_uppercase if use_upper else ''
    lower = string.ascii_lowercase if use_lower else ''
    digits = string.digits if use_digits else ''
    special = "!@#$%^&*()_+-=" if use_special else ''
    
    # Ensure at least one character set is selected
    if not (use_upper or use_lower or use_digits or use_special):
        raise ValueError("At least one character set must be selected")
    
    # Combine selected character sets
    chars = upper + lower + digits + special
    
    # Ensure minimum length and requirements
    if length < 8:
        length = 8  # Enforce minimum length
        print("Minimum password length set to 8 characters")
    
    # Generate password with at least one character from each selected set
    password = []
    if use_upper:
        password.append(secrets.choice(upper))
    if use_lower:
        password.append(secrets.choice(lower))
    if use_digits:
        password.append(secrets.choice(digits))
    if use_special:
        password.append(secrets.choice(special))
    
    # Fill remaining length with random characters
    remaining_length = length - len(password)
    password.extend(secrets.choice(chars) for _ in range(remaining_length))
    
    # Shuffle the password
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main():
    try:
        # Get user input
        length = int(input("Enter password length (minimum 8): "))
        
        # Get character set preferences
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate and display password
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Your secure password: {password}")
        
        # Password strength indicator
        strength = "Strong" if len(password) >= 12 else "Moderate" if len(password) >= 10 else "Basic"
        print(f"Password strength: {strength}")
        
    except ValueError as e:
        if str(e) == "At least one character set must be selected":
            print(e)
        else:
            print("Please enter a valid number for password length")

if __name__ == "__main__":
    main()