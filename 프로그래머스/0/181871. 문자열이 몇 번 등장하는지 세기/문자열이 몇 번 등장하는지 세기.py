def solution(myString, pat):
    answer = 0
    a = len(myString)
    b = len(pat)
    for i in range(0,a-b+1):
        if myString[i:i+b] == pat:
            answer+=1
    return answer