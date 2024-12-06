def solution(intStrs, k, s, l):
    answer = []
    for strs in intStrs:
        strToInt = int(strs[s:s+l])
        if strToInt > k :
            answer.append(strToInt)
    return answer