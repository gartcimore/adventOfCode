package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	currentMax := 0
	scanner := bufio.NewScanner(file)
	elves := make([]int, 0)
	// optionally, resize scanner's capacity for lines over 64K, see next example
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			//new elve
			fmt.Println("new elve, reset currentMax ", currentMax)
			elves = append(elves, currentMax)
			currentMax = 0
		}
		intVar, _ := strconv.Atoi(line)
		currentMax += intVar
		fmt.Println("currentMax for this elve is ", currentMax)
	}
	fmt.Println("nb of elves ", len(elves))
	sort.Sort(sort.Reverse(sort.IntSlice(elves)))

	totalCountOfCalories := elves[0] + elves[1] + elves[2]
	fmt.Println("most calorie for one elve ", elves[0])
	fmt.Println("final calories count is ", totalCountOfCalories)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
