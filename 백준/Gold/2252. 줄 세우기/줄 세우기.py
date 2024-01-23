import sys
from collections import deque
input = sys.stdin.readline

def topological_sort(graph, indegree):
    que = deque(node for node in range(1, len(indegree)) if indegree[node] == 0)
                        
    while que:
        node = que.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                que.append(next_node)
                  
def main():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    indegree = [0] * (v + 1)
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a] += [b]
        indegree[b] += 1

    topological_sort(graph, indegree)
            
if __name__ == '__main__':
    main()