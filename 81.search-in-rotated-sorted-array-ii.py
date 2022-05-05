#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (35.57%)
# Likes:    4377
# Dislikes: 722
# Total Accepted:    422.6K
# Total Submissions: 1.2M
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].
#
# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.
#
# You must decrease the overall operation steps as much as possible.
#
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
#
#
#
# Follow up: This problem is similar to Search in Rotated Sorted Array, but
# nums may contain duplicates. Would this affect the runtime complexity? How
# and why?
#
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if 1 == len(nums):
            return target == nums[0]

        low, high = 0, len(nums)-1
        while low <= high:
            while low < high and nums[low] == nums[low+1]:
                low += 1
            while low < high and nums[high] == nums[high-1]:
                high -= 1

            mid = (low + high) // 2
            if target == nums[mid]:
                return True

            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                    continue
                low = mid + 1
                continue
            if nums[mid] <= nums[high]:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                    continue
                high = mid - 1
                continue
        return False
# @lc code=end
