package main

import "C"
import (
	"fmt"
	"time"
)

//export Start
func Start() {
	go func() {
		for now := range time.Tick(1 * time.Second) {
			fmt.Printf("%v\n", now)
		}
	}()
	println("end of go Start")
}

func main() {}
