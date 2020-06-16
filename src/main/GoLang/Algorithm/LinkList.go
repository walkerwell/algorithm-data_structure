package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func makeNodes(n int) *ListNode {
	if n < 1 {
		return nil
	}
	head := &ListNode{}
	result := head
	for i := 1; i <= n; i++ {
		head.Val = i
		if i < n-1 {
			head.Next = &ListNode{}
			head = head.Next
		}
	}
	return result
}
func traverse(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, "->")
		head = head.Next
	}
	fmt.Println()
}

/**
检查链表中是否存在环
*/
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	fast := head
	for head != nil && fast != nil && fast.Next != nil {
		if head == fast || fast.Next == head {
			return true
		}
		head = head.Next
		fast = fast.Next.Next
	}
	return false
}

/**
合并两个有序链表
*/
func mergeSortedLink(l1, l2 *ListNode) *ListNode {
	result := &ListNode{}
	p := result
	for l1 != nil && l2 != nil {
		if l1.Val > l2.Val {
			p.Next = l2
			p = p.Next
			l2 = l2.Next
		} else {
			p.Next = l1
			p = p.Next
			l1 = l1.Next
		}
	}
	if l1 != nil {
		p.Next = l1
	} else {
		p.Next = l2
	}
	return result
}

/*
删除单链表的第N个节点
*/
func deleteNElement(head *ListNode, n int) *ListNode {
	result := &ListNode{}
	result.Next = head
	pre := result
	i := 1
	for i < n {
		pre = head
		head = head.Next
		i++
	}
	pre.Next = pre.Next.Next
	return result.Next
}

/**
删除单链表中的倒数第N个节点
*/
func deleteLastNElement(head *ListNode, n int) *ListNode {
	result := &ListNode{}
	result.Next = head
	p := result
	pre := p
	i := 1
	for head != nil {
		if i >= n {
			pre = p
			p = p.Next
		}
		head = head.Next
		i++
	}
	pre.Next = pre.Next.Next
	return result.Next
}

/**
判断单链表构成的字符 是否是回文串
应用快慢指针找到中间节点
当链表节点总数为 奇数的时候，slow就是中间节点，偶数的时候，slow指向的是中间节点的上一个节点
在找中介节点的过程中，将slow节点存起来，为了后续比较是否是回文
所以需要判断head.Next为空时，说明是奇数节点，那么就需要将栈顶除去
然后拿栈里面的元素和slow后面的元素挨个比较 判断是否是回文
*/
func LinkIsReverse(head *ListNode) bool {
	if head == nil {
		return false
	}
	slow, fast := head, head
	stack := make([]int, 0)
	index := 0
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		stack[index] = slow.Val
		index++
	}
	if head.Next == nil {
		index--
	}
	for slow.Next != nil {
		slow = slow.Next
		if slow.Val != stack[index] {
			return false
		}
		index--
	}
	return true
}

/**
单链表反转
*/
func LinkedReverse(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	res, pre := &ListNode{-1, nil}, head
	head = head.Next
	for head != nil || pre != nil {
		pre.Next = res
		res = pre
		pre = head
		if head != nil {
			head = head.Next
		}
	}
	return res
}

/**
判断链表是否存在相交节点
*/
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	pA, pB := headA, headB
	for pA != pB {
		if pA == nil {
			pA = headB
		} else {
			pA = pA.Next
		}
		if pB == nil {
			pB = headA
		} else {
			pB = pB.Next
		}
	}
	return pA
}

/**
最近最久未使用
*/
func LRU(head *ListNode) *ListNode {
	return nil
}

func main() {
	head := makeNodes(10)
	traverse(head)
	head = deleteNElement(head, 8)
	traverse(head)

	head = makeNodes(10)
	head = deleteLastNElement(head, 3)
	traverse(head)

	head = makeNodes(3)
	head = LinkedReverse(head)
	traverse(head)
}
