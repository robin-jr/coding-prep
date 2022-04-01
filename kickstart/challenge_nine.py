def get_minimum_number_divisible_by_nine(n):
    number =str(n)
    if n%9 ==0:
        return number[0]+"0"+number[1:]
    else:
        res=""
        number_to_add = 9-(n%9)
        for idx,val in enumerate(number):
            if number_to_add <  int(val):
                return res + str(number_to_add) + number[idx:]
            else:
                res+=val
        return res+str(number_to_add)

T= int(input())
for i in range(T):
    n = int(input())
    x = get_minimum_number_divisible_by_nine(n)
    print("Case #{}: {}".format(i+1,x))
