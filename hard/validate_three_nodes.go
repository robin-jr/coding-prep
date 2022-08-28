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

func oneHasThree(root *BST, mid *BST, last *BST, isMidFound bool) bool {
	if root == nil {
		return false
	}
	if root.Value == mid.Value {
		isMidFound = true
	}
	if root.Value == last.Value {
		return isMidFound
	}
	if root.Value < last.Value {
		return oneHasThree(root.Right, mid, last, isMidFound)
	}
	return oneHasThree(root.Left, mid, last, isMidFound)
}

func ValidateThreeNodes1(nodeOne *BST, nodeTwo *BST, nodeThree *BST) bool {
	return oneHasThree(nodeOne, nodeTwo, nodeThree, false) || oneHasThree(nodeThree, nodeTwo, nodeOne, false)
}
