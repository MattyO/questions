from copy import deepcopy
class Direction:
    direction_order = ["right", "down", "left", "up" ]
    direction_offset = {"right": (1,0),
                        "down": (0,1,),
                        "left": (-1,0,),
                        "up": (0,-1)}

    def __init__(self, direction=None):
        self.name = direction
        if self.name  == None:
            self.name   = self.direction_order[0]

    def next(self):
        self.name = self.direction_order[(self.direction_order.index(self.name) + 1)  % len(self.direction_order)]

    @property
    def offset(self):
        return self.direction_offset.get(self.name, (0,0))

class Position:
    def __init__(self, x=None, y=None, value=None):
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def apply_offset(self, offset):
        new_x, new_y = [sum(corr) for corr in zip((self.x, self.y), offset)]
        return Position(new_x, new_y)

    def same_location(self, other_position):
        return self.x == other_position.x and self.y == other_position.y


class Grid:
    def __init__(self):
        self.cells = []
    def get_position(self, find_position):
        return next((position for position in self.cells
            if position == find_position), Position())

    def next_position(self, current_position, direction):
        next_position = current_position.apply_offset(direction.offset)
        return self.get_position(next_position)

def enumerate_clockwise(grid):
    grid = deepcopy(grid)
    direction = Direction()
    position = grid.get_position(Position(0,0)) 

    while position.value != None: 
        yield position
        position.value = None
        next_position = grid.next_position(position, direction)
        if next_position.value == None:
            direction.next()
            next_position = grid.next_position(position, direction)
        position = next_position

def create_grid(string_from_file):
    the_grid = Grid()
    for row_num, row in enumerate(string_from_file.split("\n")):
        for col_num, value in enumerate(row.split(" ")):
            the_grid.cells.append(Position(col_num, row_num, str(value)))

    return the_grid
