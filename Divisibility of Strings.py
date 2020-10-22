def divisible(s, t):
    if len(s) % len(t) != 0:
        return -1
    n = len(s) // len(t)
    if s != t*n:
        return -1
    for i in range(len(t)//2):
        if len(t) % (i+1) == 0:
            cur = len(t) // (i+1)
            if cur * t[:i+1] == t:
                return t[:i+1]
    return len(t)

print(divisible('bcdbcdbcd', 'bcdbcd'))
print(divisible('bcdbcdbcd', 'bcd'))
print(divisible('bcdbcdbcdd', 'bcdbcd'))
print(divisible('bcd', 'bcd'))