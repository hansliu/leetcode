class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, board, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = "$"
            if dfs(i+1, j, board, word[1:]) or dfs(i, j+1, board, word[1:]) or dfs(i-1, j, board, word[1:]) or dfs(i, j-1, board, word[1:]):
                return True
            board[i][j] = tmp
            return False

        if board:
            for i in xrange(len(board)):
                for j in xrange(len(board[i])):
                    if dfs(i, j, board, word):
                        return True
        return False

