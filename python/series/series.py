
def smash(s, num):
    l = []
    i = len(s) - num
    for val in range(i+1):
        l.append(s[val:num+val])
    return l

def slices(s, num):
    ans = []
    if num is 0:
        raise ValueError("zero")
    elif num is 1:
        ans = [ [int(x)] for x in s ]
        return ans
    elif num < len(s):
        i = len(s) - num
        # use list comprehension.
        ans = [ [int(y) for y in x] for x in smash(s, num) ]
        # print(ans)
        return ans
    elif num is len(s):
        temp = [ int(x) for x in s ]
        ans.append(temp)
        return ans
    elif num > len(s):
        raise ValueError("Very long length")
    else:
        raise ValueError("Very Short length")

if __name__ == '__main__':
    print(slices('49142', 3))
    # print('\n' * 5)
    # print(smash('49142', 3))
