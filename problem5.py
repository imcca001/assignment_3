def caesar_encrypt(key, message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    for char in message.lower():
        try:
            rotation = (alpha.index(char) + key) % 26
            new_char = alpha[rotation]
        except ValueError:
            new_char = char
        encrypted_message += new_char
    return encrypted_message

def caesar_decrypt(key, message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ''
    for char in message.lower():
        try:
            rotation = (alpha.index(char) - key) % 26
            new_char = alpha[rotation]
        except ValueError:
            new_char = char
        decrypted_message += new_char
    return decrypted_message

#Lock = 11, "believe you can and you are half way there"
greetings = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
lock = 11
print caesar_decrypt(lock, greetings)
