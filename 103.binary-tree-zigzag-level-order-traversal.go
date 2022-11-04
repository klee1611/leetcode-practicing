/*
 * @lc app=leetcode id=103 lang=golang
 *
 * [103] Binary Tree Zigzag Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (55.11%)
 * Likes:    7562
 * Dislikes: 202
 * Total Accepted:    828.1K
 * Total Submissions: 1.5M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return the zigzag level order traversal of
 * its nodes' values. (i.e., from left to right, then right to left for the
 * next level and alternate between).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3],[20,9],[15,7]]
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
 * -100 <= Node.val <= 100
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
func zigzagLevelOrder(root *TreeNode) [][]int {
	var ret [][]int
	if nil == root {
		return ret
	}

	nodeQueue, j := []*TreeNode{root}, 0
	for curQueue := nodeQueue; len(curQueue) > 0; {
		var nextQueue []*TreeNode
		nextRet := make([]int, len(curQueue))
		for i, node := range curQueue {
			var index int
			if j%2 == 0 {
				index = i
			} else {
				index = len(curQueue) - i - 1
			}
			nextRet[index] = node.Val
			if nil != node.Left {
				nextQueue = append(nextQueue, node.Left)
			}
			if nil != node.Right {
				nextQueue = append(nextQueue, node.Right)
			}
		}
		j++
		ret = append(ret, nextRet)
		curQueue = nextQueue
	}

	return ret
}

// @lc code=end
