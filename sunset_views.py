def sunsetViews(buildings, direction):
    left_maxs = [0]
    right_maxs =[0]

    for i in range(len(buildings)-1):
        left_maxs.append(max(left_maxs[i],buildings[i]))
    for i in range(len(buildings)-1,0,-1):
        right_maxs.insert(0,max(right_maxs[0],buildings[i]))
    
    result =[]
    
    if direction=="EAST":
        for i in range(len(buildings)):
            if buildings[i]>right_maxs[i]:
                result.append(i)
    elif direction=="WEST":
        for i in range(len(buildings)):
            if buildings[i]>left_maxs[i]:
                result.append(i)
    return result

buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"

x = sunsetViews(buildings, direction)
print(x)
