from collections import defaultdict
import heapq


class Graph:
    def __init__(self) -> None:
        self.nodes = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.nodes[u].append((v, weight))

    def get_all_nodes(self):
        node = set(self.nodes.keys())
        for u in self.nodes:
            for v, _ in self.nodes[u]:
                node.add(v)
        return node

    def djikstra(self, source, target=None):
        distances = {node: float("inf") for node in self.get_all_nodes()}
        distances[source] = 0
        queue = [(0, source)]
        prev = {node: None for node in self.get_all_nodes()}

        while queue:
            current_distance, u = heapq.heappop(queue)

            if u == target:
                break

            if current_distance > distances[u]:
                continue

            for v, edge in self.nodes[u]:
                new_distance = current_distance + edge
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    prev[v] = u
                    heapq.heappush(queue, (new_distance, v))

        if not target:
            return distances

        path = []
        temp = target
        while temp:
            path.append(temp)
            temp = prev[temp]
        path.reverse()
        return path, distances[target]

    def astar(self, source, target, heuristic):
        g_score = {node: float("inf") for node in self.get_all_nodes()}
        g_score[source] = 0

        f_score = {node: float("inf") for node in self.get_all_nodes()}
        f_score[source] = heuristic(source, target)

        prev = {node: None for node in self.get_all_nodes()}
        open_set = [(f_score[source], source)]

        while open_set:
            _, u = heapq.heappop(open_set)

            if u == target:
                break

            for v, weight in self.nodes[u]:
                tentative_g = g_score[u] + weight

                if tentative_g < g_score[v]:
                    g_score[v] = tentative_g
                    f_score[v] = tentative_g + heuristic(v, target)
                    prev[v] = u
                    heapq.heappush(open_set, (f_score[v], v))

        # reconstruct path
        path = []
        temp = target
        while temp:
            path.append(temp)
            temp = prev[temp]
        path.reverse()

        return path, g_score[target]


g = Graph()
g.add_edge("A", "B", 2)
g.add_edge("A", "C", 5)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 4)
g.add_edge("C", "D", 1)

start = "A"
target = "D"
print(f"Result is {g.djikstra(start)})")
print(f"Result is {g.djikstra(start, target)})")


def build_grid_graph(width, height):
    g = Graph()

    for x in range(width):
        for y in range(height):
            if x + 1 < width:
                g.add_edge((x, y), (x + 1, y), 1)
                g.add_edge((x + 1, y), (x, y), 1)

            if y + 1 < height:
                g.add_edge((x, y), (x, y + 1), 1)
                g.add_edge((x, y + 1), (x, y), 1)

    return g


def manhattan(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


g = build_grid_graph(30, 30)

start = (0, 0)
target = (29, 29)

path_d, dist_d = g.djikstra(start, target)
path_a, dist_a = g.astar(start, target, manhattan)

print("Dijkstra distance:", dist_d)
print("A* distance:", dist_a)
print("Path length (Dijkstra):", len(path_d))
print("Path length (A*):", len(path_a))
