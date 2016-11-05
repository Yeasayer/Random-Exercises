package main 

import "fmt"

func sum(nums ...int){
	fmt.Println(nums," ")
	total := 0
	for i, num := range nums{
		total += num
		if i == len(nums)-1{
			fmt.Print(num,"=")
		}else{
			fmt.Print(num,"+")
		}
	}
	fmt.Println(total)
}

func main(){

	sum(1,2)
	sum(3,5,7)

	nums := []int{1,2,3,4}
	sum(nums...)
}