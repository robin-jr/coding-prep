package main

import (
	"fmt"
	"math"
)

func get(a [][]int, i, j int) int {
	if i < 0 || j < 0 {
		return 0
	}
	return a[i][j]
}

func MaximumSumSubmatrix(matrix [][]int, size int) int {
	sums := make([][]int, len(matrix))
	for i := range matrix {
		sums[i] = make([]int, len(matrix[0]))
	}
	sums[0][0] = matrix[0][0]
	for i := 1; i < len(matrix[0]); i++ {
		sums[0][i] = sums[0][i-1] + matrix[0][i]
	}
	for i := 1; i < len(matrix); i++ {
		sums[i][0] = sums[i-1][0] + matrix[i][0]
	}
	for i := 1; i < len(matrix); i++ {
		for j := 1; j < len(matrix[0]); j++ {
			sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i][j]
		}
	}
	max_sum := math.MinInt

	for i := size - 1; i < len(matrix); i++ {
		for j := size - 1; j < len(matrix[0]); j++ {
			t := get(sums, i, j) - get(sums, i, j-size) - get(sums, i-size, j) + get(sums, i-size, j-size)
			max_sum = max(t, max_sum)
		}
	}
	return max_sum
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func main() {
	matrix := [][]int{
		{5, 3, -1, 5},
		{-7, 3, 7, 4},
		{12, 8, 0, 0},
		{1, -8, -8, 2},
	}
	matrix = [][]int{
		{-1, -2, -3, -4, -5},
		{1, 1, 1, 1, 1},
		{-1, -10, -10, -4, -5},
		{5, 5, 5, 5, 5},
		{-5, -4, -3, -10, -1},
	}
	x := MaximumSumSubmatrix(matrix, 2)
	fmt.Println(x)
}
