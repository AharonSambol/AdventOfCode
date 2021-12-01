package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func ReadFromFileNums(fileName string) []int {
	file, err := os.Open(fileName)

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

func main() {
	input := ReadFromFileNums("D:/Aharon/git/ajs-code/golang/pieces.text")
	//part 1
	prev := input[0]
	ans := 0
	for i := 1; i < len(input); i++ {
		if input[i] > prev {
			ans += 1
		}
		prev = input[i]
	}
	println(ans)
	//part 2
	prev = input[0] + input[1] + input[2]
	ans = 0
	for i := 1; i < len(input)-2; i++ {
		cur := input[i] + input[i+1] + input[i+2]
		if cur > prev {
			ans += 1
		}
		prev = cur
	}
	println(ans)

}
