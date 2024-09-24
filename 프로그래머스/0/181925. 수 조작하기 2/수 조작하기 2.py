def solution(numlog):
    answer = ''
    for i in range(len(numlog)) :
        if i == 0 :
            continue
        else :
            if (numlog[i] - numlog[i-1]) == 1 :
                answer += 'w'
            elif (numlog[i] - numlog[i-1]) == -1 :
                answer += 's'
            elif (numlog[i] - numlog[i-1]) == 10 :
                answer += 'd'
            elif (numlog[i] - numlog[i-1]) == -10 :
                answer += 'a'
    return answer