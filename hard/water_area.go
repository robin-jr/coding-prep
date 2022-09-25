package main

import "fmt"

func WaterArea(heights []int) int {
	sum := 0
	if len(heights) == 0 {
		return 0
	}
	lms := getLeftMaxHeights(heights)
	rms := getRightMaxHeights(heights)
	for i, ch := range heights {
		t := min(lms[i], rms[i]) - ch
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

func getLeftMaxHeights(heights []int) []int {
	leftMaxHeights := make([]int, len(heights))
	max := heights[0]
	for i := 1; i < len(heights); i++ {
		leftMaxHeights[i] = max
		if heights[i] > max {
			max = heights[i]
		}
	}
	return leftMaxHeights
}
func getRightMaxHeights(heights []int) []int {
	rightMaxHeights := make([]int, len(heights))
	max := heights[len(heights)-1]
	for i := len(heights) - 2; i >= 0; i-- {
		rightMaxHeights[i] = max
		if heights[i] > max {
			max = heights[i]
		}
	}
	return rightMaxHeights
}

func main() {
	// heights := []int{0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3}
	// heights := []int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8}
	heights := []int{0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0}
	x := WaterArea(heights)
	fmt.Println(x)
}
