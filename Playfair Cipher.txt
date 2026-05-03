# Function to create 5x5 Playfair matrix
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


# Function to prepare message
def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                result += 'X'
                i += 1
            else:
                result += text[i + 1]
                i += 2
        else:
            result += 'X'
            i += 1

    return result


# Find position of character in matrix
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


# Encrypt function
def playfair_encrypt(message, key):
    matrix = generate_matrix(key)
    message = prepare_text(message)
    cipher_text = ""

    for i in range(0, len(message), 2):
        r1, c1 = find_position(matrix, message[i])
        r2, c2 = find_position(matrix, message[i + 1])

        if r1 == r2:  # Same row
            cipher_text += matrix[r1][(c1 + 1) % 5]
            cipher_text += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:  # Same column
            cipher_text += matrix[(r1 + 1) % 5][c1]
            cipher_text += matrix[(r2 + 1) % 5][c2]

        else:  # Rectangle rule
            cipher_text += matrix[r1][c2]
            cipher_text += matrix[r2][c1]

    return cipher_text


# Decrypt function
def playfair_decrypt(cipher_text, key):
    matrix = generate_matrix(key)
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        r1, c1 = find_position(matrix, cipher_text[i])
        r2, c2 = find_position(matrix, cipher_text[i + 1])

        if r1 == r2:  # Same row
            plain_text += matrix[r1][(c1 - 1) % 5]
            plain_text += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:  # Same column
            plain_text += matrix[(r1 - 1) % 5][c1]
            plain_text += matrix[(r2 - 1) % 5][c2]

        else:  # Rectangle rule
            plain_text += matrix[r1][c2]
            plain_text += matrix[r2][c1]

    return plain_text


# ---------------- MAIN PROGRAM ----------------

print("\n---- Playfair Cipher ----")
print("1. Encrypt using Playfair Cipher")
print("2. Decrypt using Playfair Cipher")

choice = int(input("Enter your choice (1 or 2): "))
message = input("Enter the message: ")
key = input("Enter the key: ")

if choice == 1:
    encrypted = playfair_encrypt(message, key)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = playfair_decrypt(message, key)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")
