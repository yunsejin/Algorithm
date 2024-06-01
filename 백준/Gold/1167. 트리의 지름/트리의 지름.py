import sys
from collections import deque

input = sys.stdin.read
sys.setrecursionlimit(100000)

def bfs(start, graph):
    n = len(graph)
    distances = [-1] * n
    queue = deque([start])
    distances[start] = 0

    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        
        for neighbor, weight in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + weight
                queue.append(neighbor)
    
    max_distance = max(distances)
    farthest_node = distances.index(max_distance)
    return farthest_node, max_distance

def main():
    data = input().split()
    idx = 0
    V = int(data[idx])
    idx += 1
    
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(V):
        u = int(data[idx])
        idx += 1
        while True:
            v = int(data[idx])
            if v == -1:
                idx += 1
                break
            w = int(data[idx + 1])
            graph[u].append((v, w))
            idx += 2
    
    farthest_node, _ = bfs(1, graph)
    
    _, tree_diameter = bfs(farthest_node, graph)
    
    print(tree_diameter)

if __name__ == "__main__":
    main()
