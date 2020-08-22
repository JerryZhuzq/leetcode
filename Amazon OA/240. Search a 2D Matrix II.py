class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix)-1, 0
        while m > -1 and m < len(matrix) and n > -1 and n < len(matrix[0]):
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                n += 1
            else:
                m -= 1
        return False