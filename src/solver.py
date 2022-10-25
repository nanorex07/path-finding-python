from .symbols import *
import heapq

class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.sr = -1
        self.sc = -1
        self.er = -1
        self.ec = -1
        self.maze.process_nodes()
        self.path = None
        self.init_poses()

    # Find the start and end coor from maze
    def init_poses(self):
        for i in range(0, self.maze.rows):
            for j in range(0, self.maze.cols):
                if self.maze.maze[i][j].symbol == START:
                    self.sr = i
                    self.sc = j
                if self.maze.maze[i][j].symbol == END:
                    self.ec = j
                    self.er = i

    def _dfs(self):
        stack = []
        self.maze.maze[self.sr][self.sc].visited = True
        stack.append(self.maze.maze[self.sr][self.sc])
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

    # Calculate manhattan dist between 2 nodes
    def _manhattan_dist(self,n1, n2):
        return abs(n1.r-n2.r) + abs(n1.c - n2.c) 

    def _bfs(self):
        self.maze.maze[self.sr][self.sc].visited = True
        queue = [self.maze.maze[self.sr][self.sc]]
        while len(queue) > 0:
            ne = queue.pop(0)
            if ne.symbol == END:
                break
            for i in ne.neighbors:
                if not i.visited:
                    i.parent = ne
                    i.visited = True
                    queue.append(i)
        self.trace_path()

    def _a_star(self):
        self.maze.maze[self.sr][self.sc].g = 0
        opens = []
        closed = []
        heapq.heappush(opens, (0, self.maze.maze[self.sr][self.sc]))
        while len(opens) > 0:
            q = heapq.heappop(opens)
            for i in q[1].neighbors:
                i.g = 1 + q[1].g
                if i.symbol == END:
                    i.parent = q[1]
                    self.trace_path()
                    print(self.maze.maze[self.sr][self.sc].g)
                    return
                fcost = i.g + self._manhattan_dist(i, self.maze.maze[self.er][self.ec])

                skip = False

                for n in opens+closed:
                    if i == n[1] and n[0] < fcost:
                        skip = True 
                        break
                if skip:
                    continue
                i.parent = q[1]
                heapq.heappush(opens,(fcost, i))

            closed.append(q)
        self.trace_path()
                
    # Construct the path
    def trace_path(self):
        node = self.maze.maze[self.er][self.ec].parent
        self.path = 1
        while node.parent:
            self.path += 1
            node.symbol = PATH
            node = node.parent
