import math
a = '34345245'
b = []
for i in range(math.ceil(len(a)/3)):
    b.append(a[i*3:min(i*3+3, len(a))])
print(b)