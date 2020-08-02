
def encrpt(message, key):
    
    encrypted_message = ""
    for i in message:
        encrypted_character = chr(ord(i) ^ key)
        encrypted_message += encrypted_character
    return encrypted_message


if __name__ == "__main__":

    encrypted_message_lst = []
    key = 250
    with open("input.txt", "r") as fread:
        message = fread.readlines()
        with open("encrypted.txt", "w") as fwrite:
            for i in message:
                encrypted_message = encrpt(i, key)
                fwrite.write(encrypted_message)