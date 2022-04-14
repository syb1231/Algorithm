def solution(A, B):
    answer = 0
    pointA = 0
    pointB = 0
    A.sort()
    B.sort()
    while(pointB<len(B)):
        if(B[pointB]>A[pointA]):
            pointB += 1
            pointA += 1
            answer +=1
            
        else:
            pointB += 1

    return answer
