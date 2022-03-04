T= int(input())
for case_no in range(T):
    no_of_bags, no_of_kids=map(int,input().split())
    no_of_candies=sum(map(int,input().split()))
    remaining_no_of_candies= no_of_candies%no_of_kids
    print("Case #{}: {}".format(case_no+1,remaining_no_of_candies))