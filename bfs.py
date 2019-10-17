def bfs(vertex, adj):
    seen = [vertex] 
    nxt = [vertex]
    while nxt:
        current = nxt.pop(0)
        for i in adj[current]:
            if i not in seen:
                seen.append(i)
                nxt.append(i)
    return seen
graph = {0: [1, 2], 1: [2], 2: []}
print(bfs(0, graph))