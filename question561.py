class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        s_so_far=0
        for i in range(0, len(nums) - 1, 2):
            s_so_far += nums[i]
        return s_so_far