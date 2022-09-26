package main

import "fmt"

type sack struct {
	value   int
	indices []int
}

func canAddToSack(s sack, i int) bool {
	for _, j := range s.indices {
		if j == i {
			return false
		}
	}
	return true
}
func addToSack(s sack, i int, value int) sack {
	s.indices = append(s.indices, i)
	s.value += value
	return s
}

func max(a, b sack) sack {
	if a.value > b.value {
		return a
	}
	return b
}

func KnapsackProblem(items [][]int, capacity int) []interface{} {
	d := make([]sack, capacity+1)
	d[0] = sack{0, []int{}}
	for curr_cap := 1; curr_cap < capacity+1; curr_cap++ {
		maxItem := d[curr_cap-1]
		for idx, item := range items {
			diff := curr_cap - item[1]
			if diff >= 0 && canAddToSack(d[diff], idx) {
				maxItem = max(maxItem, addToSack(d[diff], idx, item[0]))
			}
		}
		d[curr_cap] = maxItem
	}

	return []interface{}{d[capacity].value, d[capacity].indices}
}
func main() {
	items := [][]int{
		{1, 2},
		{4, 3},
		{5, 6},
		{6, 7},
	}
	x := KnapsackProblem(items, 10)
	fmt.Println(x)
}
