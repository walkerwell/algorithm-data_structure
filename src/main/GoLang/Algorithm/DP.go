package main

import (
	"fmt"
)

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

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/***
第120题：给定一个三角形，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


[2],
[3,4],
[6,5,7],
[4,1,8,3]

*/
func trangleMinPathSum(trangle [4][]int) int {
	if len(trangle) < 1 {
		return 0
	}
	res := 10 << 10
	for i := 1; i < len(trangle); i++ {
		for j := 0; j < len(trangle[i]); j++ {
			if j == 0 {
				trangle[i][j] = trangle[i-1][j] + trangle[i][j]
			} else if j == len(trangle[i])-1 {
				trangle[i][j] = trangle[i-1][j-1] + trangle[i][j]
			} else {
				trangle[i][j] = min(trangle[i-1][j], trangle[i-1][j-1]) + trangle[i][j]
			}
		}
	}
	//for i, _ := range trangle {
	//	for j, _ := range trangle[i] {
	//		fmt.Print(trangle[i][j], " ")
	//	}
	//	fmt.Println()
	//}
	for _, a := range trangle[len(trangle)-1] {
		if res > a {
			res = a
		}
	}
	return res
}

/***
第64题：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
*/

func minPathSum(grid [3][]int) int {
	if len(grid) < 1 {
		return 0
	}
	l := len(grid)
	for i := 0; i < l; i++ {
		for j := 0; j < len(grid[i]); j++ {
			if i == 0 && j > 0 {
				grid[i][j] = grid[i][j-1] + grid[i][j]
			} else if i > 0 && j == 0 {
				grid[i][j] = grid[i-1][j] + grid[i][j]
			} else if i != 0 && j != 0 {
				grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
			}
		}
	}
	//for i, _ := range grid {
	//	for j, _ := range grid[i] {
	//		fmt.Print(grid[i][j], " ")
	//	}
	//	fmt.Println()
	//}
	return grid[l-1][len(grid[l-1])-1]
}

/***
打家劫舍
第198题：你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

dp[i] 小偷至i家能偷得得最大金额
*/
func findMaxValue(m []int) int {
	if len(m) < 1 {
		return 0
	}
	for i, _ := range m {
		if i == 0 {
			continue
		} else if i == 1 {
			m[i] = max(m[0], m[1])
		} else {
			m[i] = max(m[i-2]+m[i], m[i-1])
		}
	}
	res := 0
	for _, a := range m {
		if a > res {
			res = a
		}
	}
	return res
}

func add(a, b int) int {
	max_ := max(a, b)
	max_ = max_ << 1 & max_
	return max_ ^ min(a, b)
}




func main() {
	fmt.Println("findResult:", findResult(4))
	a := [9]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println("findLonger:", findLonger(a))
	fmt.Println("lengthOfLIS:", lengthOfLIS(a))
	/***
	[2],
	[3,4],
	[6,5,7],
	[4,1,8,3]
	*/
	trangle := [4][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}
	fmt.Println("trangleMinPathSum:", trangleMinPathSum(trangle))
	/**
	[
	  [1,3,1],
	  [1,5,1],
	  [4,2,1]
	]
	*/
	grid := [3][]int{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}}
	fmt.Println("minPathSum:", minPathSum(grid))
	fmt.Println("findMaxValue:", findMaxValue([]int{2, 7, 9, 3, 1}))
	fmt.Println("add:", add(12, 7))


}
