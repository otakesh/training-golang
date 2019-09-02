package main

/*
#include <stdlib.h>
typedef struct { char *data; int len; } ByteArray;
typedef int BytesFunc(ByteArray, ByteArray, ByteArray);
static int Handler_BytesFunc(BytesFunc *f, void *b0, int l0, void *b1, int l1, void *b2, int l2) {
	ByteArray ba0 = {b0, l0};
	ByteArray ba1 = {b1, l1};
	ByteArray ba2 = {b2, l2};
	return f(ba0, ba1, ba2);
}
*/
import "C"
import "unsafe"

func byte2Cbyte(b []byte) (unsafe.Pointer, C.int) {
	return C.CBytes(b), C.int(len(b))
}

//export CallbackBytesFunc
func CallbackBytesFunc(cfn *C.BytesFunc) int {
	bp0, l0 := byte2Cbyte([]byte("Morning Python!"))
	defer C.free(bp0)
	bp1, l1 := byte2Cbyte([]byte("Hello Python!"))
	defer C.free(bp1)
	bp2, l2 := byte2Cbyte([]byte("See you!"))
	defer C.free(bp2)
	res := C.Handler_BytesFunc(cfn, bp0, l0, bp1, l1, bp2, l2)
	return int(res)
}

/*
##export RetByteSlice
func RetByteSlice() []byte {
	return []byte("See you again")
}
issue How to recieve GoSlice by embedded C
https://golang.org/cmd/cgo/#hdr-Go_references_to_C
*/

func main() {}
