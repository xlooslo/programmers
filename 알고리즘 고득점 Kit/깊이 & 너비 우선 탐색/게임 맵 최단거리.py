# bfs 풀이법
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1 for j in range(m)] for i in range(n)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
        
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited[n-1][m-1]
  

# dfs 풀이법은 효율성에서 떨어짐
"""def solution(maps):
    answer = 9999
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[20001 for j in range(m)]for i in range(n)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def dfs(x, y, count):
        nonlocal answer
        
        if x == n-1 and y == m-1:
            visited[n-1][m-1] = count
            answer = min(answer, count)
            return
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if maps[nx][ny] == 1 and visited[nx][ny] > count:
                visited[nx][ny] = count
                dfs(nx, ny, count+1)
        return
    
    dfs(0, 0, 1)
    
    if visited[n-1][m-1] == 20001:
        answer = -1
        
    return answer"""
