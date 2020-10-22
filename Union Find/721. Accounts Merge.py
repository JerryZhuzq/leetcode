class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = [i for i in range(len(accounts))]
        def find(i):
            while i != union[i]:
                union[i] = union[union[i]]
                i = union[i]
            return i
        email = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email:
                    union[find(email[e])] = find(i)  # sequence doesn't matter
                email[e] = i
        ans = defaultdict(list)
        for e in email:
            root = find(email[e])   # remember here
            ans[root].append(e)
        res = []
        for r in ans:
            name = accounts[r][0]
            tmp = ans[r]
            tmp.sort()
            res.append([name]+tmp)
        return res