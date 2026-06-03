## Golang Interview questions

## Content

1. [What the below code prints](#what-the-below-code-prints)
2. [Relation between defer and closure](#relation-between-defer-and-closure)

### What the below code prints

```go
func main(){
	var x []string;
	x = append(x,"Abir");
	x = append(x,"practic")
	x = append(x,"Go")

	y := x
    z := y
	x = append(x, "expert")
	y = append(y, "beginner")
	x[0] = "Nadia"

	fmt.Println(x,len(x),cap(x))
	fmt.Println(y,len(y),cap(y))
	fmt.Println(z,len(z),cap(z))
```

This will print

```bash
["Nadia", "practice", "go", "beginner"] 4 4
["Nadia", "practice", "go", "beginner"] 4 4
["Nadia", "practice", "go"] 3 4
```

Why is that, let's debunk line by line

- First three line `x` gets `"Abir","practice", "go"` so, pointer points at ref-start, len is 3 and cap is 4
- Then `y` gets the values of `x`, so it's pointer also points ref-start, len is 3, cap is 4
- Then `z` gets the values of `y`, so it's pointer also points ref-start, len is 3, cap is 4
- Then we again append to `x`, so pointer is same, len is 4 and the `python` takes `ref-start+3`th place, cap is 4
- Then we append from `y`, The initial pointer is same, but as the len was `3` for this one it becomes `4` and `beginner` takes the `ref-start+3`th place. cap is still 4
- then `x[0]=Nadia`, the initial pointer being same it's value changed from `Abir to Nadia`, the len stays 4, cap stays 4
- Now the part's are to print,
  - according to the latest values, everyones initial position pointer is same.
  - The 4th position changed, but as the z does not know that, it has only the first 3 values

Let's analyze the below code now

```go
func main(){
	var x []string;
	x = append(x,"abir");
	x = append(x,"pratice")

	y := x
    z := y
	x = append(x, "expert")
	y = append(y, "beginner")
	x[0] = "nadia"

	fmt.Println(x,len(x),cap(x))
	fmt.Println(y,len(y),cap(y))
	fmt.Println(z,len(z),cap(z))
}
```

A change in single line completely changes the game.

```bash
[nadia pratice expert] 3 4
[abir pratice beginner] 3 4
[abir pratice] 2 2
```

- First two line `x` gets `"abir", "practice"`, the pointer points at `ref-start1`, len is 2, cap is 2
- `y` and `z` gets the values what `x` has, the pointer points at `ref-start1`, len 2, cap 2
- Now `x` appends a value.
  - But this time the `cap` limit is reached, so the whole array copies to a new location with `ref-start2`
  - Appends the value `expert` to this new location, len is 3, cap is doubled to 4
- Then `y` appends a value
  - This `cap` limit of y hits. so the whole array at `ref-start1` copies to a new location lets say `ref-start3`
  - Appends the value `"abir", "practice"` + `begginer`, len is 3 cap is doubled to 4
- Now `x[0]='nadia'` so everything assumes same, just the `ref-start2` value changed `from abir to nadia`
- Not comes the printing part
  - X is pointing at `ref-start2` so it's value is `[nadia pratice expert]` len 3, cap 4
  - Y is pointing at `ref-start3` so it's value is `[abir pratice begginer]` len 3, cap 4
  - Z is pointing at `ref-start1` so it's value is old `[abir pratice]` len 2, cap 2

### Relation between defer and closure

We know that when a function returns another function, having some variable in the outer function, then the returned function is called closure or in other words, the returned function forms a closure with the outer function's escaping variables and putting them in the heap, so that those escaped variables can be used even after the outer function erased from the stack frame.

Also we know that the escaped variables are bind with inner method and a snapshot of the variable at the time of escaping (last value before inner method defined), so if we change the value of the variable after the inner function defined, it will not change the value of the variable in the inner function.

with example

```go
func outer() func(){
	x := 10
	inner := func(){
		x*=2
		fmt.Println(x)
	}
	x = 20
	return inner
}

func main(){
	closure1 := outer()
	closure1()

	closure2 := outer()
	closure2()
}
```

Here the inner function forms a closure with the variable `x` of the outer function, and the value of `x` at the time of defining inner function is `10`, so even if we change the value of `x` to `20` after defining inner function, it will not change the value of `x` in inner function, so when we call inner function it will print `20` instead of `40`. And both closure1 and closure2 will start printing `20` because they both have the same snapshot of `x` at the time of defining inner function.

Now if defer keyword call a function also forms a closure with the variables of the function, but it's **special** because for all other closure the outer function is erased from the stack when the inner function is called, but for defer the outer function is still there in the stack when the deferred function is called just before the outer function returns. So this time those variable are not snapshot with the deferred function, but their pointer is bind with the deferred function and kept in a linked-list in the very stack block of the function to be called in a stack/LIFO manner before the outer function returns, so if we change the value of the variable after the defer statement, it will change the value of the variable in the deferred function as well. And it is deliberately designed like this because defer is used to do some clean up work before the function returns, so it should have the latest value of the variable to do the clean up work properly.

Now there is a gotcha if the escaped variable is also a returned variable. Now in go returned variables can be named or unnamed.

If named returned variable get's the latest changes after defer statement is called but if the returned variable is unnamed then it will not get the latest changes after defer statement is called but the final value of if got at return statement not the change at defer. Cause in this case before the defer is called the return statement take a snapshot they are returning before starting to execute the defer statement.

An example will shade more light on this

```go
func outer() (x int){
	x = 10
	inner = func(){
		x*=2
		fmt.Println("inner", x)
	}
	defer inner()
	x = 20
	fmt.Println("outer", x)
	return x
}
func main(){
	fmt.Println("main", outer())
}
```

here we will get

```bash
outer 20
inner 40
main 40
```

on the other hand if we change the return type to unnamed then we will get

```go
func outer() int{
	x := 10
	inner = func(){
		x*=2
		fmt.Println("inner", x)
	}
	defer inner()
	x = 20
	fmt.Println("outer", x)
	return x
}
func main(){
	fmt.Println("main", outer())
}
```

the output will be

```bash
outer 20
inner 40
main 20
```
