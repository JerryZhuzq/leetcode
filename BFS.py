
def adjcent_v(v,s):
    adj = []
    if s in v:
        for i in v[s]:
            adj.append(i)
    else:
        print("There is no %s in the dictionary!" %(s))
    return adj

def BFS(v,s):
    level = {s:0}
    parent = {s:None}
    level_num = 1

    frontier = [s]
    while frontier:
        next = []
        for i in frontier:
            adj = adjcent_v(v,i)
            for j in adj:
                if j not in level:
                    level[j] = level_num
                    parent[j] = i
                    next.append(j)
        frontier = next
        level_num += 1
    return level,parent


graph = {'s':['a','x'],'a':['s','z'],'x':['s','d','c'],'z':['a'],
         'c':['x','d','f','v'],'d':['x','c','f'],'f':['d','c','v'],'v':['c','f']}

level,parent = BFS(graph,'s')
print(level)
print(parent)