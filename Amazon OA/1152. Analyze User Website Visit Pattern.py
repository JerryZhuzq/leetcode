class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        total_pattern = [[username[i], timestamp[i], website[i]] for i in range(len(username))]
        total_pattern.sort()
        user = defaultdict(list)
        for u, t, w in total_pattern:
            user[u].append(w)
        largest = 0
        sequences = defaultdict(int)  # different 3-sequences for visited websites
        res = []
        for k in user:
            if len(user[k]) > 2:
                for s in set(list(combinations(user[k], 3))):
                    sequences[s] += 1
                    if sequences[s] > largest:
                        res.clear()
                        res.append(s)
                        largest = sequences[s]
                    elif sequences[s] == largest:
                        res.append(s)
        res.sort()
        return res[0]