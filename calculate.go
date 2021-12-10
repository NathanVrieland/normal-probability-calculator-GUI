// Calculate.go
// Author: Nathan Vrieland
// Estimates probability by taking reimann sums of standard normal curve function
package main

import (
	"fmt"
	"runtime"
	"time"
)

// returns standard z-score
func z(mean float64, stdev float64, value float64) float64 {
	return (value - mean) / stdev
}

func main() {
	var NUM_RECTANGLES = 100000000
	var mean, stdev, x0, xn float64
	{
		fmt.Scan(&mean)
		fmt.Scan(&stdev)
		fmt.Scan(&x0)
		fmt.Scan(&xn)
	} // inputs
	Start :=time.Now()
    fmt.Print("Alpha: ")
	fmt.Printf("%.16f\n",goGetSum(z(mean, stdev, x0), z(mean, stdev, xn), NUM_RECTANGLES, runtime.NumCPU()))

	duration := time.Since(Start)
	fmt.Println("Compute Time: " + fmt.Sprint(duration))
}