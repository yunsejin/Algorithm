package main

import (
	"fmt"
)

func main() {
	arr := make([]int, 8)
	for i := 0; i < 8; i++ {
		fmt.Scan(&arr[i])
	}

	if isAscending(arr) {
		fmt.Println("ascending")
	} else if isDescending(arr) {
		fmt.Println("descending")
	} else {
		fmt.Println("mixed")
	}
}

func isAscending(arr []int) bool {
	for i := 0; i < 7; i++ {
		if arr[i] > arr[i+1] {
			return false
		}
	}
	return true
}

func isDescending(arr []int) bool {
	for i := 0; i < 7; i++ {
		if arr[i] < arr[i+1] {
			return false
		}
	}
	return true
}
