from symbols import *
import random
from maze import Maze

class Generator:
    def __init__(self, maze):
        self.maze = maze
        self.walls_list = []

    def add_walls(self,r,c):
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        for x in range(0, 4):
            if (r+dx[x] >= 0 and r+dx[x] < self.maze.rows) and (c+dy[x] >= 0 and c+dy[x] < self.maze.cols):
                self.walls_list.append(self.maze.maze[r+dx[x]][c+dy[x]])

    def _randomized_prim(self):
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
    