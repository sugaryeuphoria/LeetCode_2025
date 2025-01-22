def caesar_cipher(text, value):
    result = ""
    for char in text:
        result += chr((ord(char) - 97 + value) % 26 + 97)
    return result

text = "hello"
value = 3
encr_text = caesar_cipher(text, value)
print("Encrypted text:", encr_text)
