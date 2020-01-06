class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        res = 0
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        if k != 0:
            for i in dic:
                if (i-k) in dic and dic[i-k] > 0:
                    res += 1
                if (i+k) in dic and dic[i+k] > 0:
                    res += 1
                dic[i] = 0
        else:
            for i in dic:
                if dic[i] > 1:
                    res += 1
        return res

    # use dict to record elements