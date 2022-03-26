import heapq

def solution(jobs):
    answer = 0
    minus = 0
    now= 0
    forwardNow = 0
    heap = []
    jobs.sort(key=lambda x:x[0])
    for j in jobs:
        minus += j[0]

    while(now<len(jobs)):
        while(now<len(jobs) and forwardNow>=jobs[now][0]):
            heapq.heappush(heap,jobs[now][1])
            now += 1
        if(heap): 
            forwardNow += heapq.heappop(heap)
            answer += forwardNow
        elif(now<len(jobs)):
            forwardNow = jobs[now][0]

    while(heap):
        forwardNow += heapq.heappop(heap)
        answer += forwardNow
            
    return (answer-minus) // len(jobs)
