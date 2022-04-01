from numpy import prod

memo = {}

def get_hash(n):
    hash_list=[hex(0) for _ in range(10)]
    for e in str(n):
        hash_list[int(e)]+=hex(1)
    hash=""
    for e in hash_list:
        hash+=str(e)
    return hash

def solve(t):
    a, b = map(int, input().split(' '))
    count = 0
    for i in range(a, b + 1):
        cur = [int(x) for x in str(i)]
        hash_key=get_hash(i)
        if hash_key in memo:
            if memo[hash_key] == True:
                count += 1
            continue
        p = prod(cur)
        s = sum(cur)
        if p % s == 0:
            count += 1
            memo[hash_key] = True
        else:
            memo[hash_key] = False
    print('Case #' + str(t) + ': ' + str(count))


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        solve(i)
