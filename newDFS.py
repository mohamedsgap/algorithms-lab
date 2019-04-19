

graph= {
            "A": set(["B","C"]),
            "B": set(["A","D","E"]),
            "C": set(["A","E"]),
            "D": set(["B","E","G"]),
            "E": set(["B","D","G"]),
            "G": set(["D","E"])
            }


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


print(dfs(graph, "A"))

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print(dfs(graph, 'G'))
    
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'G')))


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

print(list(dfs_paths(graph, 'A', 'G')))   