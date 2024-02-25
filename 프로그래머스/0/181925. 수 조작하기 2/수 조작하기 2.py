def solution(numLog):
    ans = []
    for i in range(1,len(numLog)):
        if numLog[i] - numLog[i-1] ==1:
            ans.append('w') 
        elif numLog[i] - numLog[i-1] ==-1:
            ans.append('s')
        elif numLog[i] - numLog[i-1] ==10:
            ans.append('d')
        else:
            ans.append('a')
    return ''.join(ans)