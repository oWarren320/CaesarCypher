def encrypt(text, shift):
    result = ""
    
    # Traverse through the given text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters are added without change
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    while True:
        print("Caesar Cipher Tool")
        print("------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted Text: {encrypted_text}\n")
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted Text: {decrypted_text}\n")
        elif choice == '3':
            print("Exiting Caesar Cipher Tool.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
