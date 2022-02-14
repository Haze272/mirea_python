import operator
from queue import PriorityQueue


class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def heuristic(a, b):
   return abs(a.x - b.x) + abs(a.y - b.y)

def near_gold(check, x, y):
    gold_dict = dict()
    for i in range(27):
        for j in range(10):
            if check("gold", i, j) == True:
                gold_dict[heuristic(Coordinate(x, y), Coordinate(i, j))] = Coordinate(i, j)
    sorted_dict = {k: gold_dict[k] for k in sorted(gold_dict)}
    keys = list(sorted_dict.keys())
    return sorted_dict[keys[0]]


def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        while check("wall", x + 2, y) == 0:
            return "right"
        return "down"
    elif check("level") == 2:

        if x == 0 and y == 10:
            print("Near gold is in", near_gold(check, x, y).x, near_gold(check, x, y).y)
        return "up"

    return "pass"
