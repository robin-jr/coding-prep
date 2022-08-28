package main

// This is an input class. Do not edit.
type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func rootHasChild(root *BST, child *BST) bool {
	if root == nil {
		return false
	}
	if root.Value == child.Value {
		return true
	}
	if root.Value < child.Value {
		return rootHasChild(root.Right, child)
	}
	return rootHasChild(root.Left, child)
}

func ValidateThreeNodes(nodeOne *BST, nodeTwo *BST, nodeThree *BST) bool {
	if rootHasChild(nodeOne, nodeTwo) {
		return rootHasChild(nodeTwo, nodeThree)
	} else if rootHasChild(nodeThree, nodeTwo) {
		return rootHasChild(nodeTwo, nodeOne)
	}
	return false
}
