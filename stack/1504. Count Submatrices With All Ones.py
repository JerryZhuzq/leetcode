def numSubmat(mat) -> int:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if not mat[i][j]:
                continue
            mat[i][j] += mat[i-1][j] if i-1 >= 0 else 0
    # count submatrices with all 1s with bottom left corner at (i,j)
    ret = 0
    print(mat)
    for i in range(len(mat)):
        row = mat[i]
        stack = []
        tot = 0   # means the total val in stack
        for j in range(len(row)):
            ths = 1   # means the total length of current val
            while stack and stack[-1][0] >= row[j]:
                popped = stack.pop()
                tot -= popped[0] * popped[1]
                ths += popped[1]
            stack.append([row[j], ths])
            tot += ths * row[j]
            ret += tot
        print(ret)
    return ret


mat = [[1,0,1],[1,1,0],[1,1,0]]
numSubmat(mat)

