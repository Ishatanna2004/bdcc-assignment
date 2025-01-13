import heapq
import time

def dijkstra(graph, start):
    pq = []
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'A': 2, 'E': 3, 'F': 6},
    'C': {'A': 4, 'D': 1, 'F': 5},
    'D': {'A': 7, 'C': 1, 'G': 2},
    'E': {'B': 3, 'F': 1, 'H': 8},
    'F': {'B': 6, 'C': 5, 'E': 1, 'G': 3, 'H': 2},
    'G': {'D': 2, 'F': 3, 'H': 4},
    'H': {'E': 8, 'F': 2, 'G': 4}
}

iterations = 5
total_time = 0

for _ in range(3):  # Run a few iterations without recording time to warm up JIT compiler for pypy
    result = dijkstra(graph, 'A')

for _ in range(iterations):
    start_time = time.time()
    result = dijkstra(graph, 'A')
    #print(result)
    end_time = time.time()
    total_time += (end_time - start_time)

average_time = total_time / iterations

print(average_time)