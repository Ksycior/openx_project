import pytest
from src.graph import Node


@pytest.fixture(scope="session")
def graph():
    node_1 = Node(5)
    node_2 = Node(3)
    node_3 = Node(7)
    node_4 = Node(2)
    node_5 = Node(5)
    node_6 = Node(1)
    node_7 = Node(0)
    node_8 = Node(2)
    node_9 = Node(8)
    node_10 = Node(5)

    node_1.add_neighbours([node_2, node_3])
    node_2.add_neighbours([node_4, node_5])
    node_3.add_neighbours([node_6, node_7])
    node_7.add_neighbours([node_8, node_9])
    node_9.add_neighbours([node_10])

    return [node_1, node_2, node_3, node_4, node_5, node_6, node_7, node_8, node_9, node_10]


@pytest.mark.parametrize(
    "node, subtree_average", [
        (0, 3.8),
        (1, 3.33),
        (2, 3.83),
        (6, 3.75),
        (8, 6.5),
        (9, 5)
    ]
)
def test_average(graph, node, subtree_average):
    assert subtree_average == graph[node].average_fun()


@pytest.mark.parametrize(
    "node, subtree_median", [
        (0, 4),
        (1, 3),
        (2, 3.5),
        (6, 3.5),
        (8, 6.5),
        (9, 5)

    ]
)
def test_median(graph, node, subtree_median):
    assert subtree_median == graph[node].median_fun()


@pytest.mark.parametrize(
    "node, subtree_sum", [
        (0, 38),
        (1, 10),
        (2, 23),
        (6, 15),
        (8, 13),
        (9, 5)
    ]
)
def test_sum(graph, node, subtree_sum):
    assert subtree_sum == graph[node].sum_fun()