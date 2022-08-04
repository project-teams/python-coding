def maxArea(height) -> int:
    area = first = 0
    last = len(height)-1
    while last > first:
        h = min(height[first], height[last])
        w = last - first
        if height[first] < height[last]:
            first += 1
        else:
            last -= 1
        area = max(area, w*h)


    print(area)

maxArea([1,8,6,2,5,4,8,3,7])