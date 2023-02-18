import heapq
from typing import List
def delivery_route_optimization(buildings: List[int], start: int) -> List[int]:
    # n = no_of_nodes
    v =set()
    for i,j,w in buildings:
       v.add(i)
       v.add(j)
    # n = no_of_nodes
    adj = {i: [] for i in range(1, len(v)+1)}

    # s = src, d = dst, w = weight
    # adjencency List
    for s, d, w in edges:
         adj[s].append((d,w))
    
    shortest = {}
    minHeap = [(0, start)]
    while minHeap:
        w1,n1 = heapq.heappop(minHeap)
        print(w1,n1)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2, w2 in adj[n1]:
             if n2 not in shortest:
                 heapq.heappush(minHeap, (w1+w2, n2))
    return shortest.values()


edges = [(1,2,10),(1,3,3),(3,2,4),(2,4,2),(3,5,2),(3,4,8),(4,5,5)]
node = 5
start = 1
result = delivery_route_optimization(edges, start)
print(result)