from maze import Maze
from maze_generator import Generator

def main():
    m = Maze(8,12)
    m.process_walls()
    gen = Generator(m)
    gen._randomized_prim()
    m.write_to_file("maze_gen.txt")

if __name__ == "__main__":
    main()