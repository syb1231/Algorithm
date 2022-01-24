from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
visited = {}
ans = 0
def cal (init,target):
    while(len(init) != len(target)):
        if(target[-1] == 'A'):
            target = target[0:-1]
        else:
            target = target[0:-1]
            tmp = ""
            for i in target:
                tmp = i + tmp
            target = tmp

    if(init == target):
        print(1)
    else:
        print(0)   
    

init = input()[:-1]
target = input()[:-1]
cal(init,target)

# 문자열 문제가 그리디랑 비슷한듯 결국에 어떻게 풀어갈 것이냐
