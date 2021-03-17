package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}

	return i
}

func main() {
	sc.Split(bufio.ScanWords)
	n := nextInt()
	x := nextInt()
	f := true
	for i := 0; i < n; i++ {
		a := nextInt()
		if x != a {
			if f {
				fmt.Printf("%v", a)
				f = false
			} else {
				fmt.Printf(" %v", a)
			}
		}
	}
}
