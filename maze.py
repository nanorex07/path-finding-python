from symbols import *

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
    def __str__(self):
        return f'''
            "{self.symbol}" -> {len(self.neighbors)}
        '''
    def addNeighbor(self, n):
        self.neighbors.append(n)

class Maze:
    '''Maze class to generate and blit maze'''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = []
        self.create()

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

    def process_walls(self):
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if self.maze[r][c].wall:
                    dx = [-1,1,0,0]
                    dy = [0,0,1,-1]
                    for x in range(0, 4):
                        if (r+dx[x] >= 0 and r+dx[x] < self.rows) and (c+dy[x] >= 0 and c+dy[x] < self.cols) and not self.maze[r+dx[x]][c+dy[x]].wall:
                            self.maze[r][c].addNeighbor(self.maze[r+dx[x]][c+dy[x]])

    def __str__(self):
        res = ""
        for i in self.maze:
            for j in i:
                res += j.symbol
            res += "\n"
        return res
    
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

    def write_to_svg(self, filename):
        f = open(filename, 'w')
        w = self.cols * SVG_RECT_SIZE
        h = self.rows * SVG_RECT_SIZE
        f.write(f'<svg width="{w}" height="{h}">')
        y = 0
        for i in range(self.rows):
            x = 0
            for j in range(self.cols):
                f.write(f'<rect x="{x}" y="{y}" width="{SVG_RECT_SIZE}" height="{SVG_RECT_SIZE}" style="fill:{COLORS[self.maze[i][j].symbol]};stroke:{SVG_BORDER_COL};stroke-width:{SVG_STROKE_WIDTH};" />')
                x += SVG_RECT_SIZE
            y += SVG_RECT_SIZE
        f.write(f'</svg>')
        f.close()