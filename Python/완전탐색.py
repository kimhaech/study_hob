def solution(answers):
    answer = [0, 0, 0]
    loser1 = [1, 2, 3, 4, 5] # %5
    loser2 = [2, 1, 2, 3, 2, 4, 2, 5] # %8
    loser3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # %10
    
    for i in range(len(answers)):
        if answers[i] == loser1[i%5]:
            answer[0] += 1
        if answers[i] == loser2[i%8]:
            answer[1] += 1
        if answers[i] == loser3[i%10]:
            answer[2] += 1
    
    max_val = max(answer) # 최대값
    result = []
    for i in range(3):
        if answer[i] == max_val:
            result.append(i+1)
        
    return result