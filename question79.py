# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
class Solution(object):
    def location(self,board,i,j,word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.location(board, i + 1, j, word[1:]) or self.location(board, i - 1, j, word[1:]) \
              or self.location(board, i, j + 1, word[1:]) or self.location(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        rownum=len(board)
        columnnum=len(board[0])
        for i in range(rownum):
            for j in range(columnnum):
                if self.location(board,i,j,word):
                    return True
        return False
s=Solution()
board =["CAA",
        "AAA",
        "BCD"]
word="AAB"

print(s.exist(board,word))
