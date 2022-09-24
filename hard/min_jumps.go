package main

import (
	"fmt"
)

type e struct {
	value int
	index int
}

func MinNumberOfJumps0(array []int) int {
	count := 0
	for i := 0; i < len(array)-1; {
		h := e{0, 0}
		j := i + 1
		for ; j < len(array) && j <= i+array[i]; j++ {
			if h.value < array[j] {
				h = e{array[j], j}
			}
		}
		j--
		count += 1
		if j == len(array)-1 {
			break
		} else if h.value+h.index > array[j]+j {
			i = h.index
		} else {
			i = j
		}
	}
	return count
}

func MinNumberOfJumps(array []int) int {
	jumps := 0
	maxReach := array[0]
	steps := maxReach
	for i := 1; i < len(array); i++ {
		if i == len(array)-1 {
			return jumps + 1
		}
		maxReach = max(maxReach, array[i]+i)
		steps -= 1
		if steps == 0 {
			steps = maxReach - i
			jumps += 1
		}
	}
	return jumps
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func main() {
	// array := []int{3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3}
	// array := []int{3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1}
	array := []int{2, 1, 2, 3, 1}
	x := MinNumberOfJumps(array)
	fmt.Println(x)
}
