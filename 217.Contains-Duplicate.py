class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums.count(0) > 1:
            return True
        return sum(nums) - sum(set(nums)) != 0

print Solution().containsDuplicate([-1200000005,-1200000005])
