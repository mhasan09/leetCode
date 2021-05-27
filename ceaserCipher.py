def caesarCipherEncryptor(string, key):
    newLetter = []
    neyKey = key % 26
    for i in string:
        newLetter.append(getNewLetter(i, neyKey))
    return "".join(newLetter)


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


print(caesarCipherEncryptor("xyz",2))