from microbit import *
import radio

ALPH_MORSE = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    " ": " "
}

MORSE_ALPH = {value: key for key, value in ALPH_MORSE.items()}

# Caesar Cipher Encryption function
def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char in ALPH_MORSE:
            encrypted_text += ALPH_MORSE[char] + ' '
    return encrypted_text

# Caesar Cipher Decryption function
def decrypt_caesar(encrypted_text, shift):
    words = encrypted_text.strip().split(' ')
    decrypted_message = ''
    for word in words:
        if word in MORSE_ALPH:
            decrypted_message += MORSE_ALPH[word]
        else:
            decrypted_message += ' '
    return decrypted_message

display.show("!")

radio.on()
radio.config(channel=1)
radio.RATE_1MBIT

while True:
    message = "I AM AHMED".lower()

    if button_a.was_pressed():
        # Encrypt the message using Caesar Cipher (with a fixed shift of 3 for example)
        shift = 3
        encrypted_morse_code = encrypt_caesar(message, shift)
        display_text = "Sending: " + encrypted_morse_code
        display.scroll(display_text)

        radio.send(encrypted_morse_code)

    received = radio.receive()
    if received:
        # Decrypt the received message using Caesar Cipher with the same shift value
        shift = 3
        decrypted_message = decrypt_caesar(received, shift)
        message = "Received: " + decrypted_message
        display.scroll(message)

    sleep(1000)
    display.clear()
