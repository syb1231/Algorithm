def solution(record):
    answer = []
    human = {}
    for reco in record:
        r = reco.split(' ')
        if(r[0] != "Leave"):
            human[r[1]] = [r[2]]
    for reco in record:
        r = reco.split(' ')
        if(r[0] == "Enter"):
            answer.append(human[r[1]][0]+"님이 들어왔습니다.")
        elif(r[0] == "Leave"):
            answer.append(human[r[1]][0]+"님이 나갔습니다.")
    return answer
