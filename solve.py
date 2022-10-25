import argparse
from src.solver import Solver
from src.maze import Maze

algorithm_help = '''
(default 1) Algorithm to use: 1. A Star, 2. DFS, 3. BFS
'''

parser = argparse.ArgumentParser(prog="Maze Solver", usage="Find a path in a maze")
parser.add_argument('-o', '--output', type=str, default="output.txt", help="Name of the output file")
parser.add_argument('-m', '--mazefile', type=str, required=True, help="Name of the maze file")
parser.add_argument('-svg', action='store_true', help="Dumps to svg")
parser.add_argument('-algo', '--algorithm', type=int, default=1, help=algorithm_help)
parser.add_argument('-e','--extra', action='store_true', help="Show visited cells in SVG")
arg = parser.parse_args()

def main():
    m = Maze.load_from_file(arg.mazefile)
    solver = Solver(m)
    if arg.algorithm == 1:
        print("Algorithm Used: A Star")
        solver._a_star()
    elif arg.algorithm == 2:
        print("Algorithm Used: Depth First Search")
        solver._dfs()
    else:
        print("Algorithm Used: Breath First Search")
        solver._bfs()

    m.write_to_file(arg.output)

    if arg.svg:
        m.write_to_svg(arg.output[:-3]+"svg", arg.extra, [solver.er,solver.ec] if arg.algorithm==1 else [-1,-1])
    print(f"[ + ] Dumped, Path Length {solver.path}")

if __name__ == "__main__":
    main()