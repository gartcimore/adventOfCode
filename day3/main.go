package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"unicode/utf8"
	"unicode"
)

var FILENAME = "input"
var letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
}

func splitLines(line string) (string, string){
	var lineLength = utf8.RuneCountInString(line)
	fmt.Printf("Length of line is %d\n", lineLength)
	fmt.Printf("line is %s\n", line)
	var front = line[0:lineLength/2]
	var back = line[lineLength/2:lineLength]
	return front, back
}

func analyseItemPlacement(front string, back string) (int){
	for _, rune := range front {
		if(strings.ContainsRune(back, rune)) {
			fmt.Printf("back contains this rune %q\n", rune)
			return priority(rune)
		}
	}
	return 0;
}

func priority(c rune) int {
	if unicode.IsUpper(c) {
		return int(c - 38)
	} else {
		return int(c - 96)
	}
}