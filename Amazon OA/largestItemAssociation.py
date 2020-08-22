from collections import defaultdict
from collections import deque

# def largestItemAssociation(itemAssociation):
# multiple association
def func(itemAssociation):
    store = defaultdict(list)
    n = len(itemAssociation)
    for i in range(n):
        for item in itemAssociation[i]:
            store[item].append(i)
    res = []
    visited = set()
    for item in store:
        if item not in visited:
            visited.add(item)
            q = deque()
            q += store[item]
            temp = []
            while q:
                i = q.popleft()
                temp += itemAssociation[i]
                for c in itemAssociation[i]:
                    if c not in visited:
                        visited.add(c)
                        q += store[c]
            res.append(list(set(temp)))
    res.sort(key=lambda x: len(x), reverse=True)
    length = len(res[0])
    final = []
    for i in res:
        if len(i) == length:
            i.sort()
            final.append(i)
        else:
            break
    final.sort()
    return final[0]


print(func([['A', 'B'], ['D', 'E'], ['C', 'D']]) == ['C', 'D', 'E'])
print(func([['A', 'B'], ['C', 'D'], ['F', 'E']]) == ['A', 'B'])
print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]) == ['C', 'D', 'E', 'F'])
print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]) == ['A', 'B', 'C', 'D', 'E', 'F'])
print(func([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'],
            ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
            ['A', 'C'],]) == ['A', 'B', 'C', 'D', 'E', 'F'])
print(func([['item1','item2'],['item3','item4'],['item4','item5']]) == ['item3', 'item4', 'item5'])
print(func([['item1','item2'],['item2','item5'],['item3']]) == ['item1', 'item2', 'item5'])
print(func([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]) == ['item1', 'item2', 'item3'])
print(func([["item1","item2"], ["item1","item3"], ["item2","item7"], ["item3","item7"], ["item5","item6"], ["item3","item7"]]) == ['item1', 'item2', 'item3', 'item7'])

print(func([['item1', 'item2'], ['item1', 'item4'], ['item3', 'item4'], ['item4', 'item5']]))

print(func([["item3","item4"], ["item1","item2"], ["item5","item6"], ["item4","item5"], ["item2","item7"], ["item7","item8"]]))

print(func([["item1","item2"], ["item3","item4"], ["item5","item6"], ["item4","item5"]]))