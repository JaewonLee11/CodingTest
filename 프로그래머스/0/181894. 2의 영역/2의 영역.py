def solution(arr):
    indexList = []
    for i,v in enumerate(arr):
        if v == 2:
            indexList.append(i)
    
    if len(indexList) == 1:
        answer = [arr[indexList[0]]]
    elif len(indexList) > 1:
        answer = arr[indexList[0]:indexList[-1]+1]
    else :
        answer = [-1]

    return answer