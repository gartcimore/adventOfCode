package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var FILENAME = "input"

var (
	R, P, S = 1, 2, 3 //score for corresponding shapes
	L, D, W = 0, 3, 6 //Lose, Draw, Win

)

func getFile() [][]string {
	//open and read the file and return a slice with slices
	var container [][]string
	f, err := os.Open(FILENAME)
	if err != nil {
		log.Fatalf("%v\n", err)
	}
	contents := bufio.NewScanner(f)
	for contents.Scan() {
		line := contents.Text()
		line_arr := strings.Split(line, " ")
		container = append(container, line_arr)
	}
	return container
}

func main() {
	games := getFile()

	var Total = 0
	for _, shps := range games {
		opp, me := shps[0], shps[1]
		var score int
		switch opp {
		case "A":
			//Rock
			if me == "Y" {
				//Paper wins against rock
				score = W + P
			} else if me == "X" {
				//draw rock vs rock
				score = D + R
			} else {
				//lose against Scissors
				score = L + S
			}
		case "B":
			//Paper
			if me == "Z" {
				//win, scissors
				score = W + S
			} else if me == "Y" {
				//draw, Paper
				score = D + P
			} else {
				//lose, Rock
				score = L + R
			}
		case "C":
			//Scissors
			if me == "X" {
				//win, Rock
				score = W + R

			} else if me == "Z" {
				//Draw, Scissors
				score = D + S

			} else {
				//lose, Paper
				score = L + P

			}
		default:
			fmt.Println(opp, me)
		}
		// log.Print(score)
		Total += score
	}
	fmt.Printf("\nfinal score: %v\n", Total)
}
