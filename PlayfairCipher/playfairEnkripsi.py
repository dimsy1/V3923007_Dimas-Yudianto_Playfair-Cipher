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

def playfair_encrypt(message: str, key: str) -> str:
    playfair_square = create_playfair_square(key)
    ciphertext = ''
    message = "".join(filter(str.isalpha, message)).upper()
    message = message.replace('J', 'I')
    i = 0
    while i < len(message) - 1:
        if message[i] == message[i+1]:
            message = message[:i+1] + 'X' + message[i+1:]
        i += 2
    if len(message) % 2 == 1:
        message += 'X'
    for i in range(0, len(message), 2):
        digraph = message[i:i+2]
        row1, col1 = find_location(playfair_square, digraph[0])
        row2, col2 = find_location(playfair_square, digraph[1])
        if row1 == row2:
            sub1 = playfair_square[row1][(col1 + 1) % 5]
            sub2 = playfair_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            sub1 = playfair_square[(row1 + 1) % 5][col1]
            sub2 = playfair_square[(row2 + 1) % 5][col2]
        else:
            sub1 = playfair_square[row1][col2]
            sub2 = playfair_square[row2][col1]
        ciphertext += sub1 + sub2
    return ciphertext

if __name__ == "__main__":
    key = input("Masukkan kata kunci untuk enkripsi: ").strip()
    message = input("Masukkan pesan yang akan dienkripsi: ").strip()
    encrypted_message = playfair_encrypt(message, key)
    print(f'Pesan terenkripsi: {encrypted_message}')
