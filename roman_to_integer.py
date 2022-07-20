def romanToInt(s):
    res, prev = 0, 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in s[::-1]:
        print('i', i)
        if dict[i] >= prev:
            res += dict[i]
            print('res+', res)
            print('dict[i]', dict[i])
            print('prev', prev)
        else:
            res -= dict[i]
            print('res-', res)
        prev = dict[i]
        print('after', prev)
        print('------------------------------')
    return res


print(romanToInt("MCMXCIV"))
