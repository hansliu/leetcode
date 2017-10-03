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
                    best_max = max(best_max, p-cur)
                else:
                    cur = p
        return best_max

print Solution().maxProfit([])
print Solution().maxProfit([7, 1, 5, 3, 6, 4])
print Solution().maxProfit([7, 6, 4, 3, 1])
