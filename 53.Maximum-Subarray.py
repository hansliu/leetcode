class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            cur_sum = max_sum = nums[0]
            for n in nums[1:]:
                cur_sum = max(n, cur_sum+n)
                max_sum = max(cur_sum, max_sum)
        return max_sum

print Solution().maxSubArray([1,-1,3,4])
