# Search Algorithms in python
## Maze Path Finding algorithms visualization in python

Uses svg to write images

## Todos
- [x] A maze class
- [x] A maze to text file
- [x] A maze generator
- [x] A text file to svg writer
- [x] DFS
- [x] BFS
- [x] A*
- [x] Wrap up by the interface
- [ ] Add Weight's to nodes
- [ ] Weighted algorithms 
-----------------------------

## Guide to text files
These symbols can be changed from `symbols.py` file
```
# : Blocked Node
. : Walkable Node
S : Starting Node
E : Ending Node
@ : Path Node
```
-----------------------------

## How to use

Generator

```bash
python3 maze_gen.py -h
python3 maze_gen.py
```

Path Finder

```bash
python3 solve.py -h
python3 solve.py maze.txt
```

-----------------------------