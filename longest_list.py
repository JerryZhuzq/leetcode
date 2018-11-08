

def longest_list(a):
    w = 1
    seq_list = {}
    for i in a:
        if not seq_list:
            seq_list[w] = [i]
        else:
            dic = list(seq_list.keys())
            dic.reverse()
            for j in dic:
                if i > min(seq_list.get(j)) and j == w:
                    w += 1
                    seq_list[w] = [i]
                    break
                elif i > min(seq_list.get(j)):
                    j = j+1
                    seq_list[j].append(i)
                    break
                elif j==1:
                    seq_list[j].append(i)
                    break
    return seq_list

a = [18,17,19,6,11,21,23,15]
#print(longest_list(a))

def crazy_eight(a):
    w = 1
    seq_list = {}
    for i in a:
        if not seq_list:
            seq_list[w] = [i]
        else:
            dic = list(seq_list.keys())
            dic.reverse()
            for j in dic:
                v = seq_list.get(j)
                t = False
                for x in v:
                    if (i[0] == x[0] or i[1] == x[1] or i[1] == 8) and j == w:
                        w += 1
                        seq_list[w] = [i]
                        t = True
                        break
                    elif i[0] == x[0] or i[1] == x[1] or x[1] == 8:
                        j = j + 1
                        seq_list[j].append(i)
                        t = True
                        break
                    elif j == 1:
                        seq_list[j].append(i)
                        break
                if t:
                    break
    return seq_list
b = [['草花',7],['红桃',7],['草花','K'],['方块','K'],['红桃',8]]
print(crazy_eight(b))