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

func findParents(tree *BinaryTree, parent *BinaryTree, parents *map[int]*BinaryTree) {
	if tree == nil {
		return
	}
	(*parents)[tree.Value] = parent
	findParents(tree.Left, tree, parents)
	findParents(tree.Right, tree, parents)
}

func getTargetNode(target int, parents map[int]*BinaryTree) *BinaryTree {
	parent := parents[target]
	if parent == nil {
		return nil
	}
	if parent.Left != nil && parent.Left.Value == target {
		return parent.Left
	}
	return parent.Right
}

func FindNodesDistanceK1(tree *BinaryTree, target int, k int) []int {
	parents := map[int]*BinaryTree{}
	findParents(tree, nil, &parents)
	targetNode := getTargetNode(target, parents)
	if targetNode == nil {
		targetNode = tree
	}
	visited := map[int]bool{}

	q := []*BinaryTree{targetNode}
	curr_distance := 0
	for len(q) > 0 {
		if curr_distance == k {
			res := []int{}
			for _, e := range q {
				res = append(res, e.Value)
			}
			return res
		}
		temp := []*BinaryTree{}
		for _, e := range q {
			visited[e.Value] = true
			if e.Left != nil && !visited[e.Left.Value] {
				temp = append(temp, e.Left)
			}
			if e.Right != nil && !visited[e.Right.Value] {
				temp = append(temp, e.Right)
			}
			if parents[e.Value] != nil && !visited[parents[e.Value].Value] {
				temp = append(temp, parents[e.Value])
			}
		}
		q = temp
		curr_distance += 1
	}
	return []int{}
}
