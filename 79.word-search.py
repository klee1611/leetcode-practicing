#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (39.65%)
# Likes:    9126
# Dislikes: 347
# Total Accepted:    953.6K
# Total Submissions: 2.4M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def helper(i: int, j: int, index: int):
            if index == len(word):
                return True

            if i - 1 >= 0 and word[index] == board[i-1][j]:
                tmp = board[i-1][j]
                board[i-1][j] = -1
                if True is helper(i-1, j, index+1):
                    return True
                board[i-1][j] = tmp

            if i + 1 < m and word[index] == board[i+1][j]:
                tmp = board[i+1][j]
                board[i+1][j] = -1
                if True is helper(i+1, j, index+1):
                    return True
                board[i+1][j] = tmp

            if j - 1 >= 0 and word[index] == board[i][j-1]:
                tmp = board[i][j-1]
                board[i][j-1] = -1
                if True is helper(i, j-1, index+1):
                    return True
                board[i][j-1] = tmp

            if j + 1 < n and word[index] == board[i][j+1]:
                tmp = board[i][j+1]
                board[i][j+1] = -1
                if True is helper(i, j+1, index+1):
                    return True
                board[i][j+1] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = -1
                    if True is helper(i, j, 1):
                        return True
                    board[i][j] = tmp
        return False
# @lc code=end
