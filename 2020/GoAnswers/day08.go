package main

import (
	"os"
	"strconv"
	"strings"
)

func rec(m map[int]bool, line int, count int, input []string, partTwo bool, changed bool) {
	for {
		instruction := input[line]
		sp := strings.Split(instruction, " ")
		typ, valSt := sp[0], sp[1]
		val, _ := strconv.Atoi(valSt)
		if _, ok := m[line]; ok {
			println(count) // part one
			break
		}
		switch typ {
		case "nop":
			if partTwo && !changed {
				input[line] = "jmp " + valSt
				go rec(copyMap(m), line, count, input, true, true)
			}
			m[line] = true
			line++
		case "acc":
			m[line] = true
			line++
			count += val
		case "jmp":
			if partTwo && !changed {
				input[line] = "nop " + valSt
				go rec(copyMap(m), line, count, input, true, true)
			}
			m[line] = true
			line += val
		}
		if partTwo && line >= len(input) {
			println("!", count) //part two
			os.Exit(3)
		}
	}
	for partTwo {
	}
}
func copyMap(originalMap map[int]bool) map[int]bool {
	newMap := make(map[int]bool, 0)
	for k, v := range originalMap {
		newMap[k] = v
	}
	return newMap
}
func day8pt2() {
	rec(make(map[int]bool), 0, 0, ReadFromFile("day08.txt"), true, false)
}
