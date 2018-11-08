import collections

class Solution(object):


    def nofirstUniquechar(self,char):
        count_char = collections.Counter(char)
        for i in count_char:
            if count_char.get(i) == 1:
                uniquechar = i
                break
        count_num = 0
        for i in char:
            if i == uniquechar:
                return count_num
            count_num = count_num + 1



i = Solution()
print(i.nofirstUniquechar('asdfasdfij'))