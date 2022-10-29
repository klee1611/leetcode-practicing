#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (59.24%)
# Likes:    8357
# Dislikes: 329
# Total Accepted:    532.5K
# Total Submissions: 898.8K
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 19
#
#
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
# @lc code=end
