class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return sorted(nums)
nums=[0,1,0,2,1,1,0]
s=Solution()
k=s.sortColors(nums)
print(k)