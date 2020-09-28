import copy


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        union1 = [i for i in range(n + 1)]
        type1 = [n for n in edges if n[0] == 1]
        type2 = [n for n in edges if n[0] == 2]
        type3 = [n for n in edges if n[0] == 3]

        # def find(i, union):
        #     p = union[i]
        #     while p != union[p]:
        #         p = union[p]
        #     union[i] = p
        #     return p

        def find(i, union):
            if i != union[i]:
                union[i] = find(union[i])
            return i

        res, l1, l2 = 0, 0, 0
        for e in type3:
            x, y = find(e[1], union1), find(e[2], union1)
            if x == y:
                res += 1
            else:
                union1[x] = y
                l1 += 1
                l2 += 1
        union2 = union1.copy()

        for e in type2:
            x, y = find(e[1], union2), find(e[2], union2)
            if x == y:
                res += 1
            else:
                union2[x] = y
                l1 += 1

        for e in type1:
            x, y = find(e[1], union1), find(e[2], union1)
            if x == y:
                res += 1
            else:
                union1[x] = y
                l2 += 1
        if l1 != n - 1 or l2 != n - 1:
            return -1
        return res




