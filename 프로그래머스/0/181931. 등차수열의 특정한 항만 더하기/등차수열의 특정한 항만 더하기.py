def solution(a, d, included):
    answer = 0
    for index, i in enumerate(included) :
        if i == True:
            answer += (a+ d*(index))
    return answer