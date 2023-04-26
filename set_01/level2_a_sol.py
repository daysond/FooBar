


# mathematical way
# root = 2^(h-1), root of left subtree = root - 2^h (where h is the height of the subtree), root of right subtree = root - 1 

def findNode(node, parent, height):
    
    height -= 1
    leftRoot = parent - 2**height
    rightRoot = parent - 1

    if leftRoot == node or rightRoot == node:
        return parent
    
    nextRoot = leftRoot if node < leftRoot else rightRoot
    
    return findNode(node, nextRoot, height)
    
def solution(h, q):
    
    res = []
    root = 2 ** h -1
    for node in q:
        if node == root:
            res.append(-1)
        else:
            res.append(findNode(node, root, h))

    return res

# l = solution(5, [19, 14, 28])
# print(l)
# l = solution(3, [1, 4, 7])
# print(l)
# l = solution(3, [7, 3, 5, 1])
# print(l)


# traversing the whole tree... kinda bad O(n) for sure 
def solution2(h, q):
    
    dict = {}
    for num in q:
        dict[num] = -1
    
    postTraversal(h, dict, 1, 0)
    res = [dict[key] for key in q]
    return res

def postTraversal(height, result, currentHeight, currentIndex):
    
    if currentHeight == height:
        return currentIndex + 1
    
    newHeight = currentHeight + 1
    child1 = postTraversal(height, result, newHeight, currentIndex)
    child2 = postTraversal(height, result, newHeight, child1)
    
    parent = child2 + 1
    if child1 in result:
        result[child1] = parent
    if child2 in result:
        result[child2] = parent

    return parent




import time
start_time = time.time()
for i in range(1000000):
    solution(5, (19, 15, 28))

end_time = time.time()
total_time = end_time - start_time
print(f"Total 1 time taken: {total_time:.2f} seconds")

start_time = time.time()
for i in range(1000000):
    solution2(5, (19, 15, 28))

end_time = time.time()
total_time = end_time - start_time
print(f"Total 2 time taken: {total_time:.2f} seconds")


