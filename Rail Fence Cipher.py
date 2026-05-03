def encrypt_rail_fence(text, rails):
    rail = [['\n' for i in range(len(text))] for j in range(rails)]

    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    result = ""
    for i in range(rails):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt_rail_fence(cipher, rails):
    rail = [['\n' for i in range(len(cipher))] for j in range(rails)]

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

        if direction_down:
            row += 1
        else:
            row -= 1

    # Fill marked positions with cipher text
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read zigzag to reconstruct message
    result = ""
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        if rail[row][col] != '\n':
            result += rail[row][col]
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result


# -------- Main Program --------

print("\n---- Rail Fence Cipher ----")
print("1. Encrypt Message")
print("2. Decrypt Ciphertext")

choice = int(input("Enter your choice (1 or 2): "))
text = input("Enter the message: ")
rails = int(input("Enter number of rails: "))

if choice == 1:
    encrypted = encrypt_rail_fence(text, rails)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = decrypt_rail_fence(text, rails)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")