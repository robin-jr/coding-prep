package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func FindLoop(head *LinkedList) *LinkedList {
	slowPtr, fastPtr := head.Next, head.Next.Next
	for slowPtr != fastPtr {
		slowPtr, fastPtr = slowPtr.Next, fastPtr.Next.Next
	}
	slowPtr = head
	for slowPtr != fastPtr {
		slowPtr, fastPtr = slowPtr.Next, fastPtr.Next
	}
	return slowPtr
}
