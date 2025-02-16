import heapq

# return a dict of shortest distances from starting vertex to that all reachable vertices
# if a vertix is not reachable from start then distance == inf
def dijkstra_all_reachable_nodes(graph: dict, start: str) -> dict:
    priorityQueue = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    while priorityQueue:
        # pop the node with the smallest value from pqueue
        current_distance, current_node = heapq.heappop(priorityQueue)
        # check if the current node's distance is greater than the least saved distance in distance dict
        if current_distance > distances[current_node]:
            continue
        #loop through its neighbor nodes if one of the neighbor's distance + current wight is less than distance in distance list update the value of the node by pushing it to the pqueue 
        for neighbor in graph[current_node]:
            distance = current_distance + graph[current_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priorityQueue, (distance, neighbor))
    return distances

"""
    Implements Dijkstra's algorithm to find the shortest path 
    from `start` node to `target` node in a weighted graph.

    Parameters:
    - graph (dict): Adjacency list representation of the graph.
    - start (str): The starting node.
    - target (str): The target node.

    Returns:
    - int: The shortest distance from start to target, or -1 if no path exists.
"""
def dijkstra_shortest_path_to_target(graph: dict, start: str, target: str) -> int:
    # initialize distance dictionary ==> keep track of the each nodes smallest distance from start
    # initialize priorityQueue ==> allow us to explore nodes with smallest distances
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priorityQueue = [(0, start)]

    while priorityQueue:
        current_distance, current_node = heapq.heappop(priorityQueue)
        if current_node == target:
            return current_distance
        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + graph[current_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priorityQueue, (distance, neighbor))
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

    # distances = dijkstra_all_reachable_nodes(graph, "A")
    # print(distances)
    distance = dijkstra_shortest_path_to_target(graph, "A", "A")
    print(distance)
if __name__ == "__main__":
    main()