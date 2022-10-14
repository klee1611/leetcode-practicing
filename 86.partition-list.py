#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (51.24%)
# Likes:    4882
# Dislikes: 582
# Total Accepted:    419.1K
# Total Submissions: 817.8K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [2,1], x = 2
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if None is head or None is head.next:
            return head

        r_head = ListNode()
        r_head_cur = r_head
        r_mid = ListNode()
        r_mid_cur = r_mid
        cur = head
        while None is not cur:
            if cur.val < x:
                r_head_cur.next = ListNode(cur.val, None)
                r_head_cur = r_head_cur.next
            else:
                r_mid_cur.next = ListNode(cur.val, None)
                r_mid_cur = r_mid_cur.next
            cur = cur.next
        r_head_cur.next = r_mid.next
        return r_head.next
# @lc code=end
