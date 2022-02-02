from maze import Maze
from maze_generator import Generator

def main():
    m = Maze(15,30)
    m.process_walls()
    gen = Generator(m)
    gen._randomized_prim()
    m.write_to_file("maze_gen.txt")
    m.write_to_svg("output.svg")

if __name__ == "__main__":
    main()