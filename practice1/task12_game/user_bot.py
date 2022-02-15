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
    return sorted_dict[keys[0]]

def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y):
            return "take"
        while check("wall", x + 2, y) == 0:
            return "right"
        return "down"


    elif check("level") == 2:

        gold = near_gold(check, x, y, 2) # [1; 6]
        print(gold.x, gold.y)

        #heuristic(Coordinate(x, y), Coordinate(gold.x, gold.y))
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
        '''
        gold = near_gold(check, x, y, 3) # [1; 6]
        print(gold.x, gold.y)

        #heuristic(Coordinate(x, y), Coordinate(gold.x, gold.y))
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
        # 1 23
        '''


        if x == 1 and y == 23:
            wall_dict = np.zeros((25, 28))

            for i in range(25):
                for j in range(28):
                    if check("wall", j, i) == True:
                        wall_dict[i][j] = 1
            print(wall_dict)
        return "up"





    return "pass"
