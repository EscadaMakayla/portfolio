import re

def check_password_strength(password):
    # Initialize strength score
    strength_score = 0
    
    # Check length
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for uppercase and lowercase letters
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength_score += 1
    else:
        print("Password should contain both uppercase and lowercase letters.")
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength_score += 1
    else:
        print("Password should contain at least one digit.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        print("Password should contain at least one special character.")
    
    # Evaluate strength
    if strength_score == 4:
        return "Strong"
    elif strength_score == 3:
        return "Moderate"
    else:
        return "Weak"

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter your password: ")
    strength = check_password_strength(user_password)
    print(f"Your password strength is: {strength}")
