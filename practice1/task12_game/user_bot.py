import numpy as np

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def heuristic(a, b):
   return abs(a.x - b.x) + abs(a.y - b.y)

def near_gold(check, x, y, level):
    gold_dict = dict()

    if level == 2:
        level_width = 28
        level_height = 10
    elif level == 3:
        level_width = 28
        level_height = 25

    for i in range(level_width):
        for j in range(level_height):
            if check("gold", i, j) == True:
                gold_dict[heuristic(Coordinate(x, y), Coordinate(i, j))] = Coordinate(i, j)
    sorted_dict = {k: gold_dict[k] for k in sorted(gold_dict)}
    keys = list(sorted_dict.keys())

    print("Near gold is in", sorted_dict[keys[0]].x, sorted_dict[keys[0]].y)

    return sorted_dict[keys[0]]

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        #print(self.position == other.position)
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

def get_destination_to(check, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        print("координаты одинаковы", x1, y1, x2, y2)
    wall_dict = np.zeros((28, 25))

    for i in range(28):
        for j in range(25):
            if check("wall", i, j) == True:
                wall_dict[i][j] = 1

    wall_dict = wall_dict.transpose()

    start = (y1, x1)
    end = (y2, x2)

    if not(x1 == x2 and y1 == y2):
        path = astar(wall_dict, start, end)
        print(path)
        print('\n')
        print("NIGGERS", x1, y1)
        if path[1][0] - path[0][0] == 1:
            return "down"
        elif path[1][0] - path[0][0] == -1:
            return "up"
        elif path[1][1] - path[0][1] == 1:
            return "right"
        elif path[1][1] - path[0][1] == -1:
            return "left"
    print("NIGGERS")
    return "up"




def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        while check("wall", x + 2, y) == 0:
            return "right"
        return "down"


    elif check("level") == 2:

        gold = near_gold(check, x, y, 2)

        if check("gold", x, y):
            return "take"
        if x < gold.x:
            return "right"
        if y > gold.y:
            return "up"
        if x > gold.x:
            return "left"
        if y < gold.y:
            return "down"

    elif check("level") == 3:

        if check("gold", x, y):
            return "take"
        print('\n')

        depart = Coordinate(x, y)
        fini = near_gold(check, depart.x, depart.y, 3)

        destination = get_destination_to(check, depart.x, depart.y, fini.x, fini.y)
        print(destination)
        return destination
    return "up"
