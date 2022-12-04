package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
//	"strings"
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
	for _, line := range rucksacks {
		splitLines(line)
	}
}

func splitLines(line string) (string, string){
	var lineLength = utf8.RuneCountInString(line)
	fmt.Printf("Length of line is %d\n", lineLength)
	fmt.Printf("line is %s\n", line)
	var front = line[0:lineLength/2]
	var back = line[lineLength/2:lineLength]
	fmt.Printf("front is %s\n", front)
	fmt.Printf("back is %s\n", back)
	return front, back
}