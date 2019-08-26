# target url
https://medium.com/learning-the-go-programming-language/calling-go-functions-from-other-languages-4c7d8bcc69bf

# summary
* The package must be a main package. The compiler will build the package and all of its dependencies into a single shared object binary.
* The source must import the pseudo-package “C”.
* Use the //export comment to annotate functions you wish to make accessible to other languages.
* An empty main function must be declared.
* `go build -o awesome.so -buildmode=c-shared main.go`

注意点をソースに書き込みたかったけど、コメントでannotateしている==parseされている==コメントがかけない、みたい
