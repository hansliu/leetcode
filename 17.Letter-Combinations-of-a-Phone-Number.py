class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.result = []
        def foo(tmp, i, digits):
            if i == len(digits):
                self.result.append(tmp)
                return
            for s in self.mapping[digits[i]]:
                foo(tmp + s, i+1, digits)
        if digits:
            foo("", 0, digits)
        return self.result
