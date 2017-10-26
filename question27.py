class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.remove(val)
        return len(nums)
s=Solution();
print(s.removeElement([3,2,2,3], 3))

