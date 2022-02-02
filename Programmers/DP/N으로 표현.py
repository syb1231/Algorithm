def solution(n, number):
    answer = -1
    
    
    val = [{} for _ in range(9)]

    if(n == number):
        return 1

    val[1][n] = 1
    for numberCount in range(2,9):
        if(numberCount%2):
            halfIndex = int(numberCount/2) +1
        else:
            halfIndex = int(numberCount/2)

        for i in range(1,halfIndex+1):
            for leftVal in val[i]:
                for rightVal in val[numberCount-i]:
                    val[numberCount][float(leftVal+rightVal)] = 1
                    val[numberCount][float(leftVal*rightVal)] = 1
        for i in range(1,numberCount):
            for leftVal in val[i]:
                for rightVal in val[numberCount-i]:
                    val[numberCount][float(leftVal-rightVal)] = 1
                    if(rightVal):
                        val[numberCount][float(leftVal/rightVal)] = 1
        for v in val[numberCount-1]:
            val[numberCount][float(str(v)+str(n))] = 1
            if(v<0):
                tmp = (float((str(n)+str(abs(v)))))*-1
                val[numberCount][tmp] = 1
            else:
                val[numberCount][float(str(n)+str(v))] = 1

        if(float(number) in val[numberCount]):
            answer = numberCount
            break

    return answer
