package main

import (
	"fmt"
)

func abs(a int8) int8 {
	if a > 0 {
		return a
	} else {
		return -a
	}
}

/**
判断str是否是回文串
*/
func findStrIsLoop(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		if s[i] == s[j] || abs(int8(s[i])-int8(s[j])) == 'a'-'A' {
			i++
			j--
		} else if !((s[i] >= '0' && s[i] <= '9') || (s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
			i++
		} else if !((s[j] >= '0' && s[j] <= '9') || (s[j] >= 'a' && s[j] <= 'z') || (s[j] >= 'A' && s[j] <= 'Z')) {
			j--
		} else {
			//fmt.Println(i, j)
			//fmt.Println(s[i], s[j])
			//fmt.Println(string(s[i]), string(s[j]))
			//fmt.Println(s[i] - s[j])
			//fmt.Println(int(s[i]) - int(s[j]))
			//fmt.Println('A' - 'a')
			return false
		}
	}
	return true
}

func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		if !((s[i] >= '0' && s[i] <= '9') || (s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
			i++
		} else if !((s[j] >= '0' && s[j] <= '9') || (s[j] >= 'a' && s[j] <= 'z') || (s[j] >= 'A' && s[j] <= 'Z')) {
			j--
		} else if s[i] != s[j] {
			//fmt.Println(i, j)
			//fmt.Println(s[i], s[j])
			//fmt.Println(string(s[i]), string(s[j]))
			//fmt.Println(s[i] - s[j])
			//fmt.Println(int(s[i]) - int(s[j]))
			//fmt.Println('A' - 'a')
			return false
		} else {
			i++
			j++
		}
	}
	return true
}

func main() {
	fmt.Println(findStrIsLoop("OP"))
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))

}
