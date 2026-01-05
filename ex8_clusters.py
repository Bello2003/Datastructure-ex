def dfs(graph, visited, node):
    visited[node] = True
    for i, connected in enumerate(graph[node]):
        if connected and not visited[i]:
            dfs(graph, visited, i)

def count_clusters(graph):
    visited = [False]*len(graph)
    clusters = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, visited, i)
            clusters += 1
    return clusters

graph = [[0,1,0],
         [1,0,0],
         [0,0,0]]
print("Clusters:", count_clusters(graph))
