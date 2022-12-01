def halves_are_alike(s):
    length = len(s)
    mid = length // 2
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    first, second = 0, 0

    for i in range(0, length):
        if s[i] in vowel_list:
            if i < mid:
                first += 1
            else:
                second += 1
    return first == second


print(halves_are_alike("boek"))
