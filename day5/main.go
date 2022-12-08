package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var FILENAME = "input"

func main() {
	part1()

	//
}

func part1() {
	//open and read the file and return a slice with slices
	stacks := make([][]rune, 9)
	for i := 0; i < 9; i++ {
		stacks[i] = make([]rune, 8)
	}
	f, err := os.Open("./day5/" + FILENAME)
	if err != nil {
		log.Fatalf("%v\n", err)
	}
	contents := bufio.NewScanner(f)
	for contents.Scan() {
		line := contents.Text()
		//fmt.Printf("line  %v\n", line)
		//fmt.Printf("line length %v\n", len(line))

		if line == "" {
			//skip empty line
			fmt.Printf("empty line, skipping\n")
			break
		}

		lineAsRune := []rune(line)
		//fmt.Printf("lineAsRune length %v\n", len(lineAsRune))

		if string(lineAsRune[1]) == "1" {
			//skip empty line
			fmt.Printf("line is colums declaration\n")
			break
		}

		if string(lineAsRune[1]) != " " {
			stacks[0] = shiftNInsert(stacks[0], lineAsRune[1])
		}
		if string(lineAsRune[5]) != " " {
			stacks[1] = shiftNInsert(stacks[1], lineAsRune[5])
		}
		if string(lineAsRune[9]) != " " {
			stacks[2] = shiftNInsert(stacks[2], lineAsRune[9])
		}
		if string(lineAsRune[13]) != " " {
			stacks[3] = shiftNInsert(stacks[3], lineAsRune[13])
		}
		if string(lineAsRune[17]) != " " {
			stacks[4] = shiftNInsert(stacks[4], lineAsRune[17])
		}
		if string(lineAsRune[21]) != " " {
			stacks[5] = shiftNInsert(stacks[5], lineAsRune[21])
		}
		if string(lineAsRune[25]) != " " {
			stacks[6] = shiftNInsert(stacks[6], lineAsRune[25])
		}
		if string(lineAsRune[29]) != " " {
			stacks[7] = shiftNInsert(stacks[7], lineAsRune[29])
		}
		if string(lineAsRune[33]) != " " {
			stacks[8] = shiftNInsert(stacks[8], lineAsRune[33])
		}
	}

	for _, stack := range stacks {
		printStack(stack)
	}

	displayTopCrates(stacks)
	return
	//parse moving instructions
	// move 1 from 8 to 7

	contents = bufio.NewScanner(f)
	for contents.Scan() {
		line := contents.Text()
		if strings.HasPrefix(line, "move") {
			fmt.Printf("line to move  %v\n", line)

			fields := strings.Fields(line[5:])
			nbToMove, _ := strconv.Atoi(fields[0])
			from, _ := strconv.Atoi(fields[2])
			to, _ := strconv.Atoi(fields[4])

			from--
			to--
			printStack(stacks[from])
			printStack(stacks[to])

			for nbToMove > 0 {
				fmt.Printf("move %v from %v to %v \n", nbToMove, from, to)

				// Now "x" is the ith element and "xs" has the ith element removed.
				break
				//stacks[to-1] = append(stacks[to-1], stacks[from-1][len(stacks[from-1])-1])
				//stacks[from-1] = stacks[from-1][:len(stacks[from-1])-1]
				nbToMove--
			}
		}
	}
	for _, stack := range stacks {
		fmt.Printf("%c", stack[len(stack)-1])
	}
}

func shiftNInsert(stack []rune, data rune) []rune {
	stack = append(stack, 0)   // Making space for the new element
	copy(stack[1:], stack[0:]) // Shifting elements
	stack[0] = data            // Copying/inserting the value
	return stack
}

func printStack(stack []rune) {
	for _, item := range stack {
		fmt.Printf("[%v]", string(item))
	}
	fmt.Printf("\n")
}

func displayTopCrates(stacks [][]rune) {
	var result = ""
	for _, stack := range stacks {
		result += string(stack[getLastIndex(stack)])
	}
	fmt.Printf("part 1 result %v", result)
}

func getLastIndex(slc []rune) int {
	for i, r := range slc {
		if r == 0 {
			return i - 1
		}
	}
	return 0
}
