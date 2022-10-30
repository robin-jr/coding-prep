package main

func InterweavingStrings(one, two, three string) bool {
	if len(three) == 0 {
		return len(one) == 0 && len(two) == 0
	}
	if len(one) > 0 && len(two) > 0 && three[0] == one[0] && three[0] == two[0] {
		return InterweavingStrings(one[1:], two, three[1:]) || InterweavingStrings(one, two[1:], three[1:])
	}
	if len(one) > 0 && three[0] == one[0] {
		return InterweavingStrings(one[1:], two, three[1:])
	}
	if len(two) > 0 && three[0] == two[0] {
		return InterweavingStrings(one, two[1:], three[1:])
	}
	return false
}
