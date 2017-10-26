# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        m=len(nums)
        currentMin=nums[0]+nums[1]+nums[m-1]
        for i in range(m-2):
            lo=i+1
            hi=m-1
            current=nums[i]
            while lo<hi:
                s=nums[lo]+nums[hi]+current
                if s==target:
                    return s
                if abs(s - target) < abs(currentMin - target):
                    currentMin = s
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
        return currentMin

S =[-1,2,1,-4]

s=Solution()
print(s.threeSumClosest(S,1))
