# Monoalphabetic Cipher Program

# Fixed substitution mapping
plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"


# Encryption function
def encrypt(message):
    message = message.upper()
    cipher_text = ""

    for char in message:
        if char.isalpha():
            index = plain_alphabet.index(char)
            cipher_text += cipher_alphabet[index]
        else:
            cipher_text += char

    return cipher_text


# Decryption function
def decrypt(cipher_text):
    cipher_text = cipher_text.upper()
    plain_text = ""

    for char in cipher_text:
        if char.isalpha():
            index = cipher_alphabet.index(char)
            plain_text += plain_alphabet[index]
        else:
            plain_text += char

    return plain_text


# ---------------- MAIN PROGRAM ----------------

print("---- Monoalphabetic Cipher ----")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter your choice (1 or 2): "))

text = input("Enter the message: ")

if choice == 1:
    encrypted = encrypt(text)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = decrypt(text)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")