def solution(numbers, target):
    global count
    count = 0
    n = len(numbers)

    def dfs(i, result):
        global count
        if i == n:
            if result == target:
                count += 1
                return
        else:
            dfs(i+1, result + numbers[i])
            dfs(i+1, result - numbers[i])
        
    dfs(0, 0)
    return count
