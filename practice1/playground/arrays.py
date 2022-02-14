class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def heuristic(a, b):
   return abs(a.x - b.x) + abs(a.y - b.y)

gold_dict = dict()
gold_dict[5] = Coordinate(3, 4)
gold_dict[19] = Coordinate(7, 9)
gold_dict[heuristic(Coordinate(3, 4), Coordinate(7, 9))] = Coordinate(10, 5)
gold_dict[6] = Coordinate(2, 0)

for i in gold_dict:
    print(i)
print("-----------------------------------")

sorted_dict = {k: gold_dict[k] for k in sorted(gold_dict)}

for j in sorted_dict:
    print(j)



print("-----------------------------------")
keys = list(sorted_dict.keys())
print(keys[0])