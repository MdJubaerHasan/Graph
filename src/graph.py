from src.node import Node


class UndirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self,from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        src_node = self.nodes[from_node]
        dest_node = self.nodes[to_node]

        src_node.add_neighbor(dest_node)
        dest_node.add_neighbor(src_node)


class DirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, source_node, destination_node):
        self.add_node(source_node)
        self.add_node(destination_node)

        src_node = self.nodes[source_node]
        dest_node = self.nodes[destination_node]

        src_node.add_neighbor(dest_node)

class WeightedGraph:
    def __init__(self):
        self.nodes = {}

        