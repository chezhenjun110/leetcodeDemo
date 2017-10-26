class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num=len(prices)
        if(prices==[]):
            return 0
        minimum = prices[0]
        for i in range(num):
            if (prices[i] < minimum):
                minimum = prices[i]
            if(prices[i]-minimum>=0):
                prices[i]=prices[i]-minimum
            else:
                prices[i]=-1
        return max(prices)                   #遍历数组，每次将该位置的数字与前n个的最小值做比较


s=Solution()
print(s.maxProfit([7, 6, 4, 3, 1]))