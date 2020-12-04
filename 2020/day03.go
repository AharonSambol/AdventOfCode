package main

import (
	"bufio"
	"log"
	"os"
)



func day3part1(rowSkip int, colSkip int) int {
	// row and col in question one are 1 and 3
	input := readFromFile("day03.txt")
	count := 0
	pos := 0
	for i, row := range input {
		if i == 0 || (i+1)%rowSkip != 0 {
			continue
		}
		pos += colSkip
		pos %= len(row)
		if row[pos] == '#' {
			count++
		}
	}
	return count
}

func day3part2() {
	print(day3part1(1, 1) * day3part1(1, 3) * day3part1(1, 5) * day3part1(1, 7) * day3part1(2, 1))
}
