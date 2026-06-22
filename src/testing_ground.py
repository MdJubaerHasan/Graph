from bfs import bfs
from src.graph import UndirectedGraph

my_graph = UndirectedGraph()


my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("B", "D")


print("BFS Traversal starting from A:")
bfs(my_graph, 'B')