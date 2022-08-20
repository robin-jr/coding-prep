def min_rewards(scores):
    n = len(scores)
    rewards = [1 for _ in range(n)]
    
    for i in range(1,n):
        if scores[i-1]< scores[i]: rewards[i]+=rewards[i-1]     
    
    for i in range(n-1, 0, -1):
        if scores[i-1]> scores[i] and rewards[i-1]<=rewards[i]: 
            rewards[i-1]=rewards[i]+1
    
    print(rewards)
    return sum(rewards)


scores = [8,4,2,1,3,6,7,9,5]
# scores = [0, 4, 2, 1, 3]
# scores = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
scores = [5,10]
scores = [10,5]
x = min_rewards(scores)
print(x)

