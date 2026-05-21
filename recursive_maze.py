import random
from typing import NamedTuple
from enum import Enum


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(
        self,
        rows: int = 10,
        columns: int = 10,
        sparseness: float = 0.2,
        start: MazeLocation = MazeLocation(0, 0),
        goal: MazeLocation = MazeLocation(9, 9),
    ) -> None:

        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: list[list[Cell]] = [
            [Cell.EMPTY for c in range(columns)] for r in range(rows)
        ]
        self._randomly_fill(rows, columns, sparseness)

        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(
        self, rows: int, columns: int, sparseness: float
    ) -> None:
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0.0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = ''
        for row in self._grid:
            output += ''.join([c.value for c in row]) + '\n'
        return output

    def mark(self, path: list[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: list[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def walk(
        self,
        curr: MazeLocation,
        seen: list[MazeLocation],
        path: list[MazeLocation],
    ) -> bool:
        # base cases
        # 1. off the grid
        if (
            curr.row < 0
            or curr.row >= len(self._grid[0])
            or curr.column < 0
            or curr.column >= len(self._grid)
        ):
            return False
        # 2. are we on a wall?
        if self._grid[curr.row][curr.column].value == Cell.BLOCKED:
            return False
        # 3. are we at the end?
        if curr == self.goal:
            path.append(self.goal)
            return True
        # 4. seen?
        if curr in seen:
            return False

        # 3 steps in recursive case:
        # pre, recursive and post
        # pre
        seen.append(curr)
        path.append(curr)
        # recurse
        directions = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        )
        for offset in directions:
            row_offset, column_offset = offset
            if self.walk(
                MazeLocation(
                    curr.row + row_offset,
                    curr.column + column_offset,
                ),
                seen,
                path,
            ):
                return True

        # post
        path.pop()
        return False

    def solve(self):
        seen: list[MazeLocation] = []
        path: list[MazeLocation] = []
        self.walk(self.start, seen, path)
        return path


if __name__ == '__main__':
    m = Maze()
    print(m)
    solved_path = m.solve()
    m.mark(solved_path)
    print(m)
