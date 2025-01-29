import math

# Common password dictionary
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "12345678",
    "12345", "1234567", "111111", "123123", "abc123"
]

# Function to calculate password entropy
def calculate_entropy(password):
    character_space = 0
    if any(c.islower() for c in password):
        character_space += 26
    if any(c.isupper() for c in password):
        character_space += 26
    if any(c.isdigit() for c in password):
        character_space += 10
    if any(c in "!@#$%^&*()-_+=[]{}|;:,.<>?/`~" for c in password):
        character_space += 32
    entropy = len(password) * math.log2(character_space) if character_space > 0 else 0
    return entropy

# Function to estimate crack time
def calculate_crack_time(password):
    guesses_per_second = 1e6  # Assume 1 million guesses per second
    entropy = calculate_entropy(password)
    possible_combinations = 2 ** entropy
    time_to_crack = possible_combinations / guesses_per_second
    return time_to_crack

# Function to evaluate password strength
def evaluate_password(password):
    if password in COMMON_PASSWORDS:
        return "Weak", "Password is in the list of common passwords."

    entropy = calculate_entropy(password)
    crack_time = calculate_crack_time(password)

    if entropy < 28:
        return "Weak", f"Entropy: {entropy:.2f}. Very easy to guess."
    elif entropy < 36:
        return "Medium", f"Entropy: {entropy:.2f}. Could be guessed within hours."
    else:
        return "Strong", f"Entropy: {entropy:.2f}. Difficult to guess."

# Main function
def main():
    print("Welcome to the Password Guessability Model!")
    password = input("Enter a password to evaluate: ")
    strength, feedback = evaluate_password(password)
    crack_time = calculate_crack_time(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Feedback: {feedback}")
    print(f"Estimated Crack Time: {crack_time:.2e} seconds\n")

if __name__ == "__main__":
    main()
