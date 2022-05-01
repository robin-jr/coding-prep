pad = {
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': ['0']
}


def phoneNumberMnemonics(phoneNumber):
    # return helper(phoneNumber, ['']*len(phoneNumber))
    mnemonics = ['']
    for e in phoneNumber:
        l = len(mnemonics)
        newMnemonics = []
        for i in range(l):
            c = mnemonics[i]
            for f in pad.get(e):
                newMnemonics.append(c+f)
        mnemonics = newMnemonics
    return mnemonics


def helper(phoneNumber, current, idx=0):
    result = []
    if idx == len(phoneNumber):
        result.append("".join(current))
        return result
    for e in pad.get(phoneNumber[idx]):
        current[idx] = e
        result += helper(phoneNumber, current, idx+1)
    return result


x = phoneNumberMnemonics("1905")
print(x)
