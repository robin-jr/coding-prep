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
func LongestCommonSubsequence0(s1 string, s2 string) []byte {
	// Write your code here.
	h([]rune(s1), []rune(s2), "", 0, 0)
	fmt.Println(longestSS)
	return []byte(longestSS)
}

func getMaxLengthString(s1 string, s2 string) string {
	if len(s1) == len(s2) {
		return s1
	}
	if len(s1) > len(s2) {
		return s1
	}
	return s2
}

func LongestCommonSubsequence(s1 string, s2 string) []byte {
	d := make([][]string, len(s1)+1)

	for i := range d {
		d[i] = make([]string, len(s2)+1)
	}

	for i := 1; i < len(s1)+1; i++ {
		for j := 1; j < len(s2)+1; j++ {
			if s1[i-1] == s2[j-1] {
				d[i][j] = d[i-1][j-1] + string(s1[i-1])
			} else {
				d[i][j] = getMaxLengthString(d[i-1][j], d[i][j-1])
			}
		}
	}

	return []byte(d[len(s1)][len(s2)])
}

func main() {
	s1, s2 := "ZXVVYZW", "XKYKZPW"
	x := LongestCommonSubsequence(s1, s2)
	fmt.Println(x)
}
