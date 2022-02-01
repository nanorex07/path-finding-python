from maze import Maze

def main():
    m = Maze(10, 10)
    m.load_from_file("maze_gen.txt")
    print(m)

if __name__ == "__main__":
    main()