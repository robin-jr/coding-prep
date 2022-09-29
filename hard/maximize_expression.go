package main

import (
	"fmt"
	"math"
)

func MaximizeExpression(array []int) int {
	if len(array) < 4 {
		return 0
	}
	A := make([]int, len(array))
	A[0] = array[0]

	for i := 1; i < len(array); i++ {
		A[i] = max(array[i], A[i-1])
	}

	B := make([]int, len(array))
	B[0] = math.MinInt
	for i := 1; i < len(array); i++ {
		B[i] = max(A[i-1]-array[i], B[i-1])
	}

	C := make([]int, len(array))
	C[1] = math.MinInt
	for i := 2; i < len(array); i++ {
		C[i] = max(B[i-1]+array[i], C[i-1])
	}

	D := make([]int, len(array))
	D[2] = math.MinInt
	for i := 3; i < len(array); i++ {
		D[i] = max(C[i-1]-array[i], D[i-1])
	}

	return D[len(array)-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	// array := []int{3, 6, 1, -3, 2, 7}
	array := []int{3, 9, 10, 1, 30, 40}
	x := MaximizeExpression(array)
	fmt.Println(x)
}
