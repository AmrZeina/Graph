import heapq

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

class undirected_weighted_graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}
        '''
        Initializes a dictionary from 0 to vertices-1,
        where each key maps to a list of (neighbor, weight) tuples.
        '''

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # add edge from u to v
        self.graph[v].append((u, weight))  # because it's undirected

    def prim(self, start=0):             # starting from vertex zero by default
        D = [float('inf')] * self.V      # distance from MST initiallized to infinity
        parent = [None] * self.V         # to store MST edges
        in_mst = [False] * self.V        # to check if the node is exist in the MST or not

        D[start] = 0
        min_heap = [(0, start)]          # Priority queue
        total_cost = 0
        mst_edges = []

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if in_mst[u]:
                continue

            in_mst[u] = True
            total_cost += current_dist

            if parent[u] is not None:
                mst_edges.append((parent[u], u, current_dist))

            for neighbor, weight in self.graph[u]:
                if not in_mst[neighbor] and weight < D[neighbor]:
                    D[neighbor] = weight
                    parent[neighbor] = u
                    heapq.heappush(min_heap, (D[neighbor], neighbor))

        print("Prim's MST: ")
        for u, v, w in mst_edges:
            print(f"{u} - {v} : {w}")
        print("Total weight: ", total_cost)


g = directed_acyclic_graph(8)
g.add_edge(7, 5)
g.add_edge(7, 6)
g.add_edge(6, 3)
g.add_edge(5, 4)
g.add_edge(6, 4)
g.add_edge(3, 1)
g.add_edge(2, 1)
g.add_edge(1, 0)

g.topological_sort()

g = undirected_weighted_graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim(start=0)
