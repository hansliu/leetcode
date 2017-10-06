class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        def foo(array):
            if array in self.result:
                return
            for i in xrange(len(array)):
                foo(array[:i] + array[i+1:])
            self.result.append(array)
        foo(nums)
        return self.result

print Solution().subsets([1,2,3])
