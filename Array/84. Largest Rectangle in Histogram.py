class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[-1,-1]]
        res = 0
        if not heights:
            return res
        if len(heights) == 1:
            return heights[0]
        for i in range(len(heights)):
            if len(stack) > 1 and heights[i] <= stack[-1][0]:
                while(len(stack) > 1 and heights[i] <= stack[-1][0]):
                    cur = stack.pop()
                    res = max(res, cur[0]*(i-stack[-1][1]-1))
            stack += [[heights[i],i]]
        while(len(stack) > 1):
                cur = stack.pop()
                res = max(res, cur[0]*(len(heights)-stack[-1][1]-1))
        return res