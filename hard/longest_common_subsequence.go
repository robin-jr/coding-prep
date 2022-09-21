package main

import "fmt"

var longestSS string = ""

func h(s1, s2 []rune, s string, i, j int) {
	if len(s) > len(longestSS) {
		longestSS = s
	}
	if i >= len(s1) || j >= len(s2) {
		return
	}
	for j := j; j < len(s2); j++ {
		for i := i; i < len(s1); i++ {
			if s2[j] == s1[i] {
				h(s1, s2, s+string(s2[j]), i+1, j+1)
				break
			}
		}
	}
	h(s1, s2, s, i+1, j+1)
}

// O(nm*min(n, m)) time | O(nm*min(n, m)) space
func LongestCommonSubsequence(s1 string, s2 string) []byte {
	// Write your code here.
	h([]rune(s1), []rune(s2), "", 0, 0)
	fmt.Println(longestSS)
	return []byte(longestSS)
}

func main() {
	s1, s2 := "ZXVVYZW", "XKYKZPW"
	x := LongestCommonSubsequence(s1, s2)
	fmt.Println(x)
}
