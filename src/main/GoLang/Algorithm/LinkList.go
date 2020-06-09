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
	head := ListNode{}
	result := head
	for i := 0; i < n; i++ {
		head.val = i
		if i < n-1 {
			head.next = &ListNode{}
			head = *head.next
		}
	}
	return &result
}
func traverse(head *ListNode) {
	for head != nil {
		fmt.Println(head.val)
		head = head.next
	}
}
func main() {
	head:=makeNodes(10)
	traverse(head)
}

/**
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
