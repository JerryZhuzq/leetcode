# 阿里扇形着色问题
class Solution(object):
    def colorOfSectors(self,n,m):
        nums = 0
        if n == 1:
            nums = m
        if n == 2:
            nums = m*(m-1)
        if n == 3:
            nums = m*(m-1)*(m-2)
        if n >=4:
            nums = m*pow(m-1,n-1)-self.colorOfSectors(n-1,m)
        return nums

i = Solution()
print(i.colorOfSectors(4,3))
