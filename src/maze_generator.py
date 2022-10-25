from .symbols import *
import random

class Generator:
    '''Generates a random maze'''
    def __init__(self, maze):
        self.maze = maze
        self.walls_list = []
        self.neighbors = []

    '''Appends walls of a node to walls list'''
    def add_walls(self,r,c):
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        for x in range(0, 4):
            if (r+dx[x] >= 0 and r+dx[x] < self.maze.rows) and (c+dy[x] >= 0 and c+dy[x] < self.maze.cols):
                self.walls_list.append(self.maze.maze[r+dx[x]][c+dy[x]])

    '''Get the list of neighbors'''
    def get_neighbors(self,r,c):
        self.neighbors = []
        dx = [-2,2,0,0]
        dy = [0,0,2,-2]
        for x in range(0, 4):
            if (r+dx[x] >= 0 and r+dx[x] < self.maze.rows) and (c+dy[x] >= 0 and c+dy[x] < self.maze.cols):
                if not self.maze.maze[r+dx[x]][c+dy[x]].visited:
                    self.neighbors.append(self.maze.maze[r+dx[x]][c+dy[x]])

    def _randomized_prim(self):
        self.maze.process_walls()
        start = self.maze.maze[1][1]
        start.visited = True
        self.add_walls(1,1)
        while len(self.walls_list) > 0:
            wall = random.choice(self.walls_list)
            d = False
            for i in wall.neighbors:
                if i.visited == False:
                    wall.symbol = WALKABLE
                    i.visited = True
                    self.add_walls(i.r, i.c)
                    d = True
            if not d:
                self.walls_list.remove(wall)
        self.maze.maze[1][1].symbol = START
        self.maze.maze[self.maze.rows-1][self.maze.cols-1].symbol = END
    
    def _dfs_backtracker(self):
        stack = [self.maze.maze[1][1]]
        self.maze.maze[1][1].visited=True
        while len(stack) > 0:
            curr = stack.pop()
            self.get_neighbors(curr.r, curr.c)
            if(len(self.neighbors) > 0):
                stack.append(curr)
                ne = random.choice(self.neighbors)
                ne.visited = True
                if curr.r-ne.r == 2:
                    self.maze.maze[curr.r-1][curr.c].symbol = WALKABLE
                elif curr.r-ne.r == -2:
                    self.maze.maze[curr.r+1][curr.c].symbol = WALKABLE
                elif curr.c - ne.c == 2:
                    self.maze.maze[curr.r][curr.c-1].symbol = WALKABLE
                else:
                    self.maze.maze[curr.r][curr.c+1].symbol = WALKABLE
                stack.append(ne)
        self.maze.maze[1][1].symbol = START
        self.maze.maze[self.maze.rows-1][self.maze.cols-1].symbol = END
                