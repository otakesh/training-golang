package main

/*
#include <stdlib.h>
typedef int BytesFunc(char*, int, char*, int, char*, int);
static int Handler_BytesFunc(BytesFunc *f, void *b0, int l0, void *b1, int l1, void *b2, int l2) {
	return f(b0, l0, b1, l1, b2, l2);
}
*/
import "C"
import "unsafe"

func string2cbytes(s string) (unsafe.Pointer, C.int) {
	b := []byte(s)
	return C.CBytes(b), C.int(len(b))
}

//export CallbackBytesFunc
func CallbackBytesFunc(cfn *C.BytesFunc) int {
	bp0, l0 := string2cbytes("Morning Python!")
	defer C.free(bp0)
	bp1, l1 := string2cbytes("Hello Python!")
	defer C.free(bp1)
	bp2, l2 := string2cbytes("See you!")
	defer C.free(bp2)
	res := C.Handler_BytesFunc(cfn, bp0, l0, bp1, l1, bp2, l2)
	return int(res)
}

/*
##export RetByteSlice
func RetByteSlice() []byte {
	return []byte("See you again")
}
issue How to recieve GoSlice by python.ctypes
https://golang.org/cmd/cgo/#hdr-Go_references_to_C
*/

func main() {}
