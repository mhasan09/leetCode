import ast
from cryptography.fernet import Fernet


def encrypter(key, plaintext):
    fernet = Fernet(key)
    enc_message = fernet.encrypt(plaintext.encode())
    return enc_message


def decrypter(key, ciphertext):
    fernet = Fernet(key)
    dec_message = fernet.decrypt(ast.literal_eval(ciphertext)).decode()
    print(dec_message)
    return dec_message


def generatekey():
    key = Fernet.generate_key()
    return key


if __name__ == "__main__":
    plaintext = "01674206688"
    key = generatekey()
    ciphertext = encrypter(key, plaintext)
    decoded_message = decrypter(key, str(ciphertext))
    print(decoded_message)
