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
