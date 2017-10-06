class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.dfs([], 0, s)
        return self.result

    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        return l >= r

    def dfs(self, array, l, s):
        if l == len(s):
            self.result.append(array)
        for r in xrange(l, len(s)):
            if self.isPalindrome(l, r, s):
                self.dfs(array + [s[l:r+1]], r+1, s)

print Solution().partition("bab")
print Solution().partition("aab")
