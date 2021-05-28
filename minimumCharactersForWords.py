def minimumCharactersForWords(words):
    maximumCharacterHashmap = {}
    for i in words:
        characterCount = countCharacter(i)
        compareBetweeenHashmap(characterCount, maximumCharacterHashmap)
    return makeArray(maximumCharacterHashmap)


def countCharacter(string):
    hashmap = {}
    for i in string:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap


def compareBetweeenHashmap(frequecies, maximumFrequencies):
    for i in frequecies:
        frequency = frequecies[i]
        if i in maximumFrequencies:
            maximumFrequencies[i] = max(frequency, maximumFrequencies[i])
        else:
            maximumFrequencies[i] = frequency


def makeArray(maximumFrequencies):
    character = []
    for i in maximumFrequencies:
        frequency = maximumFrequencies[i]
        for _ in range(frequency):
            character.append(i)
    return character


print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))