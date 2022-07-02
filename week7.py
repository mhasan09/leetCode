def reverse_string(s):
    output = ""
    for i in reversed(range(len(s))):
        output = output + s[i]
    return output


# print(reverse_string('abc'))


def reverse_number(n):
    rev = 0
    while n > 0:
        remainder = n % 10
        rev = rev * 10 + remainder
        n = n // 10
    return rev


# print(reverse_number(1234))


def isPrime(start, end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


# print(isPrime(1,100))

def isPrime2(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


print(isPrime2(5))


def valid_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and s[l].isalnum():
            l += 1
        while l < r and s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def valid_Parentheses(s):
    data = {
        ')': '(',
        '}': '{',
        ']': '[',

    }

    stack = []
    for i in s:
        if i in data:
            if stack and stack[-1] == data[i]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True

    else:
        return False


def group_anagram(strs):
    result = {}
    for i in strs:
        key = "".join(sorted(list(i)))
        if key in result:
            result[key].append(i)
        else:
            result[key] = [i]
    return [i for i in result.values()]


# print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))


def valid_anagram(s, t):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    for i in t:
        if i in result:
            result[i] -= 1
        else:
            return False
    for i in result.values():
        if i != 0:
            return False
        else:
            return True


def maxArea(arr):
    l, r = 0, len(arr) - 1
    result = 0
    while l < r:
        area = min(arr[l], arr[r]) * (r - l)
        result = max(result, area)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return result


def threeSum(arr):
    arr.sort()
    result = []
    for i in range(0, len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            currentSum = arr[l] + arr[r] + arr[i]
            if currentSum < 0:
                l += 1
            elif currentSum > 0:
                r -= 1
            else:
                result.append([arr[l], arr[r], arr[i]])
            while l < r and arr[l] == arr[l + 1]:
                l += 1
            while l < r and arr[r] == arr[r + 1]:
                r -= 1
            l += 1
            r -= 1
    return result


def twoSum(arr, target):
    result = {}
    p = 0
    for i in range(0, len(arr) - 1):
        p = target - arr[i]
        if p in result:
            return [i, result[p]]
        else:
            result[arr[i]] = i
    return


def productExceptSelf(arr):
    left, right, result = [0] * len(arr), [0] * len(arr), [0] * len(arr)
    left[0] = 1
    for i in range(1, len(arr)):
        left[i] = left[i - 1] * arr[i - 1]
    right[len(arr) - 1] = 1
    for i in reversed(range(len(arr) - 1)):
        right[i] = right[i + 1] * arr[i + 1]
    for i in range(len(arr)):
        result[i] = left[i] * right[i]

    return result


# print(productExceptSelf([1, 2, 3, 4]))


def findMininRotatedSortedArr(arr):
    l, r = 0, len(arr) - 1
    result = arr[0]
    while l < r:
        if arr[l] < arr[r]:
            return min(result, arr[l])
            break
        m = arr[l] + arr[r] // 2
        result = min(result, arr[m])
        if arr[l] <= arr[m]:
            r = m - 1
        else:
            l = m + 1
    return result


def searchInRotatedSortedArr(arr, target):
    if not arr:
        return -1
    l, r = 0, len(arr) - 1
    while l < r:
        m = arr[l] + arr[r] // 2
        if arr[m] == target:
            return m
        if arr[l] <= arr[m]:
            if arr[l] <= target <= arr[m]:
                r = m - 1
            else:
                l = m + 1
        if arr[r] <= arr[m]:
            if arr[m] <= target <= arr[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


def fibonacci3(n):
    if n <= 1:
        return n
    else:
        return (fibonacci3(n - 1) + fibonacci3(n - 2))


nterms = int(input('enter'))
if nterms <= 0:
    print('enter positive int')
else:
    for i in range(nterms):
        print(fibonacci3(i))
