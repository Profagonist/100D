alphabet = ["a"," ","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def ceasar(original_text, shift_amount, encode_decode):
    cipher_text = ""

    for letter in original_text:
        if letter not in alphabet:
            cipher_text +=letter
        else:
            if encode_decode == "decode":
                shift_amount *= -1

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the {encode_decode}d result: {cipher_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(original_text=text, shift_amount=shift, encode_decode=direction)
    restart = input ("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if restart == "no":
        print("Goodbye")
        break
