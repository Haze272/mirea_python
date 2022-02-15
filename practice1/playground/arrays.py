class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def heuristic(a, b):
   return abs(a.x - b.x) + abs(a.y - b.y)

gold_dict = dict()
gold_dict[2] = Coordinate(3, 4)
gold_dict[19] = Coordinate(7, 9)
if (gold_dict[2]):
    print("DAAAAAAAAAMN")
    gold_dict[2] = {Coordinate}
gold_dict[2] = Coordinate(10, 5)
gold_dict[6] = Coordinate(2, 0)

for i in gold_dict:
    print(i, ":", gold_dict[i].x, gold_dict[i].y)
print("-----------------------------------")

sorted_dict = {k: gold_dict[k] for k in sorted(gold_dict)}

for j in sorted_dict:
    print(j, ":", gold_dict[j].x, gold_dict[j].y)



print("-----------------------------------")
keys = list(sorted_dict.keys())
print(keys[0])