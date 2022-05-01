#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (71.39%)
# Likes:    9805
# Dislikes: 156
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc code=start
class Solution:
    def helper(
        self,
        r: List[List[int]],
        nums: List[int],
        n: List[int],
        start: int
    ) -> None:
        r.append(n)
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            self.helper(r, nums, n + [nums[i]], i+1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if 1 == len(nums):
            return [[], nums]

        r = []
        self.helper(r, nums, [], 0)
        return r
# @lc code=end
