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
        # bfs will always find the shortest path. whereas dfs
        # can sometimes do the job quicker; that's the trade off
        # bfs systematically looks one layer of nodes farther away
        # from the start on each iteration.
        # the underlying data structure is a Queue.
        seen: list[bool] = [False] * len(self._vertices)
        path: list[int] = [-1] * len(self._vertices)
        seen[0] = True
        frontier: Queue[int] = Queue()
        frontier.enqueue(start)
        while frontier.length:
            curr: V = frontier.deque()
            if curr == end:
                break
            for edge in self._edges[curr]:
                if not seen[edge.v]:
                    frontier.enqueue(edge.v)
                    path[edge.v] = curr
                    seen[edge.v] = True
        # walk back path
        curr = end
        res = []
        while path[curr] != -1:
            res.append(curr)
            curr = path[curr]
        if res:
            res.reverse()
            return [start] + res
        else:
            return None

    def _walk(
        self, curr: V, end: V, path: list[int], seen: list[bool]
    ) -> bool:
        path.append(curr)
        if curr == end:
            return True
        seen[curr] = True
        for edge in self._edges[curr]:
            if seen[edge.v]:
                return False
            if self._walk(edge.v, end, path, seen):
                return True
        path.pop()
        return False

    def dfs(self, start: V, end: V) -> list[int]:
        # proceed along a path until a barrier is hit.
        # then backtrack to the last decision point.
        # the underlying datastructure is a stack
        # this often takes the form of the call stack
        # via a recursive function
        seen: list[bool] = [False] * len(self._vertices)
        path: list[int] = []
        self._walk(start, end, path, seen)
        return path

    def dijkstra(self, start: V, end: V) -> list[V] | None:
        # Add the starting index to a priority queue (pq)
        # while there are items in the pq, pop to get the closest
        # call it current
        # look at all the neighbors of current.  If the distance arr is
        # empty or the new distance to the vertex is less than the old
        # one then update it.
        # record the curr node in the prev array at the index of the neighbor
        # return the shortest distance to every node from the start and the
        # path to get to there
        path: list[int] = [-1] * len(self._vertices)
        distances: list[int] = [None] * len(self._vertices)
        distances[start] = 0
        pq: MinHeap = MinHeap()
        pq.insert(DijkstraNode(start, 0))
        while pq.length:
            u: int = pq.pop().vertex
            distance_u: int = distances[u]
            for edge in self._edges[u]:
                if (
                    distances[edge.v] is None
                    or distances[edge.v] > distance_u + edge.weight
                ):
                    distances[edge.v] = distance_u + edge.weight
                    path[edge.v] = u
                    pq.insert(DijkstraNode(edge.v, distances[edge.v]))
        res: list[int] = []
        curr: V = end
        while path[curr] != -1:
            res.append(curr)
            curr = path[curr]
        if res:
            res.reverse()
            return [start] + res
        else:
            return None
