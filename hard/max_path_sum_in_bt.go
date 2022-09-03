package main

import (
	"fmt"
	"math"
)

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

var maxSoFar int

func max(nums ...int) int {
	t := nums[0]
	for _, e := range nums[1:] {
		if t < e {
			t = e
		}
	}
	return t
}

func getMax(tree *BinaryTree) int {
	if tree == nil {
		return 0
	}
	x, y := getMax(tree.Left), getMax(tree.Right)
	curr_max := tree.Value + max(x, y) //including only one child
	maxSoFar = max(curr_max, x+y+tree.Value, maxSoFar)
	return curr_max
}

func MaxPathSum(tree *BinaryTree) int {
	maxSoFar = math.MinInt
	getMax(tree)
	return maxSoFar
}

func main() {
	tree := &BinaryTree{1, &BinaryTree{2, nil, nil}, &BinaryTree{3, nil, nil}}
	x := MaxPathSum(tree)
	fmt.Println(x)
}
