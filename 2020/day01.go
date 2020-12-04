package main

import (
	"strconv"
)

func day1() {
	input := ReadFromFile("day01.txt")
	var nums = make([]int, len(input))
	for i, num := range input {
		nt, _ := strconv.Atoi(num)
		nums[i] = nt
	}
	for i, num := range nums {
		for j, num2 := range nums {
			for k, num3 := range nums {
				if i != j && i != k {
					if num+num2+num3 == 2020 {
						println(num * num2 * num3)
					}
				}
			}
		}
	}
}
