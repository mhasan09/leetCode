def reverseWordsInString(string):
    words = []
    startofWords = 0
    for i in range(len(string)):
        character = string[i]
        if character == " ":
            words.append(string[startofWords:i])
            startofWords = i
        elif string[startofWords] == " ":
            words.append(" ")
            startofWords = i

    words.append(string[startofWords:])
    reversellc(words)
    return "".join(words)


def reversellc(list):
    start = 0
    end = len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


print(reverseWordsInString("AlgoExpert is the best!"))
