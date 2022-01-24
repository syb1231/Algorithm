    from collections import deque
    from itertools import combinations
    import sys
    import copy
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
      
        #if parent[a] == a: # a가 루트 노드이면, a 반환
        #return a
        #p = find(parent[a]) # 루트 노드 탐색
        #parent[a] = p # a의 루트 노드 갱신
        #return parent[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    n,m = map(int,input().split())
    parent = {}
    for i in range(0, n+1):
        parent[i] = i

    for i in range(m):
        a,b,c = map(int,input().split())
        if(a==0):
            union(b,c)
        else:
            if(find(b) == find(c)):
                print('YES')
            else:
                print('NO')
