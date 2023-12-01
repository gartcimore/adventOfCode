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
var FILENAME_TEST = "input_test"

func main() {
	part1()
	part2()

	//
}

func part1() {
	//open and read the file and return a slice with slices
	var stacks [][]byte
	//f, err := os.Open("./day5/" + FILENAME_TEST)
	f, err := os.Open("./day5/" + FILENAME)
	//f, err := os.Open(FILENAME)
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

			for stack := range stacks {
				for i := 0; i < len(stacks[stack])/2; i++ {
					j := len(stacks[stack]) - 1 - i
					stacks[stack][i], stacks[stack][j] = stacks[stack][j], stacks[stack][i]
				}
			}
			continue
		}

		lineAsRune := []rune(line)
		//fmt.Printf("lineAsRune length %v\n", len(lineAsRune))

		if string(lineAsRune[1]) == "1" {
			//skip empty line
			fmt.Printf("line is colums declaration\n")
			continue
		}

		//parse moving instructions
		// move 1 from 8 to 7
		if strings.HasPrefix(line, "move") {
			prettyPrintStacks(stacks)
			//fmt.Printf("line to move  %v\n", line)

			fields := strings.Fields(line[5:])
			nbToMove, _ := strconv.Atoi(fields[0])
			from, _ := strconv.Atoi(fields[2])
			to, _ := strconv.Atoi(fields[4])

			from--
			to--

			for nbToMove > 0 {
				fmt.Printf("move %v from %v to %v \n", nbToMove, from, to)
				fmt.Printf("stacks[to] len=%d cap=%d %v\n", len(stacks[to]), cap(stacks[to]), stacks[to])
				fmt.Printf("stacks[from] len=%d cap=%d %v\n", len(stacks[from]), cap(stacks[from]), stacks[from])
				//lastIndexFrom := getLastIndex(stacks[from])
				//fmt.Printf("getLastIndex(stacks[from]) %d \n", lastIndexFrom)
				//toAppend := stacks[from][lastIndexFrom]
				//fmt.Printf("toAppend is [%v] \n", string(toAppend))
				//stacks[to] = append(stacks[to], toAppend)
				//stacks[from][lastIndexFrom] = 0
				stacks[to] = append(stacks[to], stacks[from][len(stacks[from])-1])
				stacks[from] = stacks[from][:len(stacks[from])-1]
				nbToMove--
				printStack(stacks[from])
				printStack(stacks[to])

			}
		} else {
			column := 0
			for {
				if column > len(stacks)-1 {
					stacks = append(stacks, []byte(nil))
				}

				if line[0] == '[' {
					stacks[column] = append(stacks[column], line[1])
				}

				if line = line[3:]; len(line) == 0 {
					break
				}

				line = line[1:] // Consume space
				column++
			}
			//if string(lineAsRune[1]) != " " {
			//	stacks[0] = shiftNInsert(stacks[0], lineAsRune[1])
			//}
			//if string(lineAsRune[5]) != " " {
			//	stacks[1] = shiftNInsert(stacks[1], lineAsRune[5])
			//}
			//if string(lineAsRune[9]) != " " {
			//	stacks[2] = shiftNInsert(stacks[2], lineAsRune[9])
			//}
			//if string(lineAsRune[13]) != " " {
			//	stacks[3] = shiftNInsert(stacks[3], lineAsRune[13])
			//}
			//if string(lineAsRune[17]) != " " {
			//	stacks[4] = shiftNInsert(stacks[4], lineAsRune[17])
			//}
			//if string(lineAsRune[21]) != " " {
			//	stacks[5] = shiftNInsert(stacks[5], lineAsRune[21])
			//}
			//if string(lineAsRune[25]) != " " {
			//	stacks[6] = shiftNInsert(stacks[6], lineAsRune[25])
			//}
			//if string(lineAsRune[29]) != " " {
			//	stacks[7] = shiftNInsert(stacks[7], lineAsRune[29])
			//}
			//if string(lineAsRune[33]) != " " {
			//	stacks[8] = shiftNInsert(stacks[8], lineAsRune[33])
			//}
		}

	}

	for _, stack := range stacks {
		printStack(stack)
	}
	displayTopCrates(stacks)
}

func prettyPrintStacks(stacks [][]byte) {

	var sb strings.Builder

	for i := range stacks {
		sb.WriteString(fmt.Sprintf("[%d] ", i))
	}

	fmt.Println(sb.String())
	sb.Reset()
	for i := 0; i < 15; i++ {
		for _, stack := range stacks {
			if len(stack) > i {
				r := stack[i]
				if r == 0 {
					sb.WriteString("[ ] ")
				} else {
					sb.WriteString(fmt.Sprintf("[%v] ", string(r)))
				}
			} else {
				sb.WriteString("[ ] ")
			}
		}
		fmt.Println(sb.String())
		sb.Reset()
	}
}

func printStack(stack []byte) {
	for _, item := range stack {
		fmt.Printf("[%v]", string(item))
	}
	fmt.Printf("\n")
}

func displayTopCrates(stacks [][]byte) {
	for _, stack := range stacks {
		fmt.Printf("%c", stack[len(stack)-1])
	}
}

func part2() {
	//open and read the file and return a slice with slices
	var stacks [][]byte
	//f, err := os.Open("./day5/" + FILENAME_TEST)
	f, err := os.Open("./day5/" + FILENAME)
	//f, err := os.Open(FILENAME)
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

			for stack := range stacks {
				for i := 0; i < len(stacks[stack])/2; i++ {
					j := len(stacks[stack]) - 1 - i
					stacks[stack][i], stacks[stack][j] = stacks[stack][j], stacks[stack][i]
				}
			}
			continue
		}

		lineAsRune := []rune(line)
		//fmt.Printf("lineAsRune length %v\n", len(lineAsRune))

		if string(lineAsRune[1]) == "1" {
			//skip empty line
			fmt.Printf("line is colums declaration\n")
			continue
		}

		//parse moving instructions
		// move 1 from 8 to 7
		if strings.HasPrefix(line, "move") {
			prettyPrintStacks(stacks)
			//fmt.Printf("line to move  %v\n", line)

			fields := strings.Fields(line[5:])
			nbToMove, _ := strconv.Atoi(fields[0])
			from, _ := strconv.Atoi(fields[2])
			to, _ := strconv.Atoi(fields[4])

			from--
			to--

			fmt.Printf("move %v from %v to %v \n", nbToMove, from, to)
			fmt.Printf("stacks[to] len=%d cap=%d %v\n", len(stacks[to]), cap(stacks[to]), stacks[to])
			fmt.Printf("stacks[from] len=%d cap=%d %v\n", len(stacks[from]), cap(stacks[from]), stacks[from])
			cut := len(stacks[from]) - nbToMove
			stacks[to] = append(stacks[to], stacks[from][cut:]...)
			stacks[from] = stacks[from][:cut]
			printStack(stacks[from])
			printStack(stacks[to])

		} else {
			column := 0
			for {
				if column > len(stacks)-1 {
					stacks = append(stacks, []byte(nil))
				}

				if line[0] == '[' {
					stacks[column] = append(stacks[column], line[1])
				}

				if line = line[3:]; len(line) == 0 {
					break
				}

				line = line[1:] // Consume space
				column++
			}
		}

	}

	for _, stack := range stacks {
		printStack(stack)
	}
	displayTopCrates(stacks)
}
