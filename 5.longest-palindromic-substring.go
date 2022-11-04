/*
 * @lc app=leetcode id=5 lang=golang
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (32.40%)
 * Likes:    22402
 * Dislikes: 1292
 * Total Accepted:    2.2M
 * Total Submissions: 6.7M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, return the longest palindromic substring in s.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "babad"
 * Output: "bab"
 * Explanation: "aba" is also a valid answer.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "cbbd"
 * Output: "bb"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 1000
 * s consist of only digits and English letters.
 *
 *
 */

// @lc code=start
func longestPalindrome(s string) string {
	if 1 == len(s) {
		return s
	}

	maxDistance, maxStart := 0, 0
	dp := make([][]bool, len(s))
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]bool, len(s))
		dp[i][i] = true
		if i+1 < len(s) {
			if s[i] == s[i+1] {
				dp[i][i+1] = true
				if maxDistance == 0 {
					maxDistance, maxStart = 1, i
				}
			} else {
				dp[i][i+1] = false
			}
		}
	}

	for distance := 2; distance < len(s); distance++ {
		for i := 0; i < len(s); i++ {
			if i+distance >= len(s) {
				continue
			}
			if s[i] == s[i+distance] && dp[i+1][i+distance-1] == true {
				dp[i][i+distance] = true
				if distance > maxDistance {
					maxDistance, maxStart = distance, i
				}
			} else {
				dp[i][i+distance] = false
			}
		}
	}

	return s[maxStart : maxStart+maxDistance+1]
}

// @lc code=end
