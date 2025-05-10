import heapq

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


g = undirected_weighted_graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim(start=0)
