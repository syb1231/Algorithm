import sys
from collections import deque
import heapq
input = sys.stdin.readline
n  = int(input())

info = "01"
reverse = False
left = n

while(left>2):
    num = 1
    powNum = 0
    while(num<left):
        num = num*2
    left = left - (num//2)
    reverse = not reverse

if(left):
    left -= 1
if(reverse):
    left = not left
print(info[left])
