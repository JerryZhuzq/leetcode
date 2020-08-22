from collections import Counter
from sys import maxsize

def stickers(target, s):
    target_dict = Counter(target)
    s_dict_list = []
    res = 0
    for i in s:
        s_dict_list.append(Counter(i))
    while target_dict:
        next_dict = target_dict.copy()
        interval = 0
        for dic in s_dict_list:
            tmp_interval = maxsize
            tmp_dict = target_dict.copy()
            for k in target_dict:
                if k in dic:
                    tmp_interval = min(tmp_interval, target_dict[k]/tmp_dict[k])
                    tmp_dict[k] -= min(dic[k], target_dict[k])
                    if tmp_dict[k] == 0:
                        tmp_dict.pop(k)
            if tmp_interval > interval:
                next_dict = tmp_dict
                interval = tmp_interval
        target_dict = next_dict
        res += 1
    return res

print(stickers('aaaabbbbccccdddd', ['aaaa', 'ab', 'c', 'd']))


