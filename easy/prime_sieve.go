package main

import (
	"fmt"
)

func generate() chan int {
	c := make(chan int)
	go func() {
		for i := 2; ; i++ {
			c <- i
		}
	}()
	return c
}
func filter(a chan int, prime int) chan int {
	c := make(chan int)
	go func() {
		for n := range a {
			if n%prime != 0 {
				c <- n
			}
		}
	}()
	return c
}
func main() {
	a := generate()
	for {
		prime := <-a
		if prime > 1000 {
			return
		}
		fmt.Println(prime)
		a = filter(a, prime)
	}
}
