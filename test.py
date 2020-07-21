from collections import deque

m, n = 5, 5
memo = [[-1] * (n+1) for _ in range(m+1)]
memo[1][1] =3
print(memo)