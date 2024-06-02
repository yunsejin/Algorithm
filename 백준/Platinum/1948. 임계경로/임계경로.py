from collections import deque, defaultdict

def find_critical_path(n, edges, start, end):
    indegree = [0] * (n + 1)
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    time = [0] * (n + 1)

    for u, v, w in edges:
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))
        indegree[v] += 1

    queue = deque([start])
    distances = [0] * (n + 1)

    while queue:
        current = queue.popleft()
        for next_node, weight in graph[current]:
            if distances[next_node] < distances[current] + weight:
                distances[next_node] = distances[current] + weight
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    critical_path_length = distances[end]

    queue = deque([end])
    visited = [False] * (n + 1)
    visited[end] = True
    count = 0

    while queue:
        current = queue.popleft()
        for prev_node, weight in reverse_graph[current]:
            if distances[current] - weight == distances[prev_node]:
                count += 1
                if not visited[prev_node]:
                    visited[prev_node] = True
                    queue.append(prev_node)

    return critical_path_length, count

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
edges = []
index = 2
for _ in range(m):
    u, v, w = int(data[index]), int(data[index+1]), int(data[index+2])
    edges.append((u, v, w))
    index += 3
start = int(data[index])
end = int(data[index+1])
critical_path_length, critical_edge_count = find_critical_path(n, edges, start, end)

print(critical_path_length)
print(critical_edge_count)
