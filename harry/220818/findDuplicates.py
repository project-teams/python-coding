import heapq

def solution(nums):
    dic = dict()
    pq = []

    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        if dic[num] == 2:
            heapq.heappush(pq, num)

    answer = []
    for _ in range(len(pq)):
        answer.append(heapq.heappop(pq))
    
    print(answer)
    return answer


nums = [4,3,2,7,8,2,3,1]
solution(nums)