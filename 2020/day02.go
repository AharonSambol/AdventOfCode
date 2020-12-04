package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)


func part1() {
	input := readFromFile("day02.txt")
	count := 0
	r := regexp.MustCompile(":?[-\\s]")
	for _, line := range input {
		//splits the string by the regex (i know this is bad)
		lineArr := strings.Split(r.ReplaceAllString(line, ","), ",")
		num1, err1 := strconv.Atoi(lineArr[0]) //turn to int
		num2, err2 := strconv.Atoi(lineArr[1]) //turn to int
		if err1 != nil || err2 != nil {
			log.Fatalf("char isnt number")
		}
		//count how many times the char appears in the string
		aomuntOfAcurenses := strings.Count(lineArr[3], lineArr[2])

		if aomuntOfAcurenses >= num1 && aomuntOfAcurenses <= num2 {
			count++
		}
	}
	print(count)
}
func part2() {
	input := readFromFile("day02.txt")
	count := 0
	r := regexp.MustCompile(":?[-\\s]")
	for _, line := range input {
		//splits the string by the regex (i know this is bad)
		lineArr := strings.Split(r.ReplaceAllString(line, ","), ",")
		num1, err1 := strconv.Atoi(lineArr[0]) //turn to int
		num2, err2 := strconv.Atoi(lineArr[1]) //turn to int
		if err1 != nil || err2 != nil {
			log.Fatalf("char isnt number")
		}

		lineR := []rune(lineArr[3]) // turn the line of characters into an array of characters
		//check that theyre different and one of them equals the wanted character
		if strings.Count(string(lineR[num1-1])+string(lineR[num2-1]), lineArr[2]) == 1 {
			count++
		}
	}
	print(count)
}
