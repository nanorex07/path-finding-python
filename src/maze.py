from .symbols import *
import math

class Node:
    '''Node class to store info about a node'''
    def __init__(self, r, c, symbol=WALKABLE, wall=False):
        self.neighbors = []
        self.symbol = symbol
        self.parent = None
        self.visited = False
        self.wall = wall
        self.r = r
        self.c = c
        self.g = None
    def __lt__(self, other):
        return False
    def addNeighbor(self, n):
        self.neighbors.append(n)

class Maze:
    '''Maze class to generate and blit maze'''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = []
        self.create()

    ''' Create the random maze '''    
    def create(self):
        for r in range(0, self.rows):
            temp = []
            if r%2==0:
                for c in range(0, self.cols):
                    temp.append(Node(r,c,WALL, True))
                self.maze.append(temp)
            else:
                for c in range(0, self.cols):
                    if c%2==0:
                        temp.append(Node(r,c,WALL, True))
                    else:
                        temp.append(Node(r,c))
                self.maze.append(temp)

    '''Only called in Generator'''
    def process_walls(self):
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if self.maze[r][c].wall:
                    dx = [-1,1,0,0]
                    dy = [0,0,1,-1]
                    for x in range(0, 4):
                        if (r+dx[x] >= 0 and r+dx[x] < self.rows) and (c+dy[x] >= 0 and c+dy[x] < self.cols) and not self.maze[r+dx[x]][c+dy[x]].wall:
                            self.maze[r][c].addNeighbor(self.maze[r+dx[x]][c+dy[x]])

    ''' Only called in Solver '''
    def process_nodes(self):
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if not self.maze[r][c].wall:
                    dx = [-1,1,0,0]
                    dy = [0,0,1,-1]
                    for x in range(0, 4):
                        if (r+dx[x] >= 0 and r+dx[x] < self.rows) and (c+dy[x] >= 0 and c+dy[x] < self.cols) and not self.maze[r+dx[x]][c+dy[x]].wall:
                            self.maze[r][c].addNeighbor(self.maze[r+dx[x]][c+dy[x]])

    '''utility to print the maze'''
    def __str__(self):
        res = ""
        for i in self.maze:
            for j in i:
                res += j.symbol
            res += "\n"
        return res

    ''' Write to text file '''    
    def write_to_file(self, filename):
        f = open(filename, 'w')
        for i in range(0, self.rows):
            temp = ""
            for j in self.maze[i]:
                temp += j.symbol
            if i == self.rows-1:
                f.write(temp)
            else:
                f.write(temp+'\n')
        f.close()

    ''' Reads a maze file and generate maze over it '''
    @classmethod
    def load_from_file(self, filename):
        try:
            f = open(filename, 'r')
        except:
            raise Exception("Provided file does'nt exists.")
            quit()
        
        lines = f.readlines()
        f.close()
        rows = len(lines)
        cols = len(lines[0]) - 1
        m = Maze(rows, cols)
        for i in range(0, rows):
            for j in range(0, cols):
                if(lines[i][j] not in ALL_LIST):
                    raise Exception("Invalid symbol found in file, exiting.")
                    quit()
                m.maze[i][j] = Node(i,j,lines[i][j], True if lines[i][j] == WALL else False)
        return m

    ''' Dump maze to svg '''
    def write_to_svg(self, filename, show_visit=False, endCor=[-1,-1]):
        f = open("./svg/"+filename, 'w')
        w = self.cols * SVG_RECT_SIZE
        h = self.rows * SVG_RECT_SIZE
        f.write('<?xml version="1.0" encoding="utf-8"?>')

        f.write(f'<svg version="1.1" width="{w}" height="{h}">')
        
        y = 0
        for i in range(self.rows):
            x = 0
            for j in range(self.cols):

                if self.maze[i][j].symbol == WALKABLE and (self.maze[i][j].g or self.maze[i][j].visited) and show_visit:
                    f.write(f'<rect x="{x}" y="{y}" width="{SVG_RECT_SIZE}" height="{SVG_RECT_SIZE}" style="fill:{VISITED_CELL_COL};stroke:{SVG_BORDER_COL};stroke-width:{SVG_STROKE_WIDTH};" />')
                else:
                    f.write(f'<rect x="{x}" y="{y}" width="{SVG_RECT_SIZE}" height="{SVG_RECT_SIZE}" style="fill:{COLORS[self.maze[i][j].symbol]};stroke:{SVG_BORDER_COL};stroke-width:{SVG_STROKE_WIDTH};" />')

                if self.maze[i][j].g and show_visit:
                    sz = 1 - math.floor(math.log(self.maze[i][j].g, 10))/10
                    f.write(f'<text x="{x+SVG_STROKE_WIDTH}" y="{y + (SVG_RECT_SIZE+SVG_STROKE_WIDTH)/2}" fill="white" style="font: bold {sz}em sans-serif;">{self.maze[i][j].g}</text>')

                x += SVG_RECT_SIZE
            y += SVG_RECT_SIZE
        f.write(f'</svg>')
        f.close()