class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, neighbor_node, weight = None):
        self.neighbors[neighbor_node] = weight


