# 모든 숫자를 같은 자릿수로 만들어야 함
# 3 -> 333, 34 -> 344로 만드는 것이 가장 적합하나
# 굳이 그렇게 안 하고 333, 343434로 만들어 세자릿수로 자르는 풀이법

def solution(numbers):
    answer = ""

    numbers = list(map(str, numbers))

    numbers.sort(key = lambda x:x*3, reverse = True)        

    for i in numbers:
        answer += i

    if answer[0] == '0':
        answer = '0'

    return answer
