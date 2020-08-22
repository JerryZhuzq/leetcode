from collections import defaultdict
import heapq
def getMaxUnit(num, boxes, unitSize, unitsperBox, truckSize):
    res = 0
    from collections import defaultdict
    store = defaultdict(int)
    for i in range(len(boxes)):
        store[unitsperBox[i]] = boxes[i]
    unitsperBox.sort(reverse=True)
    for i in unitsperBox:
        if truckSize <= store[i]:
            res += truckSize*i
            return res
        else:
            truckSize -= store[i]
            res += store[i]*i


# print(getMaxUnit(3, [1, 2, 3], 3, [3, 2, 1], 3))
# print(getMaxUnit(3, [3,1,6], 3, [2,7,4],6))
# print(getMaxUnit(1, [1],1,[2],1))
# print(getMaxUnit(2,[1,1],2,[9,6],1))


def funwithAnagrams(s):
    if len(s) == 0:
        return []
    cur = s[0]
    res = [s[0]]
    store = defaultdict(int)
    for i in s[1:]:
        if len(cur) != len(i):
            cur = i
            res.append(i)
        else:
            for j in cur:
                store[j] += 1
            for j in i:
                if j not in store:
                    cur = i
                    res.append(i)
                    break
                else:
                    store[j] -= 1
                    if store[j] == 0:
                        store.pop(j)
            if len(store) > 0:
                cur = i
                res.append(i)
    res.sort()
    return res
# print(funwithAnagrams(['code', 'doce', 'ecod', 'framer', 'frame']))
# print(funwithAnagrams(['code', 'framer', 'frame', 'doce']))


def modifyArray(arr):
    hp = [arr[0]]
    # min-heap to calculate for smallest differernce of increasing array
    val_min = 0
    val_max = 0
    for i in arr[1:]:
        if i <= hp[0]:
            heapq.heappush(hp, i)
        else:
            val_min += i-hp[0]
    hp = [-arr[0]]
    for i in arr[1:]:
        if i+hp[0] >= 0:
            heapq.heappush(hp, -i)
        else:
            val_max += abs(hp[0]+i)
    print(val_min, val_max)
    return min(val_max, val_min)
print(modifyArray([0,1,2,5,6,5,7]))
print(modifyArray([9,8,7,2,3,3]))


from collections import defaultdict
def funWithAnagrams(text):
    # Write your code here
    if len(text) == 0:
        return []
    res = []
    store = set()
    for t in text:
        sorted_t = ''.join(sorted(t))
        print(sorted_t, t)
        if sorted_t not in store:
            store.add(sorted_t)
            res.append(t)
    res.sort()
    return res

# print(funWithAnagrams(['code', 'aaagmnrs', 'anagrams', 'doce']))

a = [1,2,3]
a = a[::-1]
print(a)