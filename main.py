class directed_acyclic_graph:
    def __init__(self, vertices):
        self.V= vertices #Intializes a graph that has vertices number equals to variable vertices
        self.graph= {i: [] for i in range(vertices)}
        '''
        Initialize a dictionary that from 0 to vertices-1 where each key (node number) maps to its children.
        Adjacency list method
        '''
    def add_edge(self, u, v):
        self.graph[u].append(v) #v is child of u

    def topological_sort(self):
        in_degree = [0] * self.V    #Set all indegree for all nodes to be initially zero
        for u in self.graph:        #Calculate each indegree
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = []
        topological = []

        for i in range(self.V):   #Loop through all the nodes that their indegree = 0 and push them on queue
            if in_degree[i] == 0:
                queue.append(i)

        while queue:        #Pop from queue and examine children (BFS-based approach)
            current = queue.pop(0)
            topological.append(current)

            for neighbor in self.graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological) == self.V:
            print("Topological Sort:", topological)
        else:
            print("Topological sort not possible")

g = directed_acyclic_graph(8)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 6)
g.add_edge(1, 5)
g.add_edge(2, 4)
g.add_edge(4, 6)
g.add_edge(4, 7)


g.topological_sort()
