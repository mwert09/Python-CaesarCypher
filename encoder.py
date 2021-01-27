import alphabet

def encode(text, shift):
    encoded_text = ""
    for letter in text:
        if letter.isspace():
            encoded_text += ' '
            continue
        if letter.isdigit():
            encoded_text += letter
            continue

        new_letter_index = (alphabet.alphabet.index(letter) + shift) % len(alphabet.alphabet)
        new_letter = alphabet.alphabet[new_letter_index]
        encoded_text += new_letter
    print(f"The encoded text is {encoded_text}")