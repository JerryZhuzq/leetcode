def findMaxForm(strs, m, n) -> int:
    d = len(strs)
    store = [[0, 0] for x in range(d)]
    memo = [[-1] for x in range(n + 1) for x in range(m + 1)]
    print(store)
    for i in range(d):
        num0, num1 = 0, 0
        for j in strs[i]:
            if j == "0":
                num0 += 1
            elif j == "1":
                num1 += 1
        print(i, num0, num1, store[i][0], store[i][1])
        store[i][0] = num0
        store[i][1] = num1
        print(store)

findMaxForm(["10","0001","111001","1","0"],5,3)