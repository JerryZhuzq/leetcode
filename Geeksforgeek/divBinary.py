# colored LED    Tom Sawyer And His Friends

def divBinary(n):
    if not n:
        return 0
    one, res = 0, 0
    for i in range(len(n)):
        print(i, n, res)
        if one == 1:
            if n[i] == 1:
                res += divBinary(n[i:])
                return res
            else:
                res += divBinary(n[i+1:]) + 1
        else:
            if n[i] == 1:
                res += divBinary(n[i+1:])
    return res + 1


def countWays(arr, n):
    pos = [0 for i in range(n)]
    p = 0

    # for loop for saving the positions
    # of all 1s
    for i in range(n):
        if (arr[i] == 1):
            pos[p] = i + 1
            p += 1

    # If array contains only 0s
    if (p == 0):
        return 0

    ways = 1
    for i in range(p - 1):
        ways *= pos[i + 1] - pos[i]

        # Return the total ways
    return ways


print(divBinary([1,0,1,0,1,0,1,0,0,1]))