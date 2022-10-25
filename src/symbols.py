#Text file symbols
START = "S"
END = "E"
WALKABLE = "."
WALL = "#"
PATH = "@"
ALL_LIST = [START, END, WALKABLE, WALL, PATH]

#SVG Colors
# https://www.color-hex.com/color-palette/36646
COLORS = {
    START: "#770ad2",
    END : "#0b76d7",
    WALKABLE: "#7c818c",
    WALL: "#383c4a",
    PATH: "#5294e2",
}
VISITED_CELL_COL = "#444b5c"
SVG_BORDER_COL = "#404552"
#Other
SVG_RECT_SIZE = 20
SVG_STROKE_WIDTH = 2