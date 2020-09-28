# def test(input1, input2):
#     input1 = input1.strip()
#     text_split = input1.split(' ')
#     res = 0
#     total = []
#     for s in text_split:
#         if s != '':
#             total.append(s)
#     print(total)
#     if len(total) == 0:
#         return 0
#     if input2 == 0:
#         return len(total)
#     for s in total:
#         l = len(s)
#         real = input2 % l
#         if real == 0:
#             res += 1
#             continue
#         if s[l - input2:] + s[:l - input2] == s:
#             res += 1
#     return res

print(test('adaada', 3))


def test(input1):
    if len(input1) % 2 != 0:
        return -1
    res = 0
    from collections import deque
    a = deque()
    for i in input1:
        if i == 'J':
            if len(a) == 0:
                res += 1
                a.append('K')
            else:
                a.pop()
        else:
            a.append(i)
    res += len(a) // 2
    return res


print(test('JKJJKKJK'))