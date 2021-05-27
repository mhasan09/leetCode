def generateDocument(characters, document):
    data_dict_char = {}
    for i in range(0, len(characters)):
        if characters[i] in data_dict_char:
            data_dict_char[characters[i]] += 1
        else:
            data_dict_char[characters[i]] = 1
    for i in range(0, len(document)):
        if document[i] not in data_dict_char or data_dict_char[document[i]] == 0:
            return False
        else:
            data_dict_char[document[i]] -= 1
    return True


print(generateDocument("aheaolabbhb", "hello"))
