# from itertools import permutations
# from collections import Counter
#
# b = '123556779'
# d = '123456798'
#
# c = Counter(d)
# ans = ''
#
# if_f = False
# if_over = False
# small = min(c.keys())
# for i in b:
#     if not if_f:
#         if i in c:
#             ans += i
#             c[i] -= 1
#             if c[i] == 0:
#                 c.pop(i)
#                 if c:
#                     small = min(c.keys())
#
#         else:
#             if_f = True
#             for n in range(int(i)+1, 10):
#                 n = str(n)
#                 if n in c:
#                     ans += n
#                     c[n] -= 1
#                     if c[n] == 0:
#                         c.pop(n)
#                         if c:
#                             small = min(c.keys())
#                     break
#                 if_over = True
#             if if_over:
#                 print('-1')
#                 break
#     else:
#         ans += small
#         c[small] -= 1
#         if c[small] == 0:
#             c.pop(small)
#             if c:
#                 small = min(c.keys())
#
#
# if not if_over:
#     if ans == b:
#         one, two = ans[-1], ans[-2]
#         print(ans[:-2]+one+two)
#     else:
#         print(ans)
#
#


import sys
from collections import Counter
b = '2222252'
d = '2222215'
c = Counter(d)
if_f = False
if_over = False
small = min(c.keys())
ans = ''
for i in b:
    if not if_f:
        if i in c:
            ans += i
            c[i] -= 1
            if c[i] == 0:
                c.pop(i)
                if c and i == small:
                    small = min(c.keys())
        else:
            if_f = True
            for n in range(int(i)+1, 10):
                n = str(n)
                if n in c:
                    ans += n
                    c[n] -= 1
                    if c[n] == 0:
                        c.pop(n)
                        if c and n == small:
                            small = min(c.keys())
                    break
                if n == '9':
                    if_over = True
            if if_over:
                print('-1')
                break
    else:
        ans += small
        c[small] -= 1
        if c[small] == 0:
            c.pop(small)
            if c:
                small = min(c.keys())
if not if_over:
    if ans == b:
        one, two = ans[-1], ans[-2]
        print(ans[:-2]+one+two)
    else:
        print(ans)

#
