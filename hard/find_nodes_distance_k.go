package main

// This is an input class. Do not edit.
type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

func FindNodesDistanceK(tree *BinaryTree, target int, k int) []int {
	ans := []int{}
	getDistanceFromTargetNode(tree, target, k, &ans)
	return ans
}

func getDistanceFromTargetNode(tree *BinaryTree, target int, k int, ans *[]int) int {
	if tree == nil {
		return -1
	}
	if tree.Value == target {
		addNodesAtDistanceK(tree, 0, k, ans)
		return 1
	}

	distanceFromLeft := getDistanceFromTargetNode(tree.Left, target, k, ans)
	distanceFromRight := getDistanceFromTargetNode(tree.Right, target, k, ans)

	if distanceFromLeft == k || distanceFromRight == k {
		*ans = append(*ans, tree.Value)
		return -1
	}

	if distanceFromLeft != -1 {
		addNodesAtDistanceK(tree.Right, distanceFromLeft+1, k, ans)
		return distanceFromLeft + 1
	}
	if distanceFromRight != -1 {
		addNodesAtDistanceK(tree.Left, distanceFromRight+1, k, ans)
		return distanceFromRight + 1
	}
	return -1
}

func addNodesAtDistanceK(tree *BinaryTree, curr_distance int, k int, res *[]int) {
	if tree == nil {
		return
	}
	if curr_distance == k {
		*res = append(*res, tree.Value)
		return
	}
	addNodesAtDistanceK(tree.Left, curr_distance+1, k, res)
	addNodesAtDistanceK(tree.Right, curr_distance+1, k, res)
}
