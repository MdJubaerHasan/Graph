from collections import deque

from src.graph import UndirectedGraph


def bfs(graph_object : UndirectedGraph, start_node :str):
    if start_node not in graph_object.nodes:
        print(f"Starting node {start_node} not found in graph")
        return

    src_node = graph_object.nodes[start_node]
    queue = deque([src_node])
    visited = {src_node}


    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")

        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)