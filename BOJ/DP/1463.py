import sys

N= int(sys.stdin.readline()) 
d = [-1 for _ in range(N+1)]
d[0]=0
d[1]=0
for num in range (2,len(d)):
    # if(d[num] != -1) :
    #     return d[num]
    a0 = 1000000
    a1 = 1000000
    if((num % 2) == 0) :
        a0 = d[num//2]
        
    if((num % 3) == 0) :
        a1 = d[num//3]
        
    a2 = d[num-1]
    
    d[num] = min(a0,a1,a2) + 1    
    
print(d[N])
