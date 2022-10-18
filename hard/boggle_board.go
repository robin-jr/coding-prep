package main

import "fmt"

func BoggleBoard(board [][]rune, words []string) []string {
	t := Trie{make(map[rune]Trie), ""}
	for _, word := range words {
		t.addWord([]rune(word), word)
	}

	visiting := make([][]bool, len(board))
	for i := range visiting {
		visiting[i] = make([]bool, len(board[0]))
	}

	res := make(map[string]bool)

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			explore(i, j, &board, &visiting, &t, &res)
		}
	}
	keys := []string{}
	for k := range res {
		keys = append(keys, k)
	}
	return keys
}

func explore(i, j int, board *[][]rune, visiting *[][]bool, root *Trie, res *map[string]bool) {
	e := (*board)[i][j]
	t, ok := root.vals[e]
	if !ok || (*visiting)[i][j] {
		return
	}
	if t, ok := t.vals['*']; ok {
		(*res)[t.word] = true
	}
	(*visiting)[i][j] = true
	neighbors := getNeighbors(i, j, board)
	for _, e := range neighbors {
		explore(e[0], e[1], board, visiting, &t, res)
	}
	(*visiting)[i][j] = false
}

func getNeighbors(i, j int, board *[][]rune) [][]int {
	res := [][]int{}
	iMax := len(*board)
	jMax := len((*board)[0])
	if i+1 < iMax {
		res = append(res, []int{i + 1, j})
	}
	if j+1 < jMax {
		res = append(res, []int{i, j + 1})
	}
	if i-1 >= 0 {
		res = append(res, []int{i - 1, j})
	}
	if j-1 >= 0 {
		res = append(res, []int{i, j - 1})
	}
	if i-1 >= 0 && j-1 >= 0 {
		res = append(res, []int{i - 1, j - 1})
	}
	if i+1 < iMax && j+1 < jMax {
		res = append(res, []int{i + 1, j + 1})
	}
	if i-1 >= 0 && j+1 < jMax {
		res = append(res, []int{i - 1, j + 1})
	}
	if i+1 < iMax && j-1 >= 0 {
		res = append(res, []int{i + 1, j - 1})
	}
	return res
}

type Trie struct {
	vals map[rune]Trie
	word string
}

func (t *Trie) addWord(word []rune, s string) {
	for _, letter := range word {
		if child, ok := t.vals[letter]; ok {
			t = &child
		} else {
			z := Trie{make(map[rune]Trie), ""}
			t.vals[letter] = z
			t = &z
		}
	}
	t.vals['*'] = Trie{word: s}
}

func main() {
	words := []string{"this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"}
	board := [][]rune{
		{'t', 'h', 'i', 's', 'i', 's', 'a'},
		{'s', 'i', 'm', 'p', 'l', 'e', 'x'},
		{'b', 'x', 'x', 'x', 'x', 'e', 'b'},
		{'x', 'o', 'g', 'g', 'l', 'x', 'o'},
		{'x', 'x', 'x', 'D', 'T', 'r', 'a'},
		{'R', 'E', 'P', 'E', 'A', 'd', 'x'},
		{'x', 'x', 'x', 'x', 'x', 'x', 'x'},
		{'N', 'O', 'T', 'R', 'E', '-', 'P'},
		{'x', 'x', 'D', 'E', 'T', 'A', 'E'},
	}
	x := BoggleBoard(board, words)
	fmt.Println(x)
}
