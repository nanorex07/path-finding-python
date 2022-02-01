
class Node:
    '''Node class to store info about a node'''
    def __init__(self, symbol='.'):
        self.neighbors = []
        self.symbol = symbol
        self.parent = None

    def __str__(self):
        return f'''
            "{self.symbol}" -> {len(self.neighbors)}
        '''


class Maze:
    '''Maze class to generate and blit maze'''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[Node() for _ in range(0, cols)] for _ in range(0, rows)]
        self.symbols = ['S', 'E', '.', '*', '#']

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

    def load_from_file(self, filename):
        try:
            f = open(filename, 'r')
        except:
            raise Exception("Provided file does'nt exists.")
            quit()
        
        lines = f.readlines()
        f.close()
        self.maze = []
        self.rows = len(lines)
        self.cols = len(lines[0]) - 1
        for i in range(0, self.rows):
            row = []
            for j in range(0, self.cols):
                if(lines[i][j] not in self.symbols):
                    raise Exception("Invalid symbol found in file, exiting.")
                    quit()
                row.append(Node(lines[i][j]))
            self.maze.append(row)
