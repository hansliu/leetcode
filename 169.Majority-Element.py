class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        t = n / 2
        for x in set(nums):
            if nums.count(x) > t:
                return x

print Solution().majorityElement([1 ,2 ,3, 3, 3])
