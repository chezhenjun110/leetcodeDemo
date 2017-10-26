class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cache=0
        if(target>nums[-1]):
            return len(nums)
        for i in range(len(nums)):
            if(target>nums[i]):
                cache=cache+1
            else:
                return cache
s=Solution()
print(s.searchInsert([1,3,5,6],0))