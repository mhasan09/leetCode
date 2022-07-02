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


# print(reverse_number(4351))

def isPrime(start, end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


# print(isPrime(1, 101))

def isPrime2(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


# print(isPrime2(5))

def valid_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


# print(valid_palindrome('madam'))


def valid_palindrome2(s):
    # s = [i for i in s.lower() if i.isalnum()]
    # return s == s[::-1]

    chars = []
    for i in s:
        if i.isalnum():
            chars.append(i)
    return chars == chars[::-1]


# print(valid_palindrome2('madam'))

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
        else:
            stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return False


# print(valid_Parentheses('()[]{}'))

def group_anagram(strs):
    result = {}
    for s in strs:
        key = "".join(sorted(list(s)))  # key = aet,aet,ant,aet,ant,abt...
        if key in result:
            result[key].append(s)  # aet:[eat,tea]...
        else:
            result[key] = [s]  # aet: [eat]

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


# print(valid_anagram('car','arb'))

def longest_running_substring(s):
    store = {}
    tracker = 0
    result = 0
    for i in range(0, len(s)):
        if s[i] in store:
            tracker = max(i, store[s[i]] + 1)
        result = max(result, i - tracker + 1)
        store[s[i]] = i
    return result


# print(longest_running_substring('pwwkew'))


def maxArea(arr):
    result = 0
    l, r = 0, len(arr) - 1
    while l < r:
        area = min(arr[l], arr[r]) * (r - l)
        result = max(result, area)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return result


# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


def threeSum(arr):
    arr.sort()
    result = []
    for i, a in enumerate(arr):
        if i > 0 and a == arr[i - 1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            currentSum = a + arr[l] + arr[r]
            if currentSum > 0:
                r -= 1
            elif currentSum < 0:
                l += 1
            else:
                result.append([arr[l], arr[r], a])
                l += 1
                while arr[l] == arr[l - 1] and l < r:
                    l += 1
    return result


# print(threeSum([-1, 0, 1, 2, -1, -4]))

def twoSum(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        currentSum = arr[l] + arr[r]
        if currentSum < target:
            l += 1
        elif currentSum > target:
            r -= 1
        else:
            return l, r


def twoSumHasah(arr, target):
    result = {}
    for i in range(0, len(arr)):
        p = target - arr[i]
        if p in result:
            return [result[p], i]
        else:
            result[arr[i]] = i
    return


# print(twoSum([2, 7, 11, 15], 9))


def findMininRotatedSortedArr(arr):
    l, r = 0, len(arr) - 1
    result = arr[0]
    while l < r:
        if arr[l] < arr[r]:
            return min(result, arr[l])
            break
        mid = (l + r) // 2
        result = min(result, arr[mid])
        if arr[l] <= arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return result


# print(findMininRotatedSortedArr([3, 4, 5, 1, 2]))


def searchInRotatedSortedArr(arr, target):
    if not arr:
        return -1
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[r]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


# print(searchInRotatedSortedArr([4, 5, 6, 7, 0, 1, 2], 0))


def productExceptSelf(arr):
    l, r, result = [0] * len(arr), [0] * len(arr), [0] * len(arr)
    l[0] = 1
    for i in range(1, len(arr)):
        l[i] = l[i - 1] * arr[i - 1]
    r[len(arr) - 1] = 1
    for k in reversed(range(len(arr) - 1)):
        r[k] = r[k + 1] * arr[k + 1]

    for i in range(len(arr)):
        result[i] = l[i] * r[i]
    return result


print(productExceptSelf([1, 2, 3, 4]))
