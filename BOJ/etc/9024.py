from collections import deque
from itertools import combinations
import sys
import copy
import heapq
input = sys.stdin.readline
T=int(input())
for test_case in range(T):
    answer = [float('inf'),-1]
    n,k = map(int,input().split())
    info = list(map(int,input().split()))
    info.sort()
    for i in range(n):
        start = i+1
        end = n-1 
        while(start<=end):
            mid = (start + end) // 2
            val = info[mid]+info[i]
            
            if(val > k):
                end = mid - 1
            else:
                start = mid + 1

            if(answer[0] == abs(val-k)):
                answer[1] += 1
            elif(answer[0] > abs(val-k)):
                answer[1] = 1
                answer[0] = abs(val-k)

    print(answer[1])
        

