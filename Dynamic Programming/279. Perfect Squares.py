class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        q = deque([[n, 1]])
        temp = set()
        while (q):
            node = q.popleft()
            value = node[0]
            step = node[1]
            i = 1
            while (True):
                num = value - i * i
                print(num, q, temp)
                if num < 0:
                    break
                if num == 0:
                    return step
                if num not in temp:
                    q.append([num, step + 1])
                    temp.add(num)
                i += 1

    class Solution:
        def numSquares(self, n: int) -> int:
            if n < 1:
                return 0
            import sys
            squares = [x ** 2 for x in range(1, int(math.sqrt(n)) + 1)]
            memo = [sys.maxsize for x in range(n + 1)]
            for i in squares:
                memo[i] = 1
            for i in range(1, n + 1):
                for j in squares:
                    if i < j:
                        break
                    memo[i] = min(memo[i], memo[i - j] + 1)
            return memo[n]
            
            # not good time complexity

            # deque  Separate the process using queue by store the step.

        class Solution:
            def numSquares(self, n: int) -> int:
                squares = [x ** 2 for x in range(1, int(n ** 0.5) + 1)]

                def computeNum(n, count):
                    if count == 1:
                        return n in squares
                    for i in squares:
                        if computeNum(n - i, count - 1):
                            return True
                    return False

                for i in range(1, n + 1):
                    if computeNum(n, i):
                        return i
        # best time complexity solution