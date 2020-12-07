package main

func day6pt1() {
	input := ReadFromFile("day06.txt")
	count := 0
	group := make(map[rune]int)
	for _, line := range input {
		if line == "" {
			for range group {
				count++
			}
			group = make(map[rune]int)
		} else {
			for _, ans := range line {
				group[ans] = 1
			}
		}
	}
	print(count)
}

func day6pt2() {
	input := ReadFromFile("day06.txt")
	count := 0
	amountOfPPl := 0
	group := make(map[rune]int)
	for _, line := range input {
		if line == "" {
			for k := range group {
				if group[k] == amountOfPPl {
					count++
				}
			}
			group = make(map[rune]int)
			amountOfPPl = 0
		} else {
			amountOfPPl++
			for _, ans := range line {
				group[ans] = group[ans] + 1
			}
		}
	}
	print(count)
}
