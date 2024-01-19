from collections import deque

def solution(people, limit):
    ans = 0

    people = deque(sorted(people))

    while len(people) > 0:
        if len(people) == 1 or people[-1] + people[0] > limit:
            people.pop()
            ans += 1

        else:
            people.pop()
            people.popleft()
            ans += 1

    return ans
