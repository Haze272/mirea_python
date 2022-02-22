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

    wall_dict = np.zeros((level_width, level_height))

    for i in range(level_width):
        for j in range(level_height):
            if check("wall", i, j) == True:
                wall_dict[i][j] = 1

    wall_dict = wall_dict.transpose()

    for i in range(level_width):
        for j in range(level_height):
            if check("gold", i, j) == True:
                gold_dict[len(astar(wall_dict, (y, x), (j, i)))] = Coordinate(i, j)
    sorted_dict = {k: gold_dict[k] for k in sorted(gold_dict)}
    keys = list(sorted_dict.keys())

    print("Near gold is in", sorted_dict[keys[0]].x, sorted_dict[keys[0]].y)

    return sorted_dict[keys[0]]

from warnings import warn
import heapq


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]


def astar(maze, start, end, allow_diagonal_movement=False):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # ОСТАНОВИСЬ, ПОКА ОСТАНОВКА НЕ СТАЛА ПОСЛЕДНЕЙ, ЕЖЖЕ
    outer_iterations = 0
    #max_iterations = (len(maze[0]) * len(maze) // 2) так вообще-то правильнее, но были провалы из-за этого
    max_iterations = (len(maze[0]) * len(maze) * len(maze))

    # суета с ходом по диагонали
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
            warn("Слишком много итераций")
            return return_path(current_node)

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)
        if current_node == end_node:
            return return_path(current_node)

        children = []

        for new_position in adjacent_squares:

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if len([open_node for open_node in open_list if
                    child.position == open_node.position and child.g > open_node.g]) > 0:
                continue
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None

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
