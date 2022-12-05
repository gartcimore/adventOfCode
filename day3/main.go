package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"unicode"
	"unicode/utf8"
)

var FILENAME = "input"

func getFile() []string {
	//open and read the file and return a slice with slices
	var container []string
	f, err := os.Open(FILENAME)
	if err != nil {
		log.Fatalf("%v\n", err)
	}
	contents := bufio.NewScanner(f)
	for contents.Scan() {
		line := contents.Text()
		container = append(container, line)
	}
	return container
}

func main() {
	rucksacks := getFile()
	fmt.Printf("\n : %v\n", rucksacks)
	var total = 0
	for _, line := range rucksacks {
		var front, back = splitLines(line)
		fmt.Printf("front is %s\n", front)
		fmt.Printf("back is %s\n", back)
		total += analyseItemPlacement(front, back)
	}
	fmt.Printf("total is %d\n", total)
	fmt.Printf("starting part 2\n")

	var totalPart2 = 0
	for index := 0; index < len(rucksacks); index += 3 {
		var set2 = makeSet(rucksacks[index+1])
		var set3 = makeSet(rucksacks[index+2])
		for _, current := range rucksacks[index] {
			if set2[current] && set3[current] {
				//found the badge
				totalPart2 += priority(current)
				break
			}
		}
	}
	fmt.Printf("total part2 is %d\n", totalPart2)

}

func makeSet(line string) map[int32]bool {
	var sorted = make(map[int32]bool)
	for _, r := range line {
		sorted[r] = true
	}
	return sorted
}

func splitLines(line string) (string, string) {
	var lineLength = utf8.RuneCountInString(line)
	fmt.Printf("Length of line is %d\n", lineLength)
	fmt.Printf("line is %s\n", line)
	var front = line[0 : lineLength/2]
	var back = line[lineLength/2 : lineLength]
	return front, back
}

func analyseItemPlacement(front string, back string) int {
	for _, r := range front {
		if strings.ContainsRune(back, r) {
			fmt.Printf("back contains this rune %q\n", r)
			return priority(r)
		}
	}
	return 0
}

func priority(c rune) int {
	if unicode.IsUpper(c) {
		return int(c - 38)
	} else {
		return int(c - 96)
	}
}
