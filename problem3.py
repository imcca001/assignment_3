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

greetings = 'Hello Friend'
lock = 9

print caesar_decrypt(lock, caesar_encrypt(lock, greetings))
