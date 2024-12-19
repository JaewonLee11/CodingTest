def solution(arr, idx):
    answer = 0
    for i in range(idx, len(arr)):
        if arr[i] == 0:
            answer = -1
            continue
        else :
            answer = i
            break
    return answer