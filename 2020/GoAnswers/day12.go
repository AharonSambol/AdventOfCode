package main

import (
	"strconv"
)

func day12pt1() {
	input := ReadFromFile("day12.txt")
	north, east, pointingTo := 0, 0, 90
	for _, lineSt := range input {
		line := []rune(lineSt)
		num, _ := strconv.Atoi(string(line[1:]))
		switch line[0] {
		case 'N':
			north += num
		case 'E':
			east += num
		case 'W':
			east -= num
		case 'S':
			north -= num
		case 'F':
			switch pointingTo {
			case 0:
				north += num
			case 90:
				east += num
			case 180:
				north -= num
			case 270:
				east -= num
			}
		case 'R':
			pointingTo += num
			pointingTo %= 360
		case 'L':
			pointingTo -= num
			if pointingTo < 0 {
				pointingTo = 360 + pointingTo
			}
		}
	}
	println(Abs(north) + Abs(east))
}
func day12pt2() {
	input := ReadFromFile("day12.txt")
	north, east := 0, 0
	addToN, addToE := 1, 10
	for _, lineSt := range input {
		line := []rune(lineSt)
		num, _ := strconv.Atoi(string(line[1:]))
		switch line[0] {
		case 'N':
			addToN += num
		case 'E':
			addToE += num
		case 'W':
			addToE -= num
		case 'S':
			addToN -= num
		case 'F':
			for i := 0; i < num; i++ {
				north += addToN
				east += addToE
			}
		case 'R':
			for i := 0; i < num/90; i++ {
				temp := -addToE
				addToE = addToN
				addToN = temp
			}

		case 'L':
			for i := 0; i < num/90; i++ {
				temp := addToE
				addToE = -addToN
				addToN = temp
			}
		}
	}
	println(Abs(north) + Abs(east))
}
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
