# Function to generate repeated key
def generate_key(message, key):
    key = key.upper()
    key_sequence = ""
    key_index = 0

    for char in message:
        if char.isalpha():
            key_sequence += key[key_index % len(key)]
            key_index += 1
        else:
            key_sequence += char

    return key_sequence


# Encryption function
def vigenere_encrypt(message, key):
    message = message.upper()
    key_sequence = generate_key(message, key)
    cipher_text = ""

    for m, k in zip(message, key_sequence):
        if m.isalpha():
            value = (ord(m) - 65 + ord(k) - 65) % 26
            cipher_text += chr(value + 65)
        else:
            cipher_text += m

    return cipher_text


# Decryption function
def vigenere_decrypt(cipher_text, key):
    key_sequence = generate_key(cipher_text, key)
    plain_text = ""

    for c, k in zip(cipher_text, key_sequence):
        if c.isalpha():
            value = (ord(c) - 65 - (ord(k) - 65)) % 26
            plain_text += chr(value + 65)
        else:
            plain_text += c

    return plain_text


# ---------------- MAIN PROGRAM ----------------

print("\n---- Vigenere Cipher ----")
print("1. Encrypt using Vigenere Cipher")
print("2. Decrypt Ciphertext using Vigenere Cipher")

choice = int(input("Enter your choice (1 or 2): "))
message = input("Enter the message: ")
key = input("Enter the key: ")

if choice == 1:
    encrypted = vigenere_encrypt(message, key)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = vigenere_decrypt(message, key)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")
