import encoder
import decoder
import art

direction = ""
text = ""
shift_number = 0
user_wants_to_continue = True

def WantsToContinue():
    continueInput = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if continueInput == "no":
        return False
    if continueInput == "yes":
        return True

def GetUserInput():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print("Invalid input. Exiting...")

    text = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    if direction == "encode":
        encoder.encode(text, shift_number)
        
    if direction == "decode":
        decoder.decode(text, shift_number)

print(art.logo)

while(user_wants_to_continue):
     GetUserInput()
     user_wants_to_continue = WantsToContinue()

