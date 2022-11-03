/*
 * @lc app=leetcode id=98 lang=golang
 *
 * [98] Validate Binary Search Tree
 *
 * https://leetcode.com/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (31.71%)
 * Likes:    12989
 * Dislikes: 1045
 * Total Accepted:    1.7M
 * Total Submissions: 5.5M
 * Testcase Example:  '[2,1,3]'
 *
 * Given the root of a binary tree, determine if it is a valid binary search
 * tree (BST).
 *
 * A valid BST is defined as follows:
 *
 *
 * The left subtree of a node contains only nodes with keys less than the
 * node's key.
 * The right subtree of a node contains only nodes with keys greater than the
 * node's key.
 * Both the left and right subtrees must also be binary search trees.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: root = [2,1,3]
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: root = [5,1,4,null,null,3,6]
 * Output: false
 * Explanation: The root node's value is 5 but its right child's value is
 * 4.
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 10^4].
 * -2^31 <= Node.val <= 2^31 - 1
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
const (
	MaxInt32 = int(^uint32(0) >> 1)
	MinInt32 = -MaxInt32 - 1
)

func isValidSubtree(node *TreeNode, upper int, lower int) bool {
	if nil == node {
		return true
	}
	if upper < node.Val || lower > node.Val {
		return false
	}
	if !isValidSubtree(node.Left, node.Val-1, lower) ||
		!isValidSubtree(node.Right, upper, node.Val+1) {
		return false
	}
	return true
}

func isValidBST(root *TreeNode) bool {
	if nil == root {
		return true
	}
	return isValidSubtree(root, MaxInt32, MinInt32)
}

// @lc code=end
