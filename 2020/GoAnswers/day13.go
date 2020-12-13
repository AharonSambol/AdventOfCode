package main

import (
	"strconv"
	"strings"
)

func day13pt1() {
	input := ReadFromFile("day13.txt")
	time, _ := strconv.Atoi(input[0])
	println(time)
	split := strings.Split(input[1], ",")
	for i := 0; i < len(split); i++ {
		if split[i] == "x" {
			split = remove(split, i)
			i--
		}
	}
	fastest, _ := strconv.Atoi(split[0])

	for _, busSt := range split {
		bus, _ := strconv.Atoi(busSt)
		if bus-time%bus < fastest-time%fastest {
			fastest = bus
		}
	}
	println(fastest * (fastest - time%fastest))
}
func remove(slice []string, s int) []string {
	return append(slice[:s], slice[s+1:]...)
}
