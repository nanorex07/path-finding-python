from maze import Maze
from maze_generator import Generator
from solver import Solver

def main():
    # m = Maze(40,60)
    # gen = Generator(m)
    # gen._dfs_backtracker()
    # m.write_to_file("tester.txt")

    m = Maze.load_from_file("tester.txt")
    solver = Solver(m)
    solver._bfs()
    m.write_to_svg("output.svg", True)

if __name__ == "__main__":
    main()