package main

import (
	"strings"
)

func day11pt1() {
	input := ReadFromFile("day11.txt")

	newArrangement := make([]string, len(input))
	changed := true
	for changed {
		changed = false
		for row, line := range input {
			newArrangement[row] = ""
			for col, seat := range []rune(line) {
				switch seat {
				case '.':
					newArrangement[row] += "."
				case 'L':
					//change this to getAmountOfFull1 for pt 1
					if getAmountOfFull2(input, row, col) == 0 {
						newArrangement[row] += "#"
						changed = true
					} else {
						newArrangement[row] += "L"
					}

				case '#':
					//change this to getAmountOfFull1 and >=4 for pt 1
					if getAmountOfFull2(input, row, col) >= 5 {
						newArrangement[row] += "L"
						changed = true
					} else {
						newArrangement[row] += "#"
					}
				}
			}
		}
		input = make([]string, len(newArrangement))
		copy(input, newArrangement)
	}
	count := 0
	for _, row := range newArrangement {
		count += strings.Count(row, "#")
	}
	println(count)
}

func getAmountOfFull1(arr []string, row int, col int) int {
	count := 0
	for r := row - 1; r <= row+1; r++ {
		for c := col - 1; c <= col+1; c++ {
			if r >= 0 && c >= 0 && r < len(arr) && c < len(arr[0]) {
				if arr[r][c] == "#"[0] && !(r == row && c == col) {
					count++
				}
			}
		}
	}
	return count
}

func getAmountOfFull2(arr []string, row int, col int) int {
	count := 0
	for r := -1; r <= 1; r++ {
		for c := -1; c <= 1; c++ {
			count += checkSeat(arr, row, col, r, c)
		}
	}
	return count
}
func checkSeat(arr []string, row int, col int, r int, c int) int {
	if r+row >= 0 && c+col >= 0 && r+row < len(arr) && c+col < len(arr[0]) && !(r == 0 && c == 0) {
		switch arr[r+row][c+col] {
		case "#"[0]:
			return 1
		case "L"[0]:
			return 0
		case "."[0]:
			if r > 0 {
				r++
			} else if r < 0 {
				r--
			}
			if c > 0 {
				c++
			} else if c < 0 {
				c--
			}
			return checkSeat(arr, row, col, r, c)
		}
	}
	return 0
}
