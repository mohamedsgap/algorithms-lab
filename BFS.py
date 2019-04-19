from collections import defaultdict

class graph:
    def __init__(self):
        self.graph = defaultdict(list)  # generate empty dictionary each value represent list

    def addEdge(self , u , v):
             self.graph[u].append(v)

    def bfs (self,s):
            visited = [False]*len(self.graph)
            queue = []
            queue.append(s)
            visited[s] = True
            while queue:
                s = queue.pop(0)
                print(s)
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i]= True

g = graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,0)
g.addEdge(5,2)
print("Breadth First Visiting Order ->")
g.bfs(0)