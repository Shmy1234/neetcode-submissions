class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) -1
        while i <= j:
            m = (i+j)//2
            if target in matrix[m]:
                return True
            elif target > matrix[m][0]:
                i = m + 1
            elif target < matrix[m][0]:
                j = m -1
        
        return False