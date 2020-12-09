package main

import (
	"os"
	"sort"
	"strconv"
)

func valid(arr []int, lookingFor int) bool {
	for i, num1 := range arr {
		for j, num2 := range arr {
			if i != j {
				if num1+num2 == lookingFor {
					return true
				}
			}
		}
	}
	return false
}

func day9pt1() int {
	input := ReadFromFile("day09.txt")
	var arr []int
	var num int
	for i, numSt := range input {
		num, _ = strconv.Atoi(numSt)
		if i < 50 {
			arr = append(arr, num)
		} else {
			if valid(arr, num) {
				arr = append(arr, num)
				arr = arr[1:]
			} else {
				return num
			}
		}
	}
	return 0
}
func day9pt2() int {
	input := ReadFromFile("day09.txt")
	lookingFor := day9pt1()
	var arr []int
	var num int
	for _, numSt := range input {
		num, _ = strconv.Atoi(numSt)
		if num == lookingFor {
			println(findParts(arr, lookingFor))
			os.Exit(3)
		}
		arr = append(arr, num)
	}
	return -1
}

func findParts(arr []int, lookingFor int) int {
	var subArr []int
	for i, num1 := range arr {
		subArr = []int{num1}
		for j := i + 1; j < len(arr); j++ {
			sum := sum(subArr)
			if sum == lookingFor {
				sort.Ints(subArr)
				return subArr[0] + subArr[len(subArr)-1]
			} else if sum < lookingFor {
				subArr = append(subArr, arr[j])
			} else {
				break
			}
		}
	}
	return -1
}
func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}
