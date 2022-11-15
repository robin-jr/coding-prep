package main

import "fmt"

func prin(arr [][]int) {
	for _, e := range arr {
		fmt.Println(e)
	}
}
func isValid(board *[][]int, i, j, num int) bool {
	for col := 0; col < 9; col++ {
		if (*board)[i][col] == num {
			return false
		}
	}
	for row := 0; row < 9; row++ {
		if (*board)[row][j] == num {
			return false
		}
	}
	iMin, jMin := 3*(i/3), 3*(j/3)
	for i := iMin; i < iMin+3; i++ {
		for j := jMin; j < jMin+3; j++ {
			if (*board)[i][j] == num {
				return false
			}
		}
	}
	return true
}

func solve(board *[][]int) bool {
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if (*board)[i][j] == 0 {
				for num := 1; num <= 9; num++ {
					if isValid(board, i, j, num) {
						(*board)[i][j] = num
						isCorrectAssignment := solve(board)
						if isCorrectAssignment {
							return true
						}
						(*board)[i][j] = 0
					}
				}
				return false
			}
		}
	}
	return true
}

func SolveSudoku(board [][]int) [][]int {
	solve(&board)
	return board
}

func main() {
	arr := [][]int{
		{7, 8, 0, 4, 0, 0, 1, 2, 0},
		{6, 0, 0, 0, 7, 5, 0, 0, 9},
		{0, 0, 0, 6, 0, 1, 0, 7, 8},
		{0, 0, 7, 0, 4, 0, 2, 6, 0},
		{0, 0, 1, 0, 5, 0, 9, 3, 0},
		{9, 0, 4, 0, 6, 0, 0, 0, 5},
		{0, 7, 0, 3, 0, 0, 0, 1, 2},
		{1, 2, 0, 0, 0, 7, 4, 0, 0},
		{0, 4, 9, 2, 0, 6, 0, 0, 7},
	}
	x := SolveSudoku(arr)
	fmt.Println(x)
}
