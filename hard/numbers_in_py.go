package main

import (
	"fmt"
	"math"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minSpaces(s string, favs *map[string]bool, cache *map[string]int) int {
	if m, ok := (*cache)[s]; ok {
		return m
	}

	if (*favs)[s] {
		return 0
	}
	m := math.MaxInt32
	for i := 1; i < len(s); i++ {
		e := s[:i]
		if (*favs)[e] {
			t := minSpaces(s[i:], favs, cache) + 1
			m = min(t, m)
		}
	}
	(*cache)[s] = m
	return m
}

func NumbersInPi(pi string, numbers []string) int {
	favs := make(map[string]bool)
	for _, v := range numbers {
		favs[v] = true
	}
	cache := make(map[string]int)
	m := minSpaces(pi, &favs, &cache)
	if m == math.MaxInt32 {
		return -1
	}
	return m
}

func main() {
	pi := "3141592653589793238462643383279"
	numbers := []string{"314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"}
	// pi = "3141592"
	// numbers = []string{"3141", "5", "31", "2", "4159", "9", "42"}
	// numbers = []string{"3", "141", "592", "65", "55", "35", "8", "9793", "23846264", "383279"}
	// pi = "3141592653589793238462643383279"
	x := NumbersInPi(pi, numbers)
	fmt.Println(x)
}
