/*
 * @lc app=leetcode id=22 lang=golang
 *
 * [22] Generate Parentheses
 *
 * https://leetcode.com/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (71.82%)
 * Likes:    15782
 * Dislikes: 606
 * Total Accepted:    1.2M
 * Total Submissions: 1.7M
 * Testcase Example:  '3'
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 *
 * Example 1:
 * Input: n = 3
 * Output: ["((()))","(()())","(())()","()(())","()()()"]
 * Example 2:
 * Input: n = 1
 * Output: ["()"]
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 8
 *
 *
 */

// @lc code=start
var res []string

func generate(left int, right int, cur string) {
	if left > right {
		return
	}
	if 0 == left {
		s := cur
		for i := 0; i < right; i++ {
			s += ")"
		}
		res = append(res, s)
		return
	}
	generate(left-1, right, cur+"(")
	generate(left, right-1, cur+")")
}

func generateParenthesis(n int) []string {
	if 1 == n {
		return []string{"()"}
	}

	res = nil
	generate(n-1, n, "(")
	return res
}

// @lc code=end
