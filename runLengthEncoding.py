def runLengthEncoding(string):
    length = 1
    array = []
    print(len(string))
    for i in range(1, len(string)):
        current = string[i]
        previous = string[i-1]
        if current != previous or length == 9:
            array.append(str(length))
            array.append(previous)
            length = 0
        length += 1

    array.append(str(length))
    array.append(string[len(string) - 1])
    return "".join(array)


print(runLengthEncoding('AAAAAAAAAAAAABBBBCCCCC'))
