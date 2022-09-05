package main

import (
	"fmt"
	"math"
)

var maxSum int
var maxes []int

func MaxSumIncreasingSubsequence(array []int) (int, []int) {
	maxSum = -1
	maxes = []int{-1}
	for i := 0; i < len(array); i += 1 {
		alg(array, i, array[i], []int{array[i]})
	}
	return maxSum, maxes
}

func alg(array []int, start int, sumFar int, res []int) {
	max := math.MaxInt
	for i := start + 1; i < len(array); i += 1 {
		if array[i] > array[start] && array[i] < max {
			alg(array, i, sumFar+array[i], append(res, array[i]))
			max = array[i]
		}
	}
	if sumFar > maxSum {
		maxSum = sumFar
		maxes = res
	}
}

type E struct {
	value, previousI int
}

func (e E) String() string {
	return fmt.Sprintf("%v %v\n", e.value, e.previousI)
}
func MaxSumIncreasingSubsequence1(array []int) (int, []int) {
	maxesSoFar := []E{{array[0], -1}}
	maxSumIndex := 0
	for i := 1; i < len(array); i += 1 {
		curr_max := E{array[i], i}
		for j := i - 1; j >= 0; j -= 1 {
			if array[j] < array[i] && array[i]+maxesSoFar[j].value > curr_max.value {
				curr_max = E{array[i] + maxesSoFar[j].value, j}
			}
		}
		maxesSoFar = append(maxesSoFar, curr_max)

		if maxesSoFar[i].value > maxesSoFar[maxSumIndex].value {
			maxSumIndex = i
		}
	}

	res := []int{array[maxSumIndex]}
	for i := maxSumIndex; i != -1 && i != maxesSoFar[i].previousI; {
		i = maxesSoFar[i].previousI
		if i == -1 {
			break
		}
		res = append(res, array[i])
	}

	// reversing
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}

	return maxesSoFar[maxSumIndex].value, res
}

func main() {
	array := []int{10, 70, 20, 30, 50, 11, 30, 5}
	x, y := MaxSumIncreasingSubsequence1(array)
	fmt.Println(x, y)
}
