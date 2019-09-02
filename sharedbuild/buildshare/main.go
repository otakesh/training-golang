package main

import "C"

import (
	"fmt"
	"math"
	"sort"
	"sync"
	"unsafe"
)

var count int
var mtx sync.Mutex

//export Add
func Add(a, b int) int { return a + b }

//export Cosine
func Cosine(x float64) float64 { return math.Cos(x) }

//export Sort
func Sort(vals []int) { sort.Ints(vals) }

//export Log
func Log(msg string) int {
	mtx.Lock()
	defer mtx.Unlock()
	fmt.Println(msg)
	count++
	return count
}

//export retString
func retString() (*C.char, int) {
	msg := "this is retrun string"
	return C.CString(msg), len(msg)
}

//export retSlice
func retSlice() (unsafe.Pointer, int, int) {
	bmsg := []byte("this is return byte slice")
	return C.CBytes(bmsg), len(bmsg), cap(bmsg)
}

func main() {}

// https://medium.com/learning-the-go-programming-language/calling-go-functions-from-other-languages-4c7d8bcc69bf
// https://golang.org/cmd/cgo/#hdr-C_references_to_Go
