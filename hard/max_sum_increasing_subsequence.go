package main

import "math"

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
