package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

type pos struct {
	row int
	col int
}
type node struct {
	value    int
	distance int
}

func ReadFromFileNums(fileName string) [][]node {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatalf("failed to open")
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var text [][]node
	for row := 0; scanner.Scan(); row++ {
		text = append(text, []node{})
		for _, chr := range scanner.Text() {
			num, _ := strconv.Atoi(string(chr))
			text[row] = append(text[row], node{num, -1})
		}
	}
	file.Close()
	return text
}

func main() {
	isPart2 := true
	input := ReadFromFileNums("D:/Aharon/golang/day15.text")
	if isPart2 {
		input = makeBiggerMapPart2(input)
	}
	findPath(&input, []int{0, 0})
	print(input[len(input)-1][len(input[0])-1].distance)
}

func makeBiggerMapPart2(original [][]node) [][]node {
	newMap := make([][]node, len(original)*5)
	for i := 0; i < len(newMap); i++ {
		newMap[i] = make([]node, len(original[0])*5)
	}
	for row := 0; row < len(original); row++ {
		for col := 0; col < len(original[0]); col++ {
			for r := 0; r < 5; r++ {
				for c := 0; c < 5; c++ {
					val := original[row][col].value + r + c
					for val > 9 {
						val -= 9
					}
					newMap[len(original)*r+row][len(original[0])*c+col] = node{val, -1}
				}
			}
		}
	}
	return newMap
}

func findPath(mazePointer *[][]node, curPos []int) {
	maze := *mazePointer
	for row := 0; row < len(maze); row++ {
		for col := 0; col < len(maze[0]); col++ {
			if row == 0 && col == 0 {
				maze[row][col].distance = 0
				continue
			}
			minVal := 0
			if row != 0 {
				minVal = maze[row-1][col].distance
			}
			if col != 0 && (row == 0 || maze[row][col-1].distance < minVal) {
				minVal = maze[row][col-1].distance
			}
			maze[row][col].distance = minVal + maze[row][col].value
			updateNeighbor(mazePointer, pos{row, col}, maze[row][col].distance)
		}
	}
}

func updateNeighbor(mazePointer *[][]node, curPos pos, curVal int) {
	maze := *mazePointer
	for _, neighbor := range []pos{
		{curPos.row - 1, curPos.col}, {curPos.row, curPos.col - 1},
		{curPos.row + 1, curPos.col}, {curPos.row, curPos.col + 1}} {
		if neighbor.row < 0 || neighbor.col < 0 || neighbor.row == len(maze) || neighbor.col == len(maze[0]) {
			continue
		}
		nbr := &maze[neighbor.row][neighbor.col]
		if curVal+nbr.value < nbr.distance {
			nbr.distance = curVal + nbr.value
			updateNeighbor(mazePointer, neighbor, nbr.distance)
		}
	}
}
