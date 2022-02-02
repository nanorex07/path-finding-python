from maze import Maze
from maze_generator import Generator
from solver import Solver

def main():
    # m = Maze(10,15)
    # gen = Generator(m)
    # gen._dfs_backtracker()
    # m.write_to_file("maze_gen.txt")
    m = Maze.load_from_file("maze_gen.txt")
    solver = Solver(m)
    solver._dfs()
    m.write_to_svg("output.svg")

if __name__ == "__main__":
    main()