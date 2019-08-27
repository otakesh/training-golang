package main

/*
#include <stdio.h>
#include <stdlib.h>
static void myprint(char* s) {
  printf("%s\n", s);
}
*/
import "C"

import (
	"unsafe"
)

//export Exmain
func Exmain() {
	cs := C.CString("Hello from stdio")
	C.myprint(cs)
	C.free(unsafe.Pointer(cs))
	// Output:
	// Hello from stdio
}

func main() {}
