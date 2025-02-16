import heapq

"""
    djikstra:   - distance dictionary to keep track of the shortest path from start to that node
                - priorityQueue to get the node with the shortest distance
    A star:     - same but instead of y = cost we have y = cost + estimate
"""
def A_start_shortest_distance_to_target(graph: dict, start: str, target: str) -> int:
    distances = { node: float("inf") for node in graph }
    distances[start] = 0

    priorityQueue = [(0, 0, start)]
    while priorityQueue:
        current_coest_with_estimate, current_cost, current_node = heapq.heappop(priorityQueue)
        if current_node == target:
            return current_cost
        
        if current_cost > distances[current_node]:
            continue

        for node, weight in graph[current_node].items():
            cost, estimate = weight
            distance = current_cost + cost
            if distance + estimate < distances[node]:
                distances[node] = distance
                heapq.heappush(priorityQueue, (distance + estimate, distance,  node))
    return -1


def main():
    graph = {
        'A': {'B': (4, 10), 'C': (1, 5)},
        'B': {'A': (4, 10), 'C': (2, 8), 'D': (2, 7)},
        'C': {'A': (1, 5), 'B': (2, 8), 'E': (3, 6)},
        'D': {'B': (2, 7), 'E': (3, 9), 'F': (5, 12)},
        'E': {'C': (3, 6), 'D': (3, 9), 'F': (1, 4)},
        'F': {'D': (5, 12), 'E': (1, 4)},
        'P': {'N': (3, 2)},
        'N': {'P': (3, 2)}
    }
    distance = A_start_shortest_distance_to_target(graph, "A", "B")
    print(distance)
if __name__ == "__main__":
    main()