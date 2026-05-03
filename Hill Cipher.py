import math

# Function to convert letters to numbers (A=0, B=1, ..., Z=25)
def char_to_num(c):
    return ord(c) - ord('A')


# Function to convert numbers to letters
def num_to_char(n):
    return chr(n + ord('A'))


# Encrypt function
def hill_encrypt(message, key):
    message = message.replace(" ", "").upper()

    # Padding if message length is odd
    if len(message) % 2 != 0:
        message += 'X'

    cipher_text = ""

    for i in range(0, len(message), 2):
        vector = [
            char_to_num(message[i]),
            char_to_num(message[i + 1])
        ]

        c1 = (key[0][0] * vector[0] + key[0][1] * vector[1]) % 26
        c2 = (key[1][0] * vector[0] + key[1][1] * vector[1]) % 26

        cipher_text += num_to_char(c1) + num_to_char(c2)

    return cipher_text


# Function to calculate modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


# Decrypt function
def hill_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()

    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        return "Key matrix is not invertible!"

    # Inverse key matrix
    inv_key = [
        [( key[1][1] * det_inv) % 26, (-key[0][1] * det_inv) % 26],
        [(-key[1][0] * det_inv) % 26, ( key[0][0] * det_inv) % 26]
    ]

    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        vector = [
            char_to_num(cipher_text[i]),
            char_to_num(cipher_text[i + 1])
        ]

        p1 = (inv_key[0][0] * vector[0] + inv_key[0][1] * vector[1]) % 26
        p2 = (inv_key[1][0] * vector[0] + inv_key[1][1] * vector[1]) % 26

        plain_text += num_to_char(p1) + num_to_char(p2)

    return plain_text


# ---------------- MAIN PROGRAM ----------------

print("\n---- Hill Cipher ----")
print("1. Encrypt Message using Hill Cipher")
print("2. Decrypt Ciphertext using Hill Cipher")

choice = int(input("Enter your choice (1 or 2): "))

# Example invertible key matrix
key = [[3, 3],
    [2, 5]]

if choice == 1:
    message = input("Enter the message: ")
    encrypted = hill_encrypt(message, key)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    cipher = input("Enter the ciphertext: ")
    decrypted = hill_decrypt(cipher, key)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")
