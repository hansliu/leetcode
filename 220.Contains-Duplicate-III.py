class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0 or t < 0:
            return False
        d = {}
        bucket = t + 1
        for i, n in enumerate(nums):
            index = n / bucket
            if index in d:
                return True
            if index-1 in d and abs(d[index-1] - n) <= t:
                return True
            if index+1 in d and abs(d[index+1] - n) <= t:
                return True
            d[index] = n
            if i >= k:
                del d[nums[i-k] / bucket]
        return False

