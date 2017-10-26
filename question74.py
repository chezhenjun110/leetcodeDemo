class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=0
        i=0
        row=len(matrix)
        if(matrix==[] or matrix==[[]]):
            return False
        else:
            column = len(matrix[0])
            if(target<matrix[0][0] or target>matrix[row-1][column-1]):
                return False
            else:

                while  m<row:
                    if(matrix[m][0]>target):
                        while i<column:
                            if (matrix[m - 1][i] == target):
                                return True
                            else:
                                i=i+1
                        return False
                    elif(matrix[m][0]==target):
                        return True
                    else:
                        m=m+1
                return False
s=Solution()
print(s.searchMatrix([[1,3]],3))

