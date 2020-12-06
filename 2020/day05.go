package main

import (
	"sort"
)

func day5pt1() {
	input := ReadFromFile("day05.txt")
	seats := []int{}
	for _, pass := range input {
		row := []int{0, 127}
		col := []int{0, 7}
		for _, ch := range pass {
			switch ch {
			case 'F':
				row[1] = row[0] + (row[1]-row[0])/2
				break
			case 'B':
				row[0] = row[1] - (row[1]-row[0])/2
				break
			case 'L':
				col[1] = col[0] + (col[1]-col[0])/2
				break
			case 'R':
				col[0] = col[1] - (col[1]-col[0])/2
				break
			}
		}
		seats = append(seats, row[0]*8+col[0])
	}
	sort.Ints(seats)
	//part 1
	println(seats[len(seats)-1])
	//part 2
	//I could optimize this by doing something similar to binary search
	// but I decided that simple is better in this case
	for i, seat := range seats {
		if seats[i+1] != seat+1 {
			println(seat + 1)
			break
		}
	}

}
