from queue import PriorityQueue

q = PriorityQueue()
q.put(1)
q.put(2)
print(q[0])


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
#         print(res1, res2)
# except:
#     pass