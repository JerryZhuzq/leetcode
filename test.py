a = ['asdfds','aweadsf','asdf']
indegree = dict(zip(set(''.join(a)), [0]*len(set(''.join(a)))))
adjacent = dict(zip(set(''.join(a)), [[] for _ in range(len(set(''.join(a))))]))
print(indegree)
print(adjacent)

