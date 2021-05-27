def minimumCharactersForWords(words):
    global charactersFrequncies
    maximumCharactersHashmap = {}
    for i in words:
        charactersFrequncies = countCharacterFrequency(i)
        updateMaximumFrequencies(charactersFrequncies, maximumCharactersHashmap)
    return makeArray(maximumCharactersHashmap)


def countCharacterFrequency(string):
    hashTable = {}
    for i in string:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    return hashTable


def updateMaximumFrequencies(frequencies, maximumFrequncies):
    for i in frequencies:
        frequency = frequencies[i]
        if i in maximumFrequncies:
            maximumFrequncies[i] = max(frequency, maximumFrequncies[i])
        else:
            maximumFrequncies[i] = frequency


def makeArray(characterFrequency):
    charcter = []
    for i in characterFrequency:
        frequency = characterFrequency[i]
        for _ in range(frequency):
            charcter.append(i)
    return charcter


print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))
# def minimumCharactersForWords(words):
#     global characterFrequencies
#     maximumCharacterFrequencies = {}
#     for i in words:
#         characterFrequencies = countCharacterFrequencies(i)
#         print(characterFrequencies)
#         updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)
#
#     return makeArray(maximumCharacterFrequencies)
#
#
# def countCharacterFrequencies(string):
#     characterFrequencies = {}
#     for i in string:
#         if i in characterFrequencies:
#             characterFrequencies[i] += 1
#         else:
#             characterFrequencies[i] = 1
#     return characterFrequencies
#
#
#
# def updateMaximumFrequencies(frequencies, maxFrequencies):
#     for i in frequencies:
#         frequency = frequencies[i]
#         if i in maxFrequencies:
#             maxFrequencies[i] = max(frequency, maxFrequencies[i])
#         else:
#             maxFrequencies[i] = frequency
#
#
# def makeArray(characterFrequency):
#     characters = []
#     for i in characterFrequency:
#         frequency = characterFrequency[i]
#         for _ in range(frequency):
#             characters.append(i)
#     return characters
#
# print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))
