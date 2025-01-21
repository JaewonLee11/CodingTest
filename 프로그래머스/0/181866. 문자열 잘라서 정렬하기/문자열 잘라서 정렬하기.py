def solution(myString):
    answer = sorted(myString.split("x"))
    for i in range(answer.count("")):
            answer.remove("")
    return answer