def aWayTooLongString(string):
    last = string[len(string)-1]
    size = len(string) - 2
    if len(string) > 10:
        s = string[0] + str(size) + last
        return s
    else:
        return string

print(aWayTooLongString("pneumonoultramicroscopicsilicovolcanoconiosis"))