import heapq

"""
    djikstra:   - distance dictionary to keep track of the shortest path from start to that node
                - priorityQueue to get the node with the shortest distance
    A star:     - same but instead of y = cost we have y = cost + estimate
    A* enhances this by adding a heuristic (h(n)), which is an estimate of the cost to reach the goal from the current node. The algorithm uses the sum f(n)=g(n)+h(n) to prioritize nodes. This way, A* is "informed" and tends to explore nodes that are both cheap so far and promising in terms of reaching the goal. For A* to guarantee an optimal path, the heuristic needs to be admissible (never overestimates the actual cost) and ideally consistent.
    note: f(n) is only used for sorting in pqueue when pushing a node and not for calculations
"""

def A_star_shortest_distance_to_target(graph: dict, heuristic: dict, start: str, target: str) -> int:
    # Initialize distances with "infinity"
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Priority queue holds tuples of (f(n) = g(n) + h(n), g(n), node)
    priorityQueue = [(0 + heuristic.get(start, 0), 0, start)]
    
    while priorityQueue:
        current_f, current_cost, current_node = heapq.heappop(priorityQueue)
        
        # If we've reached the target, return the actual cost
        if current_node == target:
            return current_cost
        
        # Skip if a better path to the current node has already been found
        if current_cost > distances[current_node]:
            continue

        for neighbor, cost in graph[current_node].items():
            distance = current_cost + cost  # g(n) for the neighbor
            # Update if a better path is found (comparing actual cost)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # f(n) = g(n) + h(n)
                heapq.heappush(priorityQueue, (distance + heuristic.get(neighbor, 0), distance, neighbor))
    
    # Return -1 if the target is unreachable
    return -1

def main():
    graph = {
        'A': {'B': 4, 'C': 1},
        'B': {'A': 4, 'C': 2, 'D': 2},
        'C': {'A': 1, 'B': 2, 'E': 3},
        'D': {'B': 2, 'E': 3, 'F': 5},
        'E': {'C': 3, 'D': 3, 'F': 1},
        'F': {'D': 5, 'E': 1},
        'P': {'N': 3},
        'N': {'P': 3}
    }

    # Heuristic values for nodes (should ideally cover all nodes that might be reached)
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 0,
    }
    
    distance = A_star_shortest_distance_to_target(graph, heuristic, "A", "B")
    print(distance)

if __name__ == "__main__":
    main()