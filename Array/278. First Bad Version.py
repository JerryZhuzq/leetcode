# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        l, r = 0, n - 1
        mid = (l + r) // 2
        while l < r:
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2
        if isBadVersion(mid):
            return mid
        else:
            return mid + 1


