package main

import "fmt"

func main() {
	i := 1
	for i <= 3{
		fmt.Println("Hey this is the number ",i,"!")
		i = i + 1
	}
	for j := 7; j <= 9; j++ {
		fmt.Println("We're on the number ",j,"! YAY!")
	}
	for{
		fmt.Println("looopdelooop")
		break
	}
	fmt.Println("WE'RE DONE HERE!")
}