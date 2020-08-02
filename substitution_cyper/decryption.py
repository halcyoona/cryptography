def decrpt(message, key):
    
    decrypted_message = ""
    for i in message:
        decrypted_character = chr(ord(i) ^ key)
        decrypted_message += decrypted_character
    return decrypted_message


if __name__ == "__main__":

    encrypted_message_lst = []
    key = 250
    with open("encrypted.txt", "r") as fread:
        message = fread.readlines()
        with open("decrypted.txt", "w") as fwrite:
            for i in message:
                decrypted_message = decrpt(i, key)
                fwrite.write(decrypted_message)