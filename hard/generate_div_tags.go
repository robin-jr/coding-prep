package main

import "fmt"

func solve(no_opens, no_close, n int, curr string) []string {
	fmt.Println(curr, n, no_opens, no_close)
	r := []string{}
	if no_close+1 == no_opens && no_opens == n {
		r = append(r, curr+"</div>")
	}
	if no_opens < n {
		r = append(r, solve(no_opens+1, no_close, n, curr+"<div>")...)
	}
	if no_close < no_opens {
		r = append(r, solve(no_opens, no_close+1, n, curr+"</div>")...)
	}
	return r
}

func GenerateDivTags(numberOfTags int) []string {
	return solve(0, 0, numberOfTags, "")
}

func main() {
	x := GenerateDivTags(3)
	fmt.Println(x)
}
