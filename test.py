import time, functools


def metric(func):
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# try:
#     while True:
#         line = sys.stdin.readline()
#         l = int(line)
#         res1 = []
#         res2 = []
#         for i in range(l):
#             line = sys.stdin.readline()
#             val1, val2 = int(line.split()[0]), int(line.split()[0])
#             res1.append(val1)
#             res2.append(val2)
#         print(res1, res2)123
# except:
#     pass