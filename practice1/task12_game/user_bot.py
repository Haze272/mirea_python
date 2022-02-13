import operator

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
                gold_dict[Coordinate(i, j)] = heuristic(Coordinate(x, y), Coordinate(i, j))

    for m in sorted_tuple:
        print(m.x, m.y, ":", sorted_tuple[m])


def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        while check("wall", x + 2, y) == 0:
            return "right"
        return "down"
    elif check("level") == 2:

        if x == 0 and y == 10:
            near_gold(check, x, y)
        return "up"

    return "pass"
