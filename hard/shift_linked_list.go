package main

import "fmt"

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func ShiftLinkedList(head *LinkedList, k int) *LinkedList {
	n := 0
	t := head
	tail := head
	for t != nil {
		n += 1
		tail = t
		t = t.Next
	}
	k = k % n
	if k == 0 {
		return head
	}
	if k > 0 {
		k = n - k
	} else {
		k = -k
	}
	fmt.Println(n, k)
	t = head
	for k > 1 {
		t = t.Next
		k--
	}
	fmt.Println(head.Value, tail.Value, t.Value)
	tail.Next = head
	head = t.Next
	t.Next = nil

	return head
}

func printList(x *LinkedList) {
	for x != nil {
		fmt.Print(x.Value, " -> ")
		x = x.Next
	}
	fmt.Print("\n")
}

func main() {
	// headOne := &LinkedList{1, &LinkedList{3, &LinkedList{5, &LinkedList{7, &LinkedList{9, nil}}}}}
	headOne := &LinkedList{0, &LinkedList{1, &LinkedList{2, &LinkedList{3, &LinkedList{4, &LinkedList{5, nil}}}}}}
	printList(headOne)
	x := ShiftLinkedList(headOne, 2)
	printList(x)
}
