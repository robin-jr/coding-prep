package main

import "fmt"

type OrgChart struct {
	Name          string
	DirectReports []*OrgChart
}

func helper(root, reportOne, reportTwo *OrgChart) (int, *OrgChart) {
	count := 0
	if root == reportOne || root == reportTwo {
		count = 1
	}
	for _, v := range root.DirectReports {
		t, x := helper(v, reportOne, reportTwo)
		if x != nil {
			return 0, x
		}
		count += t
	}
	if count == 2 {
		return 0, root
	}
	return count, nil
}

func GetLowestCommonManager(org, reportOne, reportTwo *OrgChart) *OrgChart {
	_, chart := helper(org, reportOne, reportTwo)
	return chart
}

func main() {
	one, two := &OrgChart{"B", nil}, &OrgChart{"C", nil}
	top := &OrgChart{"A", []*OrgChart{one, two}}
	x := GetLowestCommonManager(top, one, two)
	fmt.Println(x.Name)
}
