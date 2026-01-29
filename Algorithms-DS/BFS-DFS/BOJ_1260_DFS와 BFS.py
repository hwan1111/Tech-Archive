#1260, DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline
def DFS(graph, start_node, visited = []):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted((neighbor for neighbor in graph[node] if neighbor not in visited), reverse = True))

    return visited

def BFS(graph, start_node, visited = []):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted((neighbor for neighbor in graph[node] if neighbor not in visited)))
    
    return visited

N, M, start_node = map(int, input().split())
graph = {i: set() for i in range(1, N+1)}

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
    
dfs = DFS(graph, start_node)
bfs = BFS(graph, start_node)

for answer1 in dfs:
    print(answer1, end = ' ')
print()
for answer2 in bfs:
    print(answer2, end = ' ')