package main

import "fmt"

func WaterArea(heights []int) int {
	sum := 0
	for i, ch := range heights {
		leftMax := max(heights[:i]...)
		rightMax := max(heights[i+1:]...)
		t := min(leftMax, rightMax) - ch
		if t > 0 {
			sum += t
		}
	}
	return sum
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(args ...int) int {
	max := -1
	for _, e := range args {
		if max < e {
			max = e
		}
	}
	return max
}

func main() {
	// heights := []int{0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3}
	// heights := []int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8}
	heights := []int{0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0}
	x := WaterArea(heights)
	fmt.Println(x)
}
