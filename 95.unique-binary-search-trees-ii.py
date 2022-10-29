#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (51.41%)
# Likes:    5460
# Dislikes: 357
# Total Accepted:    334.3K
# Total Submissions: 649.4K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if 1 == n:
            return [TreeNode(1)]

        dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        def gen(start: int, end: int):
            if start > end:
                return [None]
            if start == end:
                dp[start][end] = [TreeNode(start)]
                return dp[start][end]
            if dp[start][end] != -1:
                return dp[start][end]

            res = []
            for i in range(start, end+1):
                left_trees, right_trees = gen(start, i-1), gen(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            dp[start][end] = res
            return dp[start][end]

        return gen(1, n)
# @lc code=end
