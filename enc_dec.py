from cryptography.fernet import Fernet


def encrypter(key, plaintext):
    fernet = Fernet(key)
    enc_message = fernet.encrypt(plaintext.encode())
    print('eeeeee',enc_message)
    return enc_message


def decrypter(key, ciphertext):
    c1 = "b'gAAAAABjMCbKdoHwKxecrT3vATPIeYkub49mmngwtsDfUKNE7Bm95eyDrevRv5KIkT4E88q7eClM_KV8WwOccn3ARjI3xceDzA=='"
    c2 = c1[2:-1]
    print("cccc2",c2)
    print("cccc2",type(c2))
    c3 = bytes(c2,'utf-8')
    print('c3333333',c3)
    print('c3333333',type(c3))

    fernet = Fernet(key)
    dec_message = fernet.decrypt(c3).decode()
    return dec_message


def generatekey():
    key = Fernet.generate_key()
    return key


if __name__ == "__main__":
    plaintext = "01674206688"

    key = generatekey()

    ciphertext = encrypter(key, plaintext)

    print("")
    print("Original string: ", plaintext)
    print("")
    print("Encrypted string: ", repr(ciphertext))
    print("")
    print("Key: ", repr(key))
    print("")

    decoded_message = decrypter(key, ciphertext)
