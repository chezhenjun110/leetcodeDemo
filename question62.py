import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        vector=[[ 0 for col in range(n) ] for row in range(m) ]
        for i in range(m):
            vector[i][0]=1
        for j in range(n):
            vector[0][j]=1
        for a in range(1,m):
            for b in range(1,n):
                vector[a][b]=vector[a-1][b]+vector[a][b-1]
        return vector[m-1][n-1]



s=Solution()
print(s.uniquePaths(10,1))