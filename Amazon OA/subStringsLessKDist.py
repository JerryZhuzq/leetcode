



def subStringLessKDist(inputString, k):
    n = len(inputString)
    res = []
    for i in range(n+1-k):
        cur_str = set(list(inputString[i:i+k]))
        print(cur_str)
        if len(cur_str) == k-1:
            res.append(inputString[i:i+k])
    return res

print(subStringLessKDist("awaglk", 4))