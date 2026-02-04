
### A* vs Dijkstra (Priority Queue Ordering)

In **Dijkstra’s algorithm**, the priority queue is ordered by the actual cost
from the source to a node:

- `g(n)` = distance from source to `n`

The algorithm always expands the node with the smallest `g(n)` (cheapest so far).

---

In **A\***, we still compute the same actual cost:

- `g(n) = g(parent) + edge_weight`

But the priority queue is **not** ordered by `g(n)`.  
Instead, it is ordered by:

- `f(n) = g(n) + h(n)`

where:
- `h(n)` is a heuristic estimate of the remaining cost from `n` to the goal

A\* always expands the node with the **smallest `f(n)`**, i.e., the smallest
estimated total cost from start to goal.

---

### Why this works
- `g(n)` measures the cost to reach the node
- `h(n)` estimates the cost to reach the goal
- `f(n)` is an estimate of the full path cost

This biases the search toward nodes that appear closer to the goal, reducing
unnecessary exploration.

---

### Optimality guarantee
If the heuristic is **admissible**:

- `h(n) ≤ true remaining cost`

then when the goal node is popped from the priority queue, the path found is
optimal.

---

### Relationship to Dijkstra
If the heuristic is zero for all nodes:

- `h(n) = 0`
- `f(n) = g(n)`

A\* reduces exactly to Dijkstra’s algorithm.

**Dijkstra is A\* with a zero heuristic.**
