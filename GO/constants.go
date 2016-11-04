package main

import "fmt"
import "math"

const s string = "constant"

func main() {
	fmt.Println(s)
	const n = 500000000

	const e = 3e20/n
	fmt.Println(e)

	fmt.Println(int64(e))

	fmt.Println(math.Sin(n))
}