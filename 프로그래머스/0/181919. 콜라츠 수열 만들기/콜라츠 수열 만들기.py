def solution(n):
    answer = []
    answer.append(n)
    while answer[-1] != 1:
        if answer[-1]%2 == 0:
            answer.append(answer[-1]/2)
        elif answer[-1]%2==1:
            answer.append(answer[-1]*3+1)
    return answer