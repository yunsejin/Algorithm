def solution(arr, queries):
    
    ans = []
    for i in queries:
        a = arr[i[0] : i[1]+1] 
        b = []
        for j in a:
            if j > i[2]:
                b.append(j)
        if len(b) > 1 :
            ans.append(min(b))
        elif len(b) == 1:
            ans.append(b[0])
            
        else : ans.append(-1)
    return ans