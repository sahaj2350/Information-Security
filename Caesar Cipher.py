def encrypt(text, shift):
    result = ""

    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # Non-alphabetic characters remain unchanged
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            result += char

    return result


# Main Program
print("\n---- Caesar Cipher ----")
print("1. Encrypt using Caesar Cipher")
print("2. Decrypt using Caesar Cipher")

choice = int(input("Enter your choice (1 or 2): "))
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if choice == 1:
    encrypted_text = encrypt(message, shift)
    print("Encrypted Text:", encrypted_text)

elif choice == 2:
    decrypted_text = decrypt(message, shift)
    print("Decrypted Text:", decrypted_text)

else:
    print("Invalid choice!")
