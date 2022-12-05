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
	tasksRange := getFile()
	cleaningTasks := getTasks(tasksRange)
	var totalPart1 = 0
	for index := 0; index < len(cleaningTasks); index += 2 {
		if cleaningTasks[index].lower <= cleaningTasks[index+1].lower &&
			cleaningTasks[index].upper >= cleaningTasks[index+1].upper {
			fmt.Printf("cleaningTasks[index] %v is > %v\n", cleaningTasks[index], cleaningTasks[index+1])
			totalPart1 += 1

		} else if cleaningTasks[index].lower >= cleaningTasks[index+1].lower &&
			cleaningTasks[index].upper <= cleaningTasks[index+1].upper {
			fmt.Printf("cleaningTasks[index] %v is < %v\n", cleaningTasks[index], cleaningTasks[index+1])
			totalPart1 += 1
		}
	}
	fmt.Printf("total part 1 is %d\n", totalPart1)

}

type cleaningTask struct {
	lower int
	upper int
}

func getTasks(lines []string) []cleaningTask {

	var cleaningTasks = []cleaningTask{}
	for _, line := range lines {
		var splitTasks = strings.Split(line, ",")
		fmt.Printf("splitTasks is %v\n", splitTasks)

		var taskStr1 = strings.Split(splitTasks[0], "-")
		var taskStr2 = strings.Split(splitTasks[1], "-")
		var lower, _ = strconv.Atoi(taskStr1[0])
		var upper, _ = strconv.Atoi(taskStr1[1])
		fmt.Printf("lower is %v\n", lower)
		fmt.Printf("upper is %v\n", upper)
		var task1 = cleaningTask{lower: lower, upper: upper}
		cleaningTasks = append(cleaningTasks, task1)

		lower, _ = strconv.Atoi(taskStr2[0])
		upper, _ = strconv.Atoi(taskStr2[1])
		fmt.Printf("lower is %v\n", lower)
		fmt.Printf("upper is %v\n", upper)
		var task2 = cleaningTask{lower: lower, upper: upper}
		cleaningTasks = append(cleaningTasks, task2)
	}
	return cleaningTasks
}

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
