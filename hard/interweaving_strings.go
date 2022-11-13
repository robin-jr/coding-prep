package main

import "fmt"

func InterweavingStrings1(one, two, three string) bool {
	if len(three) == 0 {
		return len(one) == 0 && len(two) == 0
	}
	if len(one) > 0 && len(two) > 0 && three[0] == one[0] && three[0] == two[0] {
		return InterweavingStrings(one[1:], two, three[1:]) || InterweavingStrings(one, two[1:], three[1:])
	}
	if len(one) > 0 && three[0] == one[0] {
		return InterweavingStrings(one[1:], two, three[1:])
	}
	if len(two) > 0 && three[0] == two[0] {
		return InterweavingStrings(one, two[1:], three[1:])
	}
	return false
}
func prin(arr [][]bool) {
	for _, e := range arr {
		fmt.Println(e)
	}
}

func InterweavingStrings(one, two, three string) bool {
	if len(one)+len(two) != len(three) {
		return false
	}
	dp := make([][]bool, len(one)+1)
	for i := range dp {
		dp[i] = make([]bool, len(two)+1)
	}
	for i := 0; i < len(one)+1; i++ {
		for j := 0; j < len(two)+1; j++ {
			if i == 0 && j == 0 {
				dp[i][j] = true
			} else if i == 0 {
				dp[i][j] = dp[i][j-1] && two[j-1] == three[i+j-1]
			} else if j == 0 {
				dp[i][j] = dp[i-1][j] && one[i-1] == three[i+j-1]
			} else {
				dp[i][j] = (dp[i-1][j] && one[i-1] == three[i+j-1]) || (dp[i][j-1] && two[j-1] == three[i+j-1])
			}
		}
	}
	prin(dp)
	return dp[len(one)][len(two)]
}

func main() {
	one := "aabcc"
	two := "dbbca"
	three := "aadbbcbcac"
	x := InterweavingStrings(one, two, three)
	fmt.Println(x)
}
