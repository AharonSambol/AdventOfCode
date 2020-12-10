package main

import (
	"os"
	"sort"
)

func day10pt1() {
	input := ReadFromFileNums("day10.txt")
	sort.Ints(input)
	diffsOfThrees := 1
	diffsOfOnes := 0
	lastNum := 0
	for _, num := range input {
		switch num - lastNum {
		case 1:
			diffsOfOnes++
		case 3:
			diffsOfThrees++
		default:
			println("diff is-", num, lastNum)
			os.Exit(-1)
		}
		lastNum = num
	}
	println(diffsOfOnes * diffsOfThrees)
}

func day10pt2() {
	//THIS IS BAD CODE!!!!
	//the right way is to add each one to a dict and then each thing is the sum of it-1 + it- 2 +it -3
	//if it-x isnt in the dic the its +0
	input := ReadFromFileNums("day10.txt")
	input = append(input, 0)
	arr := getAmountOfPossibilities(input)
	arr = reverse(arr)
	print(countPos(arr))
}

func getAmountOfPossibilities(input []int) []int {
	sort.Ints(input)
	ans := make([]int, len(input))
	for i, num := range input {
		for j := i + 1; j < len(input); j++ {
			if input[j]-num <= 3 {
				ans[i]++
			} else {
				break
			}
		}
	}
	return ans
}

func reverse(s []int) []int {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func countPos(arr []int) int {
	for indx, num := range arr {
		arr[indx] = 0
		for i := 0; i < num; i++ {
			arr[indx] += arr[indx-i-1]
		}
		if arr[indx] == 0 {
			arr[indx]++
		}
	}
	return arr[len(arr)-1]
}
