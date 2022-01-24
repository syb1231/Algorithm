from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
def cal():
    n = int(input())
    info = []
    for i in range(n):
        info.append(input()[:-1])
    info.sort()
    for i in range(len(info)-1):
        if(info[i] == info[i+1][:len(info[i])]):
            print('NO')
            return
    print('YES')



t = int(input())
for i in range(t):
    cal()


# 문자열에서 정렬에 대한 생각을 뺴지 말자
