package main

import (
	"container/heap"
	"sort"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func LaptopRentals(times [][]int) int {
	sort.Slice(times, func(i, j int) bool { return times[i][0] < times[j][0] })
	h := &IntHeap{}
	heap.Init(h)
	count := 0
	for _, e := range times {
		if len(*h) > 0 && (*h)[0] <= e[0] {
			heap.Pop(h)
		} else {
			count += 1
		}
		heap.Push(h, e[1])
	}
	return count
}
