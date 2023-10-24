def solution (blocks):
    n = len(blocks)
    left = [1]*n
    right = [1]*n

    for i in range (1,n):
        if blocks[1] >= blocks[i-1]:
            left[i] = left [i-1] + 1
    
    for i in range (n-2, -1, -1):
        if blocks[1] >= blocks[i+1]:
            left[i] = left [i+1] +1

    max_distance = 0
    for i in range(n):
        max_distance = max(max_distance, left [i], right[i])

    
    return max_distance

blocks = [2,6,8,5]
result = solution(blocks)

print("The longest possible distance between the frogs is:", result)

blocks = [1,5,5,2,6]
result = solution(blocks)

print("The longest possible distance between the frogs is:", result)


blocks = [1,1]
result = solution(blocks)

print("The longest possible distance between the frogs is:", result)   
