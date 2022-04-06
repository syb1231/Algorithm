class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = {}
        arr.sort()
        for a in arr:
            if(count.get(a)):
                count[a] += 1
            else:
                count[a] = 1
        arrOnly = []
        for c in count:
            arrOnly.append(c)
            
        if(target==0):
            if(count.get(0)):
                tmp1 = (count[0]-1) * count[0]
                tmp2 = tmp1 * (count[0] -2)
                tmp2 //= 6
                return tmp2 % 1000000007 
            else:
                return 0
        answer = 0
        for i in range(len(arrOnly)):
            nTarget = target - arrOnly[i]
            start = 0
            end = i-1
            while(start<end):
                tmp = arrOnly[start] + arrOnly[end]
                if(tmp == nTarget):
                    tmpS = count[arrOnly[start]] * count[arrOnly[end]]  
                    tmp2 = tmpS * count[arrOnly[i]]
                    answer += tmp2
                if(tmp<nTarget):
                    start += 1
                else:
                    end -= 1
            if(count[arrOnly[i]]>1):
                nTarget = target - arrOnly[i]*2
                if(nTarget != arrOnly[i] and count.get(nTarget)):
                    tmp1 = count[nTarget] * count[arrOnly[i]]
                    tmp2 = tmp1 * (count[arrOnly[i]] -1)
                    tmp2 //= 2
                    answer += tmp2
            if(count[arrOnly[i]]>2 and target == arrOnly[i]*3):
                    tmp1 = (count[arrOnly[i]]-1) * count[arrOnly[i]]
                    tmp2 = tmp1 * (count[arrOnly[i]] -2)
                    tmp2 //= 6
                    answer += tmp2
            answer = answer % 1000000007       

                
        return answer
