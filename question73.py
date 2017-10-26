class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rownum=len(matrix)
        columnum=len(matrix[0])
        for i in range(rownum):
            for j in range(columnum):
                if(matrix[i][j]==0):
                    for i in range(rownum):
                        for j in range(columnum):
                            matrix[i][j]=0
