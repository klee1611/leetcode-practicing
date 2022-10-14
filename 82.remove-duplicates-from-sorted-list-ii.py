#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (44.31%)
# Likes:    5667
# Dislikes: 165
# Total Accepted:    485.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
#
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if None is head:
            return None
        if None is head.next:
            return head

        r_dummy = ListNode(head.val-1, None)
        cur_r = r_dummy
        cur = head
        val = head.val
        duplicated = False
        while None is not cur.next:
            if cur.next.val == val:
                cur = cur.next
                duplicated = True
                continue
            if False is duplicated:
                cur_r.next = ListNode(val, None)
                cur_r = cur_r.next
            else:
                duplicated = False
            cur = cur.next
            val = cur.val
        if False is duplicated:
            cur_r.next = ListNode(val, None)
        return r_dummy.next
# @lc code=end
