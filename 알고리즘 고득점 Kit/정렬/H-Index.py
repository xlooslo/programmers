# 처음에는 4 4 4 2 1 1일 때 배열에 있는 값 중에 H-Index가 결정된다고 생각했으나
# H-Index는 꼭 배열에 있는 값이 아니어도 된다는 것을 알게 됐다.
# 위의 예시에서 답은 3이다.
def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    count = 1
    answer = 0
    
    for i in range(n):
        if citations[i] >= count:
            answer = count
        count += 1
    
    return answer
