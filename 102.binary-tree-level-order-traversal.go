/*
 * @lc app=leetcode id=102 lang=golang
 *
 * [102] Binary Tree Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (63.23%)
 * Likes:    11388
 * Dislikes: 214
 * Total Accepted:    1.6M
 * Total Submissions: 2.5M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return the level order traversal of its
 * nodes' values. (i.e., from left to right, level by level).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3],[9,20],[15,7]]
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1]
 * Output: [[1]]
 *
 *
 * Example 3:
 *
 *
 * Input: root = []
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 2000].
 * -1000 <= Node.val <= 1000
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
func levelOrder(root *TreeNode) [][]int {
	var ret [][]int
	if nil == root {
		return ret
	}

	ret = append(ret, []int{root.Val})
	var nodeQueue []*TreeNode
	nodeQueue = append(nodeQueue, root)

	for curQueue := nodeQueue; len(curQueue) > 0; {
		var nextQueue []*TreeNode
		var nextRet []int
		for _, curNode := range curQueue {
			if nil != curNode.Left {
				nextQueue = append(nextQueue, curNode.Left)
				nextRet = append(nextRet, curNode.Left.Val)
			}
			if nil != curNode.Right {
				nextQueue = append(nextQueue, curNode.Right)
				nextRet = append(nextRet, curNode.Right.Val)
			}
		}
		if len(nextRet) > 0 {
			ret = append(ret, nextRet)
		}
		curQueue = nextQueue
	}

	return ret
}

// @lc code=end
