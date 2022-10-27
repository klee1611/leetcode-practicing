#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (43.27%)
# Likes:    3183
# Dislikes: 651
# Total Accepted:    326.4K
# Total Submissions: 752.7K
# Testcase Example:  '"25525511135"'
#
# A valid IP address consists of exactly four integers separated by single
# dots. Each integer is between 0 and 255 (inclusive) and cannot have leading
# zeros.
#
#
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses.
#
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be formed by inserting dots into s. You are not allowed to
# reorder or remove any digits in s. You may return the valid IP addresses in
# any order.
#
#
# Example 1:
#
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#
#
# Example 2:
#
#
# Input: s = "0000"
# Output: ["0.0.0.0"]
#
#
# Example 3:
#
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# s consists of digits only.
#
#
#

# @lc code=start
class Solution:
    def helper(self, r: List[str], pre: str, s: str, seg: int) -> None:
        if len(s) < seg or len(s) > seg * 3:
            return
        if 1 == seg:
            if '0' == s[0] and len(s) > 1:
                return
            if 0 <= int(s) <= 255:
                r.append(pre + s)
            return
        self.helper(r, pre + s[0] + '.', s[1:], seg - 1)
        if s[0] == '0':
            return
        self.helper(r, pre + s[0:2] + '.', s[2:], seg - 1)
        if 100 <= int(s[0:3]) <= 255:
            self.helper(r, pre + s[0:3] + '.', s[3:], seg - 1)
        return

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        r = []
        self.helper(r, '', s, 4)
        return r
# @lc code=end
