import alphabet

def decode(text, shift):
    decoded_text = ""
    for letter in text:
        if letter.isspace():
            decoded_text += ' '
            continue
        if letter.isdigit():
            decoded_text += letter
            continue

        new_letter_index = (alphabet.alphabet.index(letter) - shift) % len(alphabet.alphabet)
        new_letter = alphabet.alphabet[new_letter_index]
        decoded_text += new_letter
    print(decoded_text)