from typing import List


class Node:
    """
    Class representing node in the graph.
    """
    def __init__(self, value: int, neighbours: List['Node'] = None):
        """"
        :param value: value of the node
        :param neighbours: list of neighbours of the node, default - None
        """
        if neighbours is None:
            neighbours = []
        self.value = value
        self.neighbours = neighbours

    def add_neighbours(self, neighbours: List['Node']):
        """
        Add nodes from given list to the list of neighbours.
        :param neighbours: list of nodes
        """
        for neighbour in neighbours:
            if neighbour not in self.neighbours:
                self.neighbours.append(neighbour)

    def average_fun(self) -> float:
        """
        Return the average value of nodes in subtree
        :return: average in float
        """
        visited = self.__dfs_visited([], self)
        return round(sum([node.value for node in visited]) / (len(visited)), 2)

    def median_fun(self) -> float:
        """
        Return the median values of nodes in subtree
        :return: median in float
        """
        values = [node.value for node in self.__dfs_visited([], self)]
        values.sort()
        return values[int(len(values) / 2)] if len(values) % 2 == 1 \
            else (values[int(len(values) / 2) - 1] + values[int(len(values) / 2)]) / 2

    def sum_fun(self) -> int:
        """
        Count the sum value of nodes in subtree
        :return: sum in int
        """
        return sum([node.value for node in self.__dfs_visited([], self)])

    def __dfs_visited(self, _visited: List['Node'], _node: 'Node') -> List['Node']:
        """
        Recursive function returning list of nodes in subtree
        :param _visited: list of visited nodes
        :param _node: next node to visit
        :return: list of nodes
        """
        _visited.append(_node)
        for neighbour in _node.neighbours:
            if neighbour not in _visited:
                self.__dfs_visited(_visited, neighbour)
        return _visited
