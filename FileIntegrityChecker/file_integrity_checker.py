import hashlib

def calculate_file_hash(file_path, algorithm="sha256"):
    """Calculates the hash of a given file using the specified algorithm."""
    try:
        # Initialize the hash object
        hash_func = hashlib.new(algorithm)
        with open(file_path, "rb") as f:
            # Read the file in chunks to handle large files
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return "Error: File not found."
    except ValueError:
        return "Error: Invalid hashing algorithm."

def main():
    print("Welcome to the File Integrity Checker!")
    print("Supported algorithms: md5, sha1, sha256, sha512")
    
    # Get user input
    file_path = input("Enter the file path: ")
    algorithm = input("Enter the hashing algorithm (default: sha256): ") or "sha256"
    
    # Calculate the file hash
    file_hash = calculate_file_hash(file_path, algorithm)
    
    if "Error" not in file_hash:
        print(f"\nHash ({algorithm}) for the file:\n{file_hash}")
        
        # Optional: Compare with known hash
        known_hash = input("Enter a known hash to compare (or press Enter to skip): ")
        if known_hash:
            if file_hash == known_hash:
                print("The file is verified and matches the known hash.")
            else:
                print("The file does NOT match the known hash.")
    else:
        print(file_hash)

if __name__ == "__main__":
    main()

