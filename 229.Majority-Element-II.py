class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = len(nums) / 3
        ans = []
        for x in set(nums):
            if nums.count(x) > t:
                ans.append(x)
        return ans
