package main

import "fmt"

type ListNode struct {
	val  int
	next *ListNode
}

func makeNodes(n int) *ListNode {
	if n < 1 {
		return nil
	}
	head := &ListNode{}
	result := head
	for i := 0; i < n; i++ {
		head.val = i
		if i < n-1 {
			head.next = &ListNode{}
			head = head.next
		}
	}
	return result
}
func traverse(head *ListNode) {
	for head != nil {
		fmt.Print(head.val, "->")
		head = head.next
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
	fast := head.next
	for head != nil && fast != nil && fast.next != nil {
		if head == fast {
			return true
		}
		head = head.next
		fast = fast.next.next
	}
	return false
}

/**
合并两个有序数组
*/
func mergeSortedLink(l1, l2 *ListNode) *ListNode {
	result := &ListNode{}
	p := result
	for l1 != nil && l2 != nil {
		if l1.val > l2.val {
			p.next = l2
			p = p.next
			l2 = l2.next
		} else {
			p.next = l1
			p = p.next
			l1 = l1.next
		}
	}
	if l1 != nil {
		p.next = l1
	} else {
		p.next = l2
	}
	return result
}

/*
删除链表的第N个节点
*/
func deleteNElement(head *ListNode, n int) *ListNode {
	result := &ListNode{}
	result.next = head
	pre := result
	i := 1
	for i < n {
		pre = head
		head = head.next
		i++
	}
	pre.next = pre.next.next
	return result.next
}

/**
删除链表中倒数第N个节点
*/
func deleteLastNElement(head *ListNode, n int) *ListNode {
	result := &ListNode{}
	result.next = head
	p := result
	pre := p
	i := 1
	for head != nil {
		if i >= n {
			pre = p
			p = p.next
		}
		head = head.next
		i++
	}
	pre.next = pre.next.next
	return result.next
}

func main() {
	head := makeNodes(10)
	traverse(head)
	head = deleteNElement(head, 8)
	traverse(head)

	head = makeNodes(10)
	head = deleteLastNElement(head, 3)
	traverse(head)
}
