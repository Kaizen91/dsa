from __future__ import annotations
from data_structures import Queue 
from min_heap import MinHeap
from typing import TypeVar
from dataclasses import dataclass

V = TypeVar('V')

@dataclass
class DijkstraNode:
    vertex: int
    distance: float

    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool:
        return self.distance == other.distance

class Graph:
    def __init__(self, vertices: list[V]):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    def bfs(self, start: V, end: V) -> list[V] | None:
        seen: list[bool] = [False] * len(self._vertices)
        prev: list[V] = [-1] * len(self._vertices)
        frontier: Queue = Queue()
        frontier.enqueue(start)
        seen[0] = True
        while frontier.length:
            curr: V = frontier.deque()
            if curr == end:
                break
            for edge in self._edges[curr]:
                if seen[edge.v]:
                    continue
                seen[edge.v] = True
                prev[edge.v] = curr
                frontier.enqueue(edge.v)
        # build back
        curr = end
        res = []
        while prev[curr] != -1:
            res.append(curr)
            curr = prev[curr]
        if res:
            res.reverse()
            return [start] + res

    def _walk(
            self,
            curr: V,
            start: V,
            end: V,
            seen: list[bool],
            path: list[V],
    ) -> bool:
        path.append(curr)
        if curr == end:
            return True
        if seen[curr]:
            return False
        seen[curr] = True
        for edge in self._edges[curr]:
            if self._walk(edge.v, start, end, seen, path):
                return True
        path.pop()
        return False

    def dfs(self, start: V, end: V) -> list[int]:
        seen: list[bool] = [False] * len(self._vertices)
        path: list[int] = []
        self._walk(start, start, end, seen, path)
        return path

    def dijkstra(self, start: V, end: V) -> list[V] | None:
        first: V = self._vertices[0]
        distances: list[int] = [None] * len(self._vertices)
        distances[first] = 0
        path: list[int] = [-1] * len(self._vertices)
        pq: MinHeap = MinHeap()
        pq.insert(DijkstraNode(first, 0))
        while pq.length:
            u: V = pq.pop().vertex
            distance_u: int = distances[u]
            for edge in self._edges[u]:
                distance_v: int = distances[edge.v]
                new_distance_v: int = distance_u + edge.weight
                if distance_v is None or distance_v > new_distance_v:
                    distances[edge.v] = new_distance_v
                    path[edge.v] = u
                    pq.insert(DijkstraNode(edge.v, distances[edge.v]))
        curr: int = end
        res: list[V] = []
        while path[curr] != -1:
            res.append(curr)
            curr = path[curr]
        if res:
            res.reverse()
            return [start] + res
        else:
            return None
