package main

import (
	"bufio"
	"log"
	"os"
)

var path string

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
	day8pt2()
}
