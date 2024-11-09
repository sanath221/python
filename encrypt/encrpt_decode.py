alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
again = True

while again == True:
    direction = input(" type encode to encrypt, type decode to decypt:\n")
    text = input("type your message :").lower()
    shift=int(input("tyupe the shift number :\n"))
    shift %= 26
    def encrypt(plain_test,shift_number,direction_number):
        encrypted_word = ""
        if direction == "decode":
            shift_number *= -1
        for letter in plain_test:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_positon = position + shift_number
                new_letter = alphabet[new_positon]
                encrypted_word += new_letter
            else:
                encrypted_word += letter
        print(encrypted_word)

    encrypt(plain_test=text,shift_number=shift,direction_number=direction)
    
    try_again = input("say 'yes' if you want to play again, say 'no' if you dont want to play : ").lower()
    if try_again == "no":
        again = False
        print("Good Bye")

"""
def encrypt(plain_test,shift_number):
    encrypted_word = ""
    for letter in plain_test:
        position = alphabet.index(letter)
        new_positon = position + shift_number
        new_letter = alphabet[new_positon]
        encrypted_word += new_letter
    print(encrypted_word)

def decrypt(plain_test,shift_number):
    decrypted_word = ""
    for letter in plain_test:
        position = alphabet.index(letter)
        new_positon = position - shift_number
        new_letter = alphabet[new_positon]
        decrypted_word += new_letter
    print(decrypted_word)


if (direction=="encode"):
    encrypt(plain_test=text,shift_number=shift)
elif (direction=="decode"):
    decrypt(plain_test=text,shift_number=shift)
else:
    print("you have choosen the wrong direction")
"""