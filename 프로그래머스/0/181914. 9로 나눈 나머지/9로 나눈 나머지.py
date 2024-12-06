def solution(number) :
    answer = 0
    strNumber = 0
    number = str(number)
    for i in number :
        strNumber += int(i)
    answer = strNumber % 9

    return answer