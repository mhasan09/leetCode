def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}
    for i in words:
        characterFrequencies = countCharacterFrequencies(i)


def countCharacterFrequencies(words):
    characterFrequencies = {}
    for i in range(len(words)):
        for j in words[i]:
            if j in characterFrequencies:
                characterFrequencies[j] += 1
            else:
                characterFrequencies[j] = 1
    print(characterFrequencies)

print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))
