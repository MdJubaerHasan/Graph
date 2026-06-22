from src.node import Node


class UndirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self,from_node, to_node, bidirectional=True):
        self.add_node(from_node)
        self.add_node(to_node)

        src_node = self.nodes[from_node]
        dest_node = self.nodes[to_node]

        src_node.add_neighbor(dest_node)
        if bidirectional:
            dest_node.add_neighbor(src_node)

