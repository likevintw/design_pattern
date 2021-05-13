package main

import "fmt"

type calculator func(a, b int) int

func addition(a, b int) int {
	return a + b
}
func subtraction(a, b int) int {
	return a - b
}

func getCalculator(input string) calculator {
	switch input {
	case "addition":
		return calculator(addition)
	case "subtraction":
		return calculator(subtraction)
	default:
		return nil
	}
}

func main() {
	calculator := getCalculator("addition")
	if calculator != nil {
		fmt.Println(calculator(1, 2))
	}
	calculator = getCalculator("subtraction")
	if calculator != nil {
		fmt.Println(calculator(1, 2))
	}
	calculator = getCalculator("no")
	if calculator != nil {
		fmt.Println(calculator(1, 2))
	}
}
