import numpy

n = int(input())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, another):
        return self.x == another.x and self.y == another.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"{self.x} {self.y}"

    def add(self, axis, dist):
        if axis == "x":
            return Point(self.x + dist, self.y)
        else:
            return Point(self.x, self.y + distance)



rooks = []
targets = []

assigned_targets = {}

for i in range(n):
    x, y = list(map(int, input().split(" ")))
    rooks.append(Point(x, y))

for i in range(n):
    x, y = list(map(int, input().split(" ")))
    targets.append(Point(x, y))


def target_offset(rook, target):
    return (target.x - rook.x, target.y - rook.y)


def target_distance(rook, target):
    offset = target_offset(rook, target)
    return abs(offset[0]) + abs(offset[1])


owned = {"x": {}, "y": {}}

for rook in rooks:
    closest = targets[0]
    distance = target_distance(rook, closest)
    for target in targets:
        if target not in assigned_targets:
            new_offset = target_offset(rook, target)
            new_distance = target_distance(rook, target)
            if new_distance <= distance:
                distance = new_distance
                closest = target

    assigned_targets[closest] = rook
    owned["x"][rook.x] = rook
    owned["y"][rook.y] = rook

moves = []

lifted = None


def drop():
    global lifted
    if lifted:
        owned["x"][lifted.x] = lifted
        owned["y"][lifted.y] = lifted
        moves.append(f"{lifted} P")
        lifted = None


def lift(rook):
    global lifted
    lifted = rook
    del owned["x"][lifted.x]
    del owned["y"][lifted.y]
    moves.append(f"{lifted} T")


def move_rook(rook, dist, axis):
    global lifted, moves
    if dist != 0:
        if getattr(rook, axis) + dist in owned[axis] and getattr(rook, axis)  + 2 * dist in owned[axis]:
            # Complex Lift
            0
        elif getattr(rook, axis)  + dist in owned[axis]:
            # Simple Lift
            lift(owned[axis][getattr(rook, axis)  + dist])

            # Move under the lifted node's column
            rook = move_rook(rook, dist, axis)
            rook = move_rook(rook, dist, axis)
            drop()
        else:
            # Nothing in front, we can just move
            
            if axis == "x" and dist == -1:
                moves.append(f"{rook} L")
            elif axis == "x" and dist == 1:
                moves.append(f"{rook} R")
            if axis == "y" and dist == -1:
                moves.append(f"{rook} U")
            if axis == "y" and dist == -1:
                moves.append(f"{rook} D")
                
            del owned[axis][getattr(rook, axis)]
            rook = rook.add(axis, dist)
            owned["x"][rook.x] = rook
            owned["y"][rook.y] = rook

    return rook

completed = 0

while completed < len(targets):
    no_move = True
    for target, rook in assigned_targets.items():
        x_move = target.x - rook.x
        y_move = target.y - rook.y

        if x_move != 0:
            if x_move < 0:
                new_rook = move_rook(rook, -1, "x")
            elif x_move > 0:
                new_rook = move_rook(rook, 1, "x")
        if y_move != 0:
            if y_move < 0:
                new_rook = move_rook(rook, -1, "y")
            elif y_move > 0:
                new_rook = move_rook(rook, 1, "y")


        no_move = False
        if target == new_rook:
            completed += 1
        assigned_targets[target] = new_rook

    if no_move:
        break


print(len(moves))
print("\n".join(moves))
