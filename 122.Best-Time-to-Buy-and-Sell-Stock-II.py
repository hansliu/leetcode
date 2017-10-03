class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_max = 0
        if prices:
            cur = prices[0]
            for p in prices[1:]:
                if p - cur > 0:
                    best_max += p-cur
                    cur = p
                else:
                    cur = p
        return best_max

print Solution().maxProfit([1,2,4])
