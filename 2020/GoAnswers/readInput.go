package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

var path string

func ReadFromFileNums(fileName string) []int {
	file, err := os.Open(path + fileName)

	if err != nil {
		log.Fatalf("failed to open")
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var text []int
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		text = append(text, num)
	}
	file.Close()
	return text
}

func ReadFromFile(fileName string) []string {
	file, err := os.Open(path + fileName)

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

func main() {
	path = "D:\\Aharon\\git\\AdventOfCode\\2020\\InputTxt\\"
	day11pt1()
}
