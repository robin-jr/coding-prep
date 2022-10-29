package main

import "fmt"

// This is an input struct. Do not edit.
type LinkedList struct {
	Value int
	Next  *LinkedList
}

func MergeLinkedLists(headOne *LinkedList, headTwo *LinkedList) *LinkedList {
	if headTwo.Value < headOne.Value {
		headOne, headTwo = headTwo, headOne
	}
	first, second := headOne, headTwo
	var firstPrev *LinkedList
	for first != nil && second != nil {
		if second.Value < first.Value {
			t := second.Next
			second.Next = first
			firstPrev.Next = second
			second = t
			firstPrev = firstPrev.Next
		} else {
			firstPrev = first
			first = first.Next
		}
	}
	if second != nil {
		firstPrev.Next = second
	}
	return headOne
}

func printList(x *LinkedList) {
	for x != nil {
		fmt.Print(x.Value, " -> ")
		x = x.Next
	}
	fmt.Print("\n")
}

func main() {
	headOne := &LinkedList{1, &LinkedList{3, &LinkedList{5, &LinkedList{7, &LinkedList{9, nil}}}}}
	headTwo := &LinkedList{2, &LinkedList{4, &LinkedList{6, &LinkedList{8, &LinkedList{10, nil}}}}}
	x := MergeLinkedLists(headOne, headTwo)
	printList(x)
}
