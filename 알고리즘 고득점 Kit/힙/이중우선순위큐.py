import heapq

def solution(operations):
    answer = []
    heap = []

    for operation in operations:
        alp, num = operation.split()
        num = int(num)

        if alp == 'I':
            heapq.heappush(heap, num)

        elif alp == 'D':
            if not heap:
                continue

            elif num == 1:
                heap = list(heap)
                max_value = max(heap)
                heap.remove(max_value)
                heapq.heapify(heap)

            else:
                heapq.heappop(heap)

    max_value = min_value = 0
    if heap:
        min_value = heap[0]
        heap = list(heap)
        max_value = max(heap)

    answer.append(max_value)
    answer.append(min_value)

    return answer
