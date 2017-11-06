class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        if m==1 or n==1:
            if 1 in obstacleGrid or [1] in obstacleGrid:
                return 0
        for i in range(m):
            if obstacleGrid[i][0]!=1:
                obstacleGrid[i][0] = 1
            else:
                for k in range(i,m):
                    obstacleGrid[k][0] = 0
                break
        for j in range(1,n):
            if  obstacleGrid[0][j] != 1:
                obstacleGrid[0][j] = 1
            else:
                for k in range(j,n):
                    obstacleGrid[0][k] = 0
                break
        for a in range(1, m):
            for b in range(1, n):
                if obstacleGrid[a][b]!=1:
                    obstacleGrid[a][b] = obstacleGrid[a - 1][b] + obstacleGrid[a][b - 1]
                else:
                    obstacleGrid[a][b]=0
        return obstacleGrid[m - 1][n - 1]
        # return obstacleGrid

s=Solution()
print(s.uniquePathsWithObstacles([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]))