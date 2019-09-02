# use shared library writen in go

## build shared
[code example](./buildshare)
* https://golang.org/cmd/cgo/#hdr-C_references_to_Go
  * Using //export in a file places a restriction on the preamble
  * `//export <FUNCTION_NAME>`export directive の前にスペース入れない
* https://medium.com/learning-the-go-programming-language/calling-go-functions-from-other-languages-4c7d8bcc69bf
  * The package must be a main package. The compiler will build the package and all of its dependencies into a single shared object binary.
  * The source must import the pseudo-package “C”.
  * Use the //export comment to annotate functions you wish to make accessible to other languages.
  * An empty main function must be declared.
* `go build -o awesome.so -buildmode=c-shared main.go && python client.py`
* http://snowsyn.net/2016/09/11/creating-shared-libraries-in-go/
* https://dev.to/mattn/call-go-function-from-c-function-1n3
* exportした関数のタプル戻り値は、.restype = Strucutreで受けられる。Goのポインタは含めないのでCのポインタにする必要はある。

## pass callback function to go c-shared library
### Python ctypes
[code example](./ctypefunc)
* https://docs.python.org/ja/3/library/ctypes.html#callback-functions
  * C の呼び出し可能な関数ポインタを作成(create C callable function pointers)
  * https://docs.python.org/ja/3/library/ctypes.html#ctypes.CFUNCTYPE
  * デコレータで書ける。
  POINTER(c_int)で渡されるのは、LP_c_intでArrayの先頭ポインタなので、長さとか終端とかない。普通にCのポインタ。
  ~~ポインタはリストに変換される。~~
  libc.qsortの要求するcmp関数の仕様が、ポインタ引数2個、戻り値intなのでこのCFUNCTYPEになる
```
@CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
def py_cmp_func(a, b):
    print("py_cmp_func", a[0], b[0])
    return a[0] - b[0]
```
* lib.soのロード
  * argtypes, restype
  * https://docs.python.org/ja/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes
  * https://docs.python.org/ja/3/library/ctypes.html#loading-dynamic-link-libraries
  * platform.system()で、Windows、Darwin、Linuxが区別できるので、使う標準ライブラリは切り替えられる
  * https://qiita.com/kjunichi/items/0bf0256ff178f7ab5514


### use embeded C code in GO
[code example](./embedded_C)
* https://golang.org/cmd/cgo/#hdr-Go_references_to_C
  * If the import of "C" is immediately preceded by a comment, that comment, called the preamble, is used as a header when compiling the C parts of the package
  * 埋込扱いされるのは、import Cの直前のコメントだけ
* https://golang.org/cmd/cgo/#hdr-Go_references_to_C
* https://qiita.com/r9y9/items/e6d879c9b7d4f2697593
  * https://coderwall.com/p/m_ma7q/pass-go-slices-as-c-array-parameters

### go(C) recieve python ctype FUNCTYPE as callback
[code example](./use_callback)
* https://golang.org/cmd/cgo/#hdr-Go_references_to_C
  * Calling C function pointers is currently not supported, however you can declare Go variables which hold C function pointers and pass them back and forth between Go and C. C code may call function pointers received from Go.
* https://docs.python.org/ja/3/library/ctypes.html#structures-and-unions
* https://docs.python.org/ja/3/library/ctypes.html#fundamental-data-types
* gohttplib
  * https://qiita.com/nothingcosmos/items/dd591055b9da1e713b9a
  * https://github.com/shazow/gohttplib/blob/master/gohttplib.go

## reference
* https://godoc.org/github.com/gophersjp/go/src/cmd/cgo
* https://qiita.com/yugui/items/e71d3d0b3d654a110188
* https://qiita.com/yugui/items/cc490d080e0297251090
* https://blog.golang.org/c-go-cgo

## environment

* python 3.6.9
* go version go1.12.5 darwin/amd64
