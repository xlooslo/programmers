from collections import deque

def str_check(x, y):
    count = 0

    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1

    return count

def solution(begin, target, words):
    count = 0
    
    n = len(words)
    
    visited = [0 for _ in range(n)]
    
    queue = deque()
    queue.append((begin, count))
    
    while queue:
        word = queue.popleft()
        if word[0] == target:
            return word[1]
        
        for i in range(n):
            if visited[i] == 0 and str_check(word[0], words[i]) == 1:
                visited[i] = word[1] + 1
                queue.append((words[i], visited[i]))
    
    return 0
