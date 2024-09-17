graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}



def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node in visited:
            continue
        
        visited.append(node)
        
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                stack.append(new_path)

solution = dfs(graph, 'S', 'G')
print("Solution is", solution)