from collections import Counter

a = 'adsfadfa(dasfda)'
b = Counter(a)['(']
print(b)
