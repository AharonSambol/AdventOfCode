package main

import (
	"bufio"
	"log"
	"os"
)

func ReadFromFile(fileName string) []string {
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
func day6pt1() {
	input := ReadFromFile("day06.txt")
	count := 0
	group := make(map[rune]int)
	for _, line := range input {
		if line == "" {
			for range group {
				count++
			}
			group = make(map[rune]int)
		} else {
			for _, ans := range line {
				group[ans] = 1
			}
		}
	}
	print(count)
}

func day6pt2() {
	input := ReadFromFile("day06.txt")
	count := 0
	amountOfPPl := 0
	group := make(map[rune]int)
	for _, line := range input {
		if line == "" {
			for k := range group {
				if group[k] == amountOfPPl {
					count++
				}
			}
			group = make(map[rune]int)
			amountOfPPl = 0
		} else {
			amountOfPPl++
			for _, ans := range line {
				group[ans] = group[ans] + 1
			}
		}
	}
	print(count)
}
