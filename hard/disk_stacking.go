package main

import (
	"fmt"
	"sort"
)

func map2[A any, B any](a []A, f func(A) B) []B {
	t := make([]B, len(a))
	for i, v := range a {
		t[i] = f(v)
	}
	return t
}

func canStack(a, b []int) bool {
	if a[0] < b[0] && a[1] < b[1] && a[2] < b[2] {
		return true
	}
	return false
}

func DiskStacking(disks [][]int) [][]int {
	sort.Slice(disks, func(i, j int) bool {
		return disks[i][2] < disks[j][2] // sorting by height
	})
	max_heights := map2(disks, func(i []int) int { return i[2] })
	parents := map2(disks, func(i []int) int { return -1 })
	maxHeightIndex := 0
	for i := 1; i < len(max_heights); i++ {
		t := max_heights[i]
		for j := 0; j < i; j++ {
			if max_heights[j]+t > max_heights[i] && canStack(disks[j], disks[i]) {
				max_heights[i] = max_heights[j] + t
				parents[i] = j
			}
		}
		if max_heights[maxHeightIndex] < max_heights[i] {
			maxHeightIndex = i
		}
	}
	r := [][]int{}
	r = append(r, disks[maxHeightIndex])
	t := parents[maxHeightIndex]
	for t != -1 {
		r = append(r, disks[t])
		t = parents[t]
	}
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return r
}

func main() {
	disks := [][]int{
		{2, 1, 2},
		{3, 2, 3},
		{2, 2, 8},
		{2, 3, 4},
		{1, 3, 1},
		{4, 4, 5},
	}
	x := DiskStacking(disks)
	fmt.Println(x)
}
