# Explanation
   - Time execution: Remember that time execution will be affected by searching on every single person of the graph for a "mango seller". On worst case scenario, you will find that person on the last edge of last vertice of the graph. Or even not find it. This means that we'll face a O(n) runtime, or simply O(number_of_edges). Also adding verified people to a list takes O(1) to insert it. Constant time. But if you're adding "N" people to your list, this regards to O(n) in total. So, breadth-first search or BFS has time execution of O(number_of_persons/number_of_vertices + number_of_edges), which is frequently writed as O(V+E).
---

## Summary

- **Time Complexity:**  
    - In the worst case, you may need to search every person (vertex) and every connection (edge) in the graph to find a "mango seller" or determine there isn't one.
    - **BFS (Breadth-First Search) Time Complexity:**  
        - Visiting all vertices: O(V)
        - Traversing all edges: O(E)
        - **Total:** O(V + E)
    - Adding each person to a verified list is O(1) per insertion, so adding N people is O(N) in total.

> **In short:**  
> Breadth-first search (BFS) on a graph runs in O(V + E) time, where V is the number of vertices (people) and E is the number of edges (connections).
