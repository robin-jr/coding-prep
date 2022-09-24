package main

func isPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}
func palindromePairs(words []string) [][]int {
	pairs := [][]int{}
	for i := 0; i < len(words)-1; i++ {
		for j := i + 1; j < len(words); j++ {
			if isPalindrome(words[i] + words[j]) {
				pairs = append(pairs, []int{i, j})
			}
			if isPalindrome(words[j] + words[i]) {
				pairs = append(pairs, []int{j, i})
			}
		}
	}
	return pairs
}
