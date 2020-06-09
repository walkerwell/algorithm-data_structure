package main

import "fmt"

/***
第268题：不使用运算符 + 和 - ，计算两整数 a 、b 之和。

*/
func numsSum(a, b int) int {
	for b != 0 {
		temp := a ^ b
		b = (a & b) << 1
		a = temp
	}
	return a
}

/**
第231题：给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

*/
func is2(n int) bool {
	if n > 0 && n&(n-1) == 0 {
		return true
	}
	return false
}

/**
一个整数数中1的个数
*/
func oneNums(n int) int {
	res := 0
	for n > 0 {
		if n&1 == 1 {
			res += 1
		}
		n = n >> 1
	}
	return res
}

func main() {
	fmt.Println("oneNums:", oneNums(3))
	fmt.Println("is2:", is2(1))
	fmt.Println(numsSum(3, 5))
}
