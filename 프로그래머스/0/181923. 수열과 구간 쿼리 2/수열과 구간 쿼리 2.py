def solution(arr, queries):
    answer = []
    for s,e,k in queries :
        filtered_list = []
        for i in range(s,e+1) :
            if arr[i] > k :
                filtered_list.append(arr[i])
            else : 
                continue
        if filtered_list :
            answer.append(min(filtered_list))
        else :
            answer.append(-1)
    return answer