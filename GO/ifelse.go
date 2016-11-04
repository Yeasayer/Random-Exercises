package main

import "fmt"

func main(){
	if 7%2==0{
		fmt.Println("Hey! 7 is even!")
	} else {
		fmt.Println("Sup! 7 is ODD!")
	}

	if 8%4==0{
		fmt.Println("8 is divisible by 4!")
	}

	if num := 9; num < 0 {
		fmt.Println(num,"is negative!")
	} else if num < 10 {
		fmt.Println(num,"is one digit!")
	} else {
		fmt.Println(num,"really take cues from those CS grad memes!")
	}
}