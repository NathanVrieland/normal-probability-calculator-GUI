// reimann.go
// Author: Nathan Vrieland
// back-end functions for Calculate.go
package main

import (
	"math"
)

// output of standardized normal curve f(x)
func normal_distro(x float64) float64 {
	var pi float64 = 3.14159265359
	var ret float64 = -(x * x)
	ret /= 2
	ret = math.Exp(ret)
	ret *= 1/math.Sqrt(2*pi)
	return ret
}

// returns: area of num rectanges between x0 and xn and outputs them to channel
func getSum(x0 float64, xn float64, num int) float64 {
	var ret float64 = 0
	var delta float64 = (xn - x0) / float64(num)
	var current float64 = x0
	for  i := 0; i < num; i++ {
		ret += delta * normal_distro(current + (delta / 2))
		current += delta
	}
	return ret
}

func getSumMP(x0 float64, xn float64, num int, channel chan float64) {
	channel <- getSum(x0, xn, num)
}

// returns: area of num rectangles between x0 and xn
// workload divided among threads
func goGetSum(x0 float64, xn float64, num int, threads int) float64 {
	sums := make(chan float64)
	var ret float64 = 0
	var threadDelta float64 = (xn-x0) / float64(threads)
	for i := 0; i < threads; i++ {
		go getSumMP(x0 + (float64(i) * threadDelta), x0 + (float64(i) * threadDelta) + threadDelta, num / threads, sums)
	}
	for i := 0; i < threads; i++ {
		ret += <- sums
	}
	return ret
}