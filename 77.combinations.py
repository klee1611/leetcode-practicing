#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (63.90%)
# Likes:    4086
# Dislikes: 140
# Total Accepted:    516.4K
# Total Submissions: 807.9K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if 1 == n and 1 == k:
            return [[1]]

        r = []
        def helper(
            nums: List[int],
            low: int,
            remain: int,
        ) -> None:
            if 0 == remain:
                r.append(nums[:k])
                return

            if n + 1 - low < remain:
                return

            for i in range(low, n+1, 1):
                helper(nums + [i], i+1, remain-1)

        helper([], 1, k)
        return r
# @lc code=end
