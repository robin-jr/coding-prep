package main

import (
	"fmt"
	"math"
)

func DijkstrasAlgorithm(start int, edges [][][]int) []int {
	distances := make([]int, len(edges))
	for i := 0; i < len(edges); i++ {
		distances[i] = math.MaxInt32
	}
	distances[start] = 0

	visited := make(map[int]bool)
	for len(visited) < len(edges) {
		currNode := getNearestUnVisitedNode(&visited, distances)
		visited[currNode] = true     // mark as visited
		neighbors := edges[currNode] // get neighbors
		for _, neighbor := range neighbors {
			idx, weight := neighbor[0], neighbor[1]
			distances[idx] = min(distances[currNode]+weight, distances[idx])
		}
	}
	for i, v := range distances {
		if v == math.MaxInt32 {
			distances[i] = -1
		}
	}
	return distances
}
func getNearestUnVisitedNode(visited *map[int]bool, distances []int) int {
	m := math.MaxInt32 + 1
	idx := -1
	for i, v := range distances {
		if v < m && !(*visited)[i] {
			m = v
			idx = i
		}
	}
	return idx
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	edges := [][][]int{
		{
			{1, 7},
		},
		{
			{2, 6},
			{3, 20},
			{4, 3},
		},
		{
			{3, 14},
		},
		{
			{4, 2},
		},
		{},
		{},
	}
	x := DijkstrasAlgorithm(0, edges)
	fmt.Println(x)
}
