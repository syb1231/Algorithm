from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
answer = []
info =[[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
def dfs(digits,index,s):
    if(index == len(digits)):
        answer.append(s)
        return

    target = int(digits[index])
    if(target):
        for comb in list(combinations(info[target],1)):
            for c in comb:
                s += c
                dfs(digits,index+1,s)
                s = s[:-1]

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        global answer
        answer = []
        if(len(digits) == 0):
            return answer
        else:
            dfs(digits,0,'')
            return answer
        
