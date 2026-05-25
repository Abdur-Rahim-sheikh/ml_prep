# Interview preperations for Golang

### Resources

- [Go with habib (beginner)](https://www.youtube.com/playlist?list=PLpCqPSEm2Xe8sEY2haMDUVgwbkIs5NCJI)

## Content

1. [Internal Memory](#internal-memory)
2. [Closure](#closure)
3. [Receiver](#receiver)
4. [Slice and Slice in Slice](#slice-and-slice-in-slice)
5. [Slice Capacity](#slice-capacity)
6. [Variadic Function](#variadic-function)
7. [Basic types of Golang](#basic-types-of-golang)
8. [Auto type conversion](#auto-type-conversion)

#### Internal Memory

There are 4 basic types of memory

- **Code segment**
  - Functions, constant are kept here as binary
- **Data segment**
  - All global veriables are kept here
- **Stack**
  - During runtime the running blocks (actually only reference of the code segment) and scoped variables are kept here
  - as soon as the function is done that part is removed from stack
- **Heap**
  - It keeps the value **escaped** during execution of closure, more later
  - Managed by gorutine garbage collector.

#### Closure

If a function's inner function needs a variable from that function, then it keeps the
varialbe outside of scope, called closure.

```go
int a=3;
const PI=3.1416;

func outer(){
    int b=8;
    int result = 0;

    func inner(){
        result:=result+a+b;
        return result;
    }
    return inner;
}

func main(){
    x:=outer()
    x()
    x()
    y:=outer()
    y()
}
```

Here during compilation,

- Code Block has: Const PI, outer function, main function
- Data block has: variable a

Then during execution,
in Stack:

- finds init -> not found no isue
- find main -> found
  - finds outer -> execute returns inner, escapes `b and result to heap`
  - executes inner taking data b and result from heap (by the way currently outer function is not present in stack just those escapped values)
  - executes inner second time
  - finds outer again -> escapes the b and result to heap again
  - gets another inner
  - executes that another inner again
  - exits main

### Receiver

In Go, receiver is what turns a normal function into a method `attached` to a type.
in below code `Citizen` and `isChild` are receriver.

There are two types of receiver:

1. Value Receiver
   - works on a copy
   - original struct does not change
   - `Citizen` is the example
2. Pointer receiver
   - works on the original value
   - Can modify struct fields

```go
type User struct{
    name string
    age int
}
// we can use any variable instead of `this` but its usually named as `this`
func (this User) Citizen(){
    return this.name>17
}

func (this *User) isChild(){
    return this.age<5
}
```

**Note**: If any method on a type uses a pointer receiver, it's common practice to use pointer receivers for all methods of that type.

### Slice and Slice in Slice

In go, slice contains a container of 3 things of the original array (pointer, length, capacity)

```go
arr = [5]string{"I", "am","giving","slice","example"}
slice1 = arr[1:4]
slice2 = arr[3:4]

//also we could initiate with direct slice literal
// just not mentioning size in the braces
brr = []int{1,2,3}
```

Here,
Slice 1,

- Pointing to adress of "am" variable
- Is of length (len) 3 cause (1,2,3 is it's values)
- Is of capacity (cap) 4
  - as the original allocates at most 4 element from the pointer

The slice 2:

- Pointing to adress of "slice" variable
- Is of length (len) 1
- Is of capacity (cap) 2
  - As the original allocates at most 2 element from the pointer

So the **Capacity** is particularly helpful when we start appending
in the slice. Cause if it exceeds the orignal capacity. The day of pointing
stops here, it copies the whole original array to a new place with bigger capacity.

So we try to allocate the first capacity as such, it need to to exceed at any time.

**Note**:

- If slice is coded to `escape` the function, the array is declared in `heap` at the beginning not stack.
- To escape it can be returned from function or any append operation also makes it `escapable` so if any changes done to the original array in the whole code, utilizing the analysis it allocate in heap from the start.

### Slice Capacity

```go
arr:=map([]int, 3, 5); //int type array, size 3 (initialized 0), capacity 5
arr = appen(arr,2)
```

after appending the array becomes [0,0,0,2]
If we keep appending and it tries to exceed the capacity.
It copies the whole thing to a new place with increased size.

How the capacity increases.

- Before `Go 1.18` version, It doubles till `threshold=1024`, after that it increases by `25%` to not waste much.
- From `Go 1.18` version, It doubles till `threshold=256`, after that it increases by `cap+=(cap + 3 * threshold)/4` to not waste much.

But for both case, the `equation` complies with go's prefix alignment size.

### Variadic Function

If a function takes variable amount of params of same type is as a slice is called a variadic function.

```go
func money(taka ...int){
  fmt.Println(taka, len(taka), cap(taka)) //here len and cap will be equal
}

func main(){
  money(2,3,4,3,5,3,3,4,5)
}

```

### Basic types of Golang

- bool
- string
- int, int8, int16, int32, int64
- unit, uint8, uint16, uint32, unit64, uintptr
- byte - alias for unit8
- rune - alias for int32 - represents a unicode code point
- float32, float64
- complex64, complex128

**note** int, unit, unitptr are system depended either 32bit or 64bit

### Auto type conversion

Unlike other languages, Go does not allow auto type conversion

like

```go
var f float = 2.0
var z int = f
```

will through error. Not even int8 auto cast to int64 type. We need to exclusively cast each thing.
