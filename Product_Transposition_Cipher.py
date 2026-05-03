import math

# ---------------- RAIL FENCE ----------------

def rail_fence_encrypt(text, rails):
    rail = [['\n' for _ in range(len(text))] for _ in range(rails)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        row += 1 if direction_down else -1

    result = ""
    for i in range(rails):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def rail_fence_decrypt(cipher, rails):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    direction_down = None
    row, col = 0, 0

    # Mark zigzag pattern
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        row += 1 if direction_down else -1

    # Fill matrix
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read zigzag
    result = ""
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        result += rail[row][col]
        col += 1

        row += 1 if direction_down else -1

    return result


# ---------------- COLUMNAR (FIXED) ----------------

def get_key_order(key):
    # Handles duplicate letters correctly
    return sorted(range(len(key)), key=lambda k: (key[k], k))


def columnar_encrypt(text, key):
    col = len(key)
    row = math.ceil(len(text) / col)

    matrix = [['X' for _ in range(col)] for _ in range(row)]

    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    order = get_key_order(key)

    result = ""
    for col_index in order:
        for i in range(row):
            result += matrix[i][col_index]

    return result


def columnar_decrypt(cipher, key):
    col = len(key)
    row = math.ceil(len(cipher) / col)

    matrix = [['' for _ in range(col)] for _ in range(row)]

    order = get_key_order(key)

    index = 0
    for col_index in order:
        for i in range(row):
            matrix[i][col_index] = cipher[index]
            index += 1

    result = ""
    for i in range(row):
        for j in range(col):
            result += matrix[i][j]

    return result.rstrip('X')


# ---------------- PRODUCT CIPHER ----------------

def product_encrypt(message, rails, key):
    step1 = rail_fence_encrypt(message, rails)
    step2 = columnar_encrypt(step1, key)
    return step2


def product_decrypt(cipher, rails, key):
    step1 = columnar_decrypt(cipher, key)
    step2 = rail_fence_decrypt(step1, rails)
    return step2


# ---------------- MAIN ----------------

print("---- Product Cipher (Transposition) ----")
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter your choice (1 or 2): "))
text = input("Enter the message: ").replace(" ", "").upper()
rails = int(input("Enter number of rails: "))
key = input("Enter columnar key: ").upper()

if choice == 1:
    encrypted = product_encrypt(text, rails, key)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = product_decrypt(text, rails, key)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")