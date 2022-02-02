from symbols import *

class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.maze.process_nodes()

    def _dfs(self):
        stack = []
        r,c = 1,1
        self.maze.maze[r][c].visited = True
        stack.append(self.maze.maze[r][c])
        while len(stack) > 0:
            ne = stack.pop()
            ne.visited = True
            if ne.symbol == END:
                break
            for i in ne.neighbors:
                if not i.visited:
                    i.parent = ne
                    stack.append(i)
        self.trace_path()

    def trace_path(self):
        r = self.maze.rows-1
        c = self.maze.cols-1
        node = self.maze.maze[r][c].parent
        while node.parent:
            node.symbol = PATH
            node = node.parent

