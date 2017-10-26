class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        childnums=[]
        if len(nums)*len(nums[0])!=r*c:
            return nums;
        else:
            for i in range(0,len(nums)):
                childnums+=nums[i]
            return [childnums[i:i+c] for i in range (0,len(childnums),c)]
nums = [[1, 2], [3,4]]
s=Solution();
print(s.matrixReshape(nums,1,4))