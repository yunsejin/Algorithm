from collections import deque

def bfs(N, K):
    if N >= K:
        return N - K
    
    max_limit = 100000
    visited = [-1] * (max_limit + 1)
    queue = deque([N])
    visited[N] = 0

    while queue:
        current = queue.popleft()
        
        if current == K:
            return visited[current]

        for next_pos in (current - 1, current + 1, 2 * current):
            if 0 <= next_pos <= max_limit and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

N, K = map(int, input().split())

print(bfs(N, K))
