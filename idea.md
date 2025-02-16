In an A* algorithm we have 2 main factors: the cost and estimate, the cost can be how long would it take us to reach the current node from that starting point, this could be time, money cost, battery consumption etc, whereas the estimate could be how close are we from our goal like euclidean distance (the closer we are the smaller the estimate) and the current node cost is the sum of the cost and the estimate

Breakdown of the Two Main Factors in A*:

Cost function  → Actual cost from the start to the current node

This represents the real cost incurred to reach the node.

Can be measured in time, money, battery consumption, energy, steps, etc.

Example: In a road trip, this could be miles traveled or fuel consumed.

Estimate (heuristic)  → Estimated cost from the current node to the goal

This is a guess of how close the node is to the goal.

It helps guide the search to prioritize promising paths.

Common Heuristics:

Euclidean distance → Best for open 2D/3D space.

Manhattan distance → Best for grids (no diagonal movement).

Chebyshev distance → Best for grids with diagonal movement.

Graph-based estimates (e.g., estimated travel time based on speed limits).

Total Cost  = 

This determines which node to expand next.

The lower , the better the priority in the open list.

Example: Pathfinding with A*

Imagine you want to go from A to B in a city:

 → Distance already traveled (in km)

 → Straight-line distance left to B (in km)

 → Total estimated distance

Key Takeaways

✅ Cost  = actual accumulated effort✅ Estimate  = guess for remaining effort✅ Total cost  = sum of both