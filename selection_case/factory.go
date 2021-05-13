package main

import "fmt"

type calculator interface {
	execute(a, b int) int
}

type addition struct {
}

func (h addition) execute(a, b int) int {
	return a + b
}

type subtraction struct {
}

func (h subtraction) execute(a, b int) int {
	return a - b
}

func main() {
	var tester calculator
	tester = addition{}
	fmt.Println(tester.execute(1, 2))
	tester = subtraction{}
	fmt.Println(tester.execute(1, 2))
}
