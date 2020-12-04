package main

import (
	"bufio"
	"log"
	"os"
)

func main() {
	day3part2()
}
func readFromFile(fileName string) []string {
	file, err := os.Open(fileName)

	if err != nil {
		log.Fatalf("failed to open")
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var text []string
	for scanner.Scan() {
		text = append(text, scanner.Text())
	}
	file.Close()
	return text
}
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
