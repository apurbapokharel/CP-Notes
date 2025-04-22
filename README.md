# P NP NP Hard NP complete


## Types of algirithms
1. ## P
Problems solvable by a deterministic algorithm in polynomial time.
Example: Sorting (like Merge Sort runs in O(n log n)), Matrix Multiplication, Shortest Path using Dijkstra's.

2. ## NP
Problems not necessarily solvable in polynomial time, but their solutions can be verified in polynomial time.
Equivalently: solvable in polynomial time by a non-deterministic Turing machine.
P ⊆ NP, because if you can solve something fast, you can obviously verify it fast.
Examples: SAT, Subset Sum, Hamiltonian Path.
### Remember P is a subset of NP

3. ## Hard And NP-Hard
There is a group of similar problems that do not have polynomial time solutions and have exponential time solution.
1. Knapsack
2. Traveling SalesMan
3. Sum of Subset
4. Graph Coloring
5. Hamiltonian Cycle
6. Satisfiability 

These problems have 2^n time (more or less). And we call them as Hard Problems.
Now, the idea is to relate these problems. So that if you can solve 1 you can solve all.
Take SAT as the base problem and classify that as NP-Hard. Now, all other Hard problem's solutions can be represented in the same way to SAT.
So, if one can solve SAT they can solve all these Hard problems.

### Formal Answer:
A problem is NP-Hard if every problem in NP can be reduced to it in polynomial time.
Not required to be in NP (i.e., may not even be verifiable in polynomial time).
Examples: Halting Problem (not even decidable), TSP (decision version is NP-Complete, optimization version is NP-Hard).

4. ## NP-Complete
For SAT we have a Non-Deterministic algorithm so we call SAT as NP-Complete, meaning it is complete as there is a Non-D polynomial time algorithm.

### Formal Answer:
Problems that are both in NP and NP-Hard.
These are the "hardest" problems in NP. If you can solve one NP-Complete problem in polynomial time, you can solve all problems in NP in polynomial time → P = NP.
First NP-Complete problem: SAT (Boolean Satisfiability Problem), proven by Cook in Cook–Levin theorem.

# More Detail on the different NP problems
 
Knowing this is very important as I should know if the CP problem I'm solving can be further optimized to be solved in polynomial time.

1. Hamiltonian Path/ Unique Path through a maze:
For constrained path-finding problems where you must visit every valid node exactly once — there’s no known polynomial-time algorithm. This is because the problem is in the class of NP-complete problems.

2. Traveling Salesman Problem (TSP)
NP-hard
Find the shortest route that visits each city once and returns to the start.

Hamiltonian Cycle: “Can I visit every city once and come back home?”
TSP: “What’s the cheapest route to do that?”
You can reduce Hamiltonian Cycle to TSP by assigning weights:
Assign weight 1 to edges that exist, weight ∞ (or a big number) to others.
Ask: “Is there a tour of total cost ≤ n?” (n = number of cities)
So yes, Hamiltonian Cycle is a special case of TSP, but TSP is more general and harder to verify (hence, not in NP unless P = NP).

3. Subset Sum Problem:
NP-complete
Given a set of numbers, is there a subset whose sum is exactly equal to a target?

4. Graph Coloring
NP-complete (in general form, like 3-coloring)
Can you assign colors to nodes such that no two adjacent nodes have the same color, using k colors?
Verifiable in polynomial time
→ NP-complete for fixed k ≥ 3
