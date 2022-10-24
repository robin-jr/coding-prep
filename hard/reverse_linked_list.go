package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func ReverseLinkedList(head *LinkedList) *LinkedList {
	var prev *LinkedList
	curr := head
	for curr != nil {
		t := curr.Next
		curr.Next = prev
		prev = curr
		curr = t
	}
	return prev
}
