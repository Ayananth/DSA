'''
Graph is a collection of nodes connected by edges

'''





from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def bfs(self, start):
        if start not in self.graph:
            return
        queue = deque()
        visited = set()
        queue.append(start)
        visited.add(start)

        while queue:
            current = queue.popleft()
            print(current, " ")
            if current not in visited:
                queue.append(current)
                visited.add(current)

    def dfs(self, start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for connections in self.graph[start]:
            if connections not in visited:
                self.dfs(connections, visited)
        
        print()


g = Graph()
g.add_edge("a", "b")
g.add_edge("b", "c")
g.dfs("a")

    

    
