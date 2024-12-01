def create_playfair_square(phrase):
    key = phrase.replace('J', 'I').upper()
    key += 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = "".join(dict.fromkeys(key))  # Hapus huruf yang berulang
    grid = [[key[i * 5 + j] for j in range(5)] for i in range(5)]
    return grid

def find_location(grid, char):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j

def playfair_decrypt(ciphertext: str, key: str) -> str:
    playfair_square = create_playfair_square(key)
    message = ''
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        row1, col1 = find_location(playfair_square, digraph[0])
        row2, col2 = find_location(playfair_square, digraph[1])
        if row1 == row2:
            sub1 = playfair_square[row1][(col1 - 1) % 5]
            sub2 = playfair_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            sub1 = playfair_square[(row1 - 1) % 5][col1]
            sub2 = playfair_square[(row2 - 1) % 5][col2]
        else:
            sub1 = playfair_square[row1][col2]
            sub2 = playfair_square[row2][col1]
        message += sub1 + sub2
    i = 0
    while i < len(message) - 2:
        if message[i] == message[i+2] and message[i+1] == 'X':
            message = message[:i+1] + message[i+2:]
        i += 1
    if message[-1] == 'X':
        message = message[:-1]
    return message

if __name__ == "__main__":
    key = input("Masukkan kata kunci untuk dekripsi: ").strip()
    ciphertext = input("Masukkan pesan terenkripsi yang akan didekripsi: ").strip()
    decrypted_message = playfair_decrypt(ciphertext, key)
    print(f'Pesan terdekripsi: {decrypted_message}')
