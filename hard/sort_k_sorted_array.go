package main

import (
	"container/heap"
	"fmt"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func SortKSortedArray(array []int, k int) []int {
	h := &IntHeap{}
	heap.Init(h)
	r := []int{}
	for _, e := range array {
		heap.Push(h, e)
		if len(*h) > k {
			r = append(r, heap.Pop(h).(int))
		}
	}
	for len(*h) > 0 {
		r = append(r, heap.Pop(h).(int))
	}
	return r
}

func main() {
	array := []int{3, 2, 1, 5, 4, 7, 6, 5}
	k := 3
	x := SortKSortedArray(array, k)
	fmt.Println(x)
}
