import argparse
from src.maze_generator import Generator
from src.maze import Maze

algorithm_help = '''
(default 2) Algorithm to use: 1. Randomized Prim, 2. DFS Backtracter
'''

parser = argparse.ArgumentParser(prog="Maze Generator", usage="Generates a random maze")
parser.add_argument('-o', '--output', type=str, default="maze_gen.txt", help="Name of the output file")
parser.add_argument('-w', '--width', type=int, default=70, help="Width of maze")
parser.add_argument('-hi', '--height', type=int, default=50, help="Height of maze")
parser.add_argument('-svg', action='store_true', help="Dumps to svg")
parser.add_argument('-algo', '--algorithm', type=int, default=2, help=algorithm_help)

arg = parser.parse_args()

def main():
    m = Maze(arg.height, arg.width)
    gen = Generator(m)
    if arg.algorithm == 1:
        gen._randomized_prim()
    else:
        gen._dfs_backtracker()
    m.write_to_file(arg.output)
    if arg.svg:
        m.write_to_svg(arg.output[:-3]+"svg")
    print("[ + ] Maze Generated, use the solver on it")

if __name__ == "__main__":
    main()