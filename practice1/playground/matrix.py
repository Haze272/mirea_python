class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def heuristic(x1, y1, x2, y2):
   return abs(x1 - x2) + abs(y1 - y2)

arr = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

cost_arr = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
for i in range(3):
    for j in range(4):
            cost_arr[i][j] = heuristic(0, 0, i, j)
print(cost_arr)
for k in range(len(cost_arr)):
    print(cost_arr[k])

is_found = False
way = []
curr = Coordinate(0, 3)

if curr.x - 1 < len(arr) and abs(curr.x - curr.x - 1) == 1:
    print("nice")
else:
    print("shit")

passy = dict()
for j in range(11):
    passy[j] = [0]*28
print(passy)





