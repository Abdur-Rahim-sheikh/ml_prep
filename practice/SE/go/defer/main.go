package main

import "fmt"

func calculate() (result int){
	fmt.Println("first", result)
	show:= func(){
		result+=10
		fmt.Println("defer", result)
	}
	defer show()
	result = 5
	fmt.Println("second", result)
	return result
}

func calc()  int{
	result := 0
	fmt.Println("first", result)
	show:= func(){
		result+=10
		fmt.Println("defer", result)
	}
	defer show()
	result = 5
	fmt.Println("second", result)
	return result
}

func outer() (result int) {
	fmt.Println("first outer", result)
	show := func() {
		result += 10
		fmt.Println("defer", result)
	}
	defer show()

	p:= func(a int){
		a++
		fmt.Println("ami", a)
	}

	defer p(result)
	result = 5
	defer fmt.Println(result)
	fmt.Println("second", result)
	return result
}

func main() {
	fmt.Println(calculate())
	fmt.Println(calc())
	fmt.Println(outer())
}