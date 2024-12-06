def solution(my_string):
    answer = []

    for i in range(len(my_string)-1):
        answer.append(my_string[i+1:])
    answer.append(my_string)
    answer = sorted(answer)
    return answer