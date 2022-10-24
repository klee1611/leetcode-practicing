#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (55.17%)
# Likes:    6830
# Dislikes: 193
# Total Accepted:    615.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
#
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        r = [[]]
        nums.sort()
        def helper(prev, start):
            if start >= len(nums):
                return
            r.append(prev + [nums[start]])
            for i in range(start+1, len(nums)):
                if i > start+1 and nums[i] == nums[i-1]:
                    continue
                helper(prev + [nums[start]], i)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            helper([], i)

        return r
# @lc code=end
