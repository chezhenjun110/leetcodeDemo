class Solution(object):
    def matrixReshape(self, matrix):
        """
        :type nums: List[List[int]]
        :rtype: List[List[int]]
        """
        cache=[x[:] for x in matrix]
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                matrix[j][i]=cache[len(matrix[0]) - i - 1][j]
        return matrix
nums = [[1, 2], [3,4]]
s=Solution();
print(s.matrixReshape(nums))

