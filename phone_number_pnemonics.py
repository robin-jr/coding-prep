pad = {
    '1':['1'],
    '2':['a', 'b', 'c'],
    '3':['d', 'e', 'f'],
    '4':['g', 'h', 'i'],
    '5':['j', 'k', 'l'],
    '6':['m', 'n', 'o'],
    '7':['p', 'q', 'r', 's'],
    '8':['t', 'u', 'v'],
    '9':['w', 'x', 'y', 'z'],
    '0':['0']
}
def phoneNumberMnemonics(phoneNumber):
    mnemonics =['']
    for e in phoneNumber:
        l = len(mnemonics)
        newMnemonics = []
        for i in range(l):
            c = mnemonics[i]
            for f in pad.get(e):
                newMnemonics.append(c+f)
        mnemonics = newMnemonics
    return mnemonics

x = phoneNumberMnemonics("1905")
print(x)