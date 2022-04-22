def solution(str1, str2):
    answer = 0
    str1Check = {}
    str2Check = {}
    
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1)-1):
        ord1 = ord(str1[i])
        ord2 = ord(str1[i+1])
    
        if(ord("A") <= ord1 <= ord('Z') and ord("A") <= ord2 <= ord('Z')):
            if(str1Check.get(str1[i] + str1[i+1])):
                str1Check[str1[i] + str1[i+1]] += 1
            else:
                str1Check[str1[i] + str1[i+1]] = 1

    for i in range(len(str2)-1):
        ord1 = ord(str2[i])
        ord2 = ord(str2[i+1])
    
        if(ord("A") <= ord1 <= ord('Z') and ord("A") <= ord2 <= ord('Z')):
            if(str2Check.get(str2[i] + str2[i+1])):
                str2Check[str2[i] + str2[i+1]] += 1
            else:
                str2Check[str2[i] + str2[i+1]] = 1

    U = {}
    N = {}
    for strTmp in str1Check:
        U[strTmp] = str1Check[strTmp]
        N[strTmp] = str1Check[strTmp]

    for strTmp in str2Check:
        if(U.get(strTmp)):
            U[strTmp] = max(U[strTmp],str2Check[strTmp])
        else:
            U[strTmp] = str2Check[strTmp]
        
    for strTmp in N:
        if(str2Check.get(strTmp)):
            N[strTmp] = min(N[strTmp],str2Check[strTmp])
        else:
            N[strTmp] = 0


    nCount = 0
    uCount = 0

    for u in U:
        uCount += U[u]

    for n in N:
        nCount += N[n]
    # print(str1Check)
    # print(str2Check)
    # print(U)
    # print(N)
    if(uCount):
        return int((nCount/uCount * 65536) // 1)
    else:
        return 65536
