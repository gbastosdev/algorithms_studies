graph = {}
graph['beginning'] = {}
graph["beginning"]['A'] = 6
graph["beginning"]['B'] = 2
graph['A'] = {}
graph['A']['end'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['end'] = 5
graph['end'] = {}

costs = {}
costs['A'] = 6
costs['B'] = 2
costs['end'] = float('inf')

parents = {}
parents['A'] = 'beginning'
parents['B'] = 'beginning'
parents['end'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
# Process each node until there are no more nodes to process.
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
print("Costs: ", costs)
print("Parents: ", parents)
print("Final graph: ", graph)
# This code implements Dijkstra's algorithm to find the shortest path in a graph.
# It initializes the graph, costs, and parents, then iteratively finds the lowest cost node  