from itertools import permutations
import copy
import math
def isPerfect(target):
    count = 0
    if(len(target) == 0):
        return 1
    if(target[0] == '('):
        count +=1
    else:
        count -= 1
    index = 1    
    while(count>=0 and index<len(target)):
        if(target[index] == '('):
            count += 1
        else:
            count -= 1
        index += 1
    if(count <0):
        return 0
    else:
        return 1

def recursuion(target):
    count = 0
    if(len(target) == 0):
        return '',''
    if(target[0] == '('):
        count +=1
    else:
        count -= 1
    index = 1
    while(index<len(target)):
        if(target[index] == '('):
            count += 1
        else:
            count -= 1
        if(not count):
            break
        index += 1
    return target[:index+1],target[index+1:]

def solution(p):
    if not p:
        return ""
    u, v = recursuion(p)
    if isPerfect(u):
        return u + solution(v)
    else:
        answer = '('

        answer += solution(v)
        answer += ')'
        for t in u[1:len(u) - 1]:
            if t == '(':
                answer += ')'
            else:
                answer += '('
        return answer
