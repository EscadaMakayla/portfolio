def caesar_cipher(text, shift, mode="encrypt"):
    """Encrypts or decrypts text using a Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift if mode == "encrypt" else -shift
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new character
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result

def main():
    print("Welcome to the Simple Encryption Tool!")
    print("Encrypt or decrypt text using a Caesar Cipher.")
    
    # Get user input
    text = input("Enter the text: ")
    shift = int(input("Enter the shift/key (e.g., 3): "))
    mode = input("Do you want to encrypt or decrypt? (default: encrypt): ").lower() or "encrypt"
    
    # Perform the encryption or decryption
    result = caesar_cipher(text, shift, mode)
    
    print(f"\nThe {mode}ed text is: {result}")

if __name__ == "__main__":
    main()
