def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x:x[0])
    n=len(intervals)
    result=[intervals[0]]
    for i in range(1,n):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1]=max(result[-1][1],intervals[i][1])
        else:
            result.append(intervals[i])
    return result

intervals=[
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]
x=mergeOverlappingIntervals(intervals)
print(x)