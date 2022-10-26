#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (45.35%)
# Likes:    8159
# Dislikes: 358
# Total Accepted:    583.8K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None:
            return head
        if left == right:
            return head

        distance = right - left
        cur, prev_left, left_p, right_next = head, None, None, None
        for i in range(1, right+2):
            if None is cur:
                break
            if i + 1 == left:
                prev_left = cur
            if i == left:
                left_p = cur
            if i == right + 1:
                right_next = cur
            cur = cur.next

        prev, cur, rev_cur = right_next, left_p, None
        for i in range(distance+1):
            rev_cur = ListNode(cur.val, prev)
            prev = rev_cur
            cur = cur.next
        if left == 1:
            return rev_cur
        prev_left.next = rev_cur
        return head
# @lc code=end
