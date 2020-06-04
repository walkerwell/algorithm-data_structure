package main

import (
	"fmt"
)

func main() {
	fmt.Println(findResult(4))
	a := [9]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println(findLonger(a))
	fmt.Println(lengthOfLIS(a))
}

/**
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
*/
func findResult(n int) int {
	a := make([]int, n)
	a[0] = 1
	a[1] = 2
	for i := 2; i < n; i++ {
		a[i] = a[i-1] + a[i-2]
	}
	return a[n-1]
}

/**
最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和


dp[i] 表示以 nums[i] 结尾的连续子数组的最大和
如果要得到dp[i]，那么nums[i]一定会被选取。
*/
func findLonger(m [9]int) int {
	res := -999
	dp := make([]int, len(m))
	for i := 1; i < len(m); i++ {
		dp[i] = max(m[i], dp[i-1]+m[i])
		res = max(res, dp[i])
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/***
第300题：给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。


dp[i] 表示以nums[i]结尾的最长上升子序列的长度。
*/
func lengthOfLIS(nums [9]int) int {
	if len(nums) < 1 {
		return 0
	}
	dp := make([]int, len(nums))
	result := 1
	for i, a := range nums {
		dp[i] = 1
		for j := 0; j < i; j++ {
			if a > nums[j] {
				dp[i] = max(dp[j]+1, dp[i])
			}
		}
		result = max(result, dp[i])
	}
	return result
}

/***
每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


*/
