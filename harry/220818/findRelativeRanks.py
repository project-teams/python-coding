import heapq

def solution(score):
    pq = []
    size = len(score)
    for i in range(size):
        heapq.heappush(pq, (-score[i], i))

    answer = [""] * size

    for i in range(size):
        num, idx = heapq.heappop(pq)
        if i == 0:
            answer[idx] = "Gold Medal"
        elif i == 1:
            answer[idx] = "Silver Medal"
        elif i == 2:
            answer[idx] = "Bronze Medal"
        else:
            answer[idx] = str(i + 1)
    
    print(answer)



score = [5,4,3,2,1]
score = [10,3,8,9,4]
solution(score)