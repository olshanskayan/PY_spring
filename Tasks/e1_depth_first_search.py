from typing import Hashable, List
import networkx as nx
from collections import deque


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visited = {node: False for node in g.nodes}
    path = []

    # # d.append() #добавить в конец
    # # d.popleft() #забрать сначала
    #
    # d.append(start_node)
    # visited[start_node] = True
    # while d:
    #     #        current_node = d.popleft()
    #     current_node = d.pop()
    #     path.append(current_node)
    #
    #     for neighbor in g.neighbors(current_node):
    #         if not visited[neighbor]:
    #             d.append(neighbor)  # поджигаем узел графа
    #             visited[neighbor] = True  # если узел подожжен, то мы его посещали

    def recursion_dfs(current_node: Hashable):

        visited[current_node] = True
        path.append(current_node)

        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                # visited[neighbor] = True  # если узел подожжен, то мы его посещали
                recursion_dfs(neighbor)
        return path

    recursion_dfs(start_node)
    return path
    # print(g, start_node)
    # return list(g.nodes)

