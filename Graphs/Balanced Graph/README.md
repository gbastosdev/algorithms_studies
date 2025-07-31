# Dijkstra Algorithm:

- Pre requisites and first steps:
    - Dijkstra is a shortest-path algorithm that always expands the node with the lowest total cost so far (using priority queue or similar structure). It is a *greedy algorithm*.
    - Dijkstra does not handle negative weights, so when you're facing a graph with negative values, you cannot use Dijkstra to find the shortest path to the end of that graph.

- The example:
    ```mermaid
    graph LR
        Beginning -- 6 --> A
        Beginning -- 2 --> B
        B -- 3 --> A
        B -- 5 --> End
        A -- 1 --> End
    ```

- Explanation:
    - For implementing Dijkstra properly, we'll need 3 specific graphs. Here, i'll call them as "graph", "costs" and "parents". Also, you'll need a "processed" array. Covering that later.
    - As we know the premises of Dijkstra, we'll need to find the shortest-path to our end. On this case, we're finding the lowest cost to reach the end. For that, we'll have this *find_lowest_cost_node* function that will handle the lowest cost seen so far, for each node of our *costs* graph.
    