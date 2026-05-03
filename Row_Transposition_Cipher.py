import math

# Get column order (handles duplicate letters correctly)
def get_key_order(key):
    return sorted(range(len(key)), key=lambda k: (key[k], k))


# Encryption
def row_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    col = len(key)
    row = math.ceil(len(text) / col)

    # Fill matrix row-wise
    matrix = [['X' for _ in range(col)] for _ in range(row)]
    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    # Read columns in sorted key order
    order = get_key_order(key.upper())

    cipher = ""
    for col_index in order:
        for i in range(row):
            cipher += matrix[i][col_index]

    return cipher


# Decryption
def row_transposition_decrypt(cipher, key):
    col = len(key)
    row = math.ceil(len(cipher) / col)

    matrix = [['' for _ in range(col)] for _ in range(row)]
    order = get_key_order(key.upper())

    # Fill column-wise based on key order
    index = 0
    for col_index in order:
        for i in range(row):
            if index < len(cipher):
                matrix[i][col_index] = cipher[index]
                index += 1

    # Read row-wise
    plain = ""
    for i in range(row):
        for j in range(col):
            plain += matrix[i][j]

    return plain.rstrip('X')


# ---------------- MAIN ----------------

print("---- Row Transposition Cipher ----")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter your choice (1 or 2): "))
text = input("Enter the message: ")
key = input("Enter the key: ")

if choice == 1:
    encrypted = row_transposition_encrypt(text, key)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = row_transposition_decrypt(text, key)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")