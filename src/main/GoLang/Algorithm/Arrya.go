package main

import "fmt"

/***
第350题：两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
*/
func intersect(nums1 []int, nums2 []int) []int {
	m0 := map[int]int{}
	for _, v := range nums1 {
		m0[v] += 1
	}
	k := 0
	for _, v := range nums2 {
		if m0[v] > 0 {
			m0[v] -= 1
			nums2[k] = v
			k++
		}
	}
	return nums2[0:k]
}

/**
两个排序好的数组 找交集
*/
func inter(nums1 []int, nums2 []int) []int {
	i, j, k := 0, 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] == nums2[j] {
			nums2[k] = nums1[i]
			i++
			j++
			k++
		} else if nums1[i] < nums2[j] {
			i++
		} else {
			j++
		}
	}
	return nums2[0:k]
}

func main() {

	fmt.Println("intersect:", intersect([]int{1, 2, 3, 4}, []int{2, 5, 3, 4}))
	fmt.Println("inter:", inter([]int{1, 2, 3, 4, 4, 13}, []int{1, 2, 3, 9, 10}))
}
