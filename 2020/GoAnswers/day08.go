package main

import (
	"os"
	"strconv"
	"strings"
)

func day8pt1() {
	m := make(map[int]bool)
	count := 0
	line := 0
	input := ReadFromFile("day08.txt")
	for {
		instruction := input[line]
		sp := strings.Split(instruction, " ")
		typ, valSt := sp[0], sp[1]
		if _, ok := m[line]; ok {
			print(count)
			break
		}
		m[line] = true
		val, _ := strconv.Atoi(valSt)
		switch typ {
		case "nop":
			line++
			break
		case "acc":
			line++
			count += val
		case "jmp":
			line += val
		}
	}
}

func rec(m map[int]bool, line int, count int, input []string, changed bool) {
	for {
		instruction := input[line]
		sp := strings.Split(instruction, " ")
		typ, valSt := sp[0], sp[1]
		val, _ := strconv.Atoi(valSt)
		if _, ok := m[line]; ok {
			break
		}

		switch typ {
		case "nop":
			if !changed {
				input[line] = "jmp " + valSt
				go rec(copyMap(m), line, count, input, true)
			}
			m[line] = true
			line++
		case "acc":
			m[line] = true
			line++
			count += val
		case "jmp":
			if !changed {
				input[line] = "nop " + valSt
				go rec(copyMap(m), line, count, input, true)
			}
			m[line] = true
			line += val
		}

		if line >= len(input) {
			println("!", count)
			os.Exit(3)
		}
	}
	for {
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
	rec(make(map[int]bool), 0, 0, ReadFromFile("day08.txt"), false)
}
