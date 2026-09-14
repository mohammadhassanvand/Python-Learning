"""
Graph - Adjacency Matrix
------------------------
Represents an undirected graph as a V x V grid, where adj[i][j] = 1
means there is an edge between node i and node j.

Space complexity : O(V^2)
Edge lookup       : O(1)
Find neighbors    : O(V)
"""

from __future__ import annotations


class Graph:
    def __init__(self, n: int) -> None:
        self.n = n
        self.adj = [[0] * n for _ in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u][v] = 1
        self.adj[v][u] = 1  # undirected

    def has_edge(self, u: int, v: int) -> bool:
        return self.adj[u][v] == 1

    def neighbors(self, u: int) -> list[int]:
        return [v for v in range(self.n) if self.adj[u][v]]

    def __str__(self) -> str:
        header = "   " + " ".join(str(i) for i in range(self.n))
        rows = [
            f"{i}: " + " ".join(str(x) for x in row)
            for i, row in enumerate(self.adj)
        ]
        return "\n".join([header, *rows])


if __name__ == "__main__":
    g = Graph(6)
    edges = [(0, 5), (1, 3), (1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
    for u, v in edges:
        g.add_edge(u, v)

    print(g)
    print("\nneighbors of 3:", g.neighbors(3))
    print("has_edge(1, 4):", g.has_edge(1, 4))
    print("has_edge(1, 5):", g.has_edge(1, 5))
