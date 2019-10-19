import numpy

n = int(input())

rooks = []
targets = []

assigned_targets = {}

for i in range(n):
    x, y = list(map(int, input().split(" ")))
    rooks.append((x, y))

for i in range(n):
    x, y = list(map(int, input().split(" ")))
    targets.append((x, y))

owned_x = {}
owned_y = {}

# Try all targets closer without stepping
for rook in rooks:
    closest = targets[0]
    distance = abs(numpy.subtract(rook, closest)[0]) + abs(numpy.subtract(rook, closest)[1])
    for target in targets:
        if target not in assigned_targets:
            new_offset = numpy.subtract(rook, target)
            new_distance = abs(new_offset[0]) + abs(new_offset[1])
            if abs(new_offset[0]) + abs(new_offset[1]) <= distance:
                distance = new_distance
                closest = target

    assigned_targets[closest] = rook
    owned_x[rook[0]] = rook
    owned_y[rook[1]] = rook


moves = []
completed = 0
lifted = None

try_lift = False

def drop():
    global lifted, try_lift
    try_lift = False
    if lifted[0] in owned_x or lifted[1] in owned_y:
        print("Overlap when dropping")
    else:
        owned_x[lifted[0]] = lifted
        owned_y[lifted[1]] = lifted
    moves.append(f"{lifted[0]} {lifted[1]} P")
    lifted = None

def lift(rook):
    global lifted, try_lift
    try_lift = False
    lifted = owned_x[rook[0]]
    del owned_x[rook[0]]
    del owned_y[rook[1]]
    moves.append(f"{rook[0]} {rook[1]} T")

def move_rook(rook, direction):
    global try_lift, lifted
    if direction == "l":
        if rook[0] - 1 not in owned_x:
            del(owned_x[rook[0]])
            rook = (rook[0] - 1, rook[1])
            moves.append(f"{rook[0]} {rook[1]} L")
            owned_x[rook[0]] = rook
        elif try_lift:
            if lifted == None:
                lift(owned_x[rook[0] - 1])
                rook = move_rook(rook, "l")
                while True:
                    rook = move_rook(rook, "l")
                    if rook[0] in owned_x and owned_x[rook[0]] == rook:
                        break       
            else:
                drop()
                rook = move_rook(rook, "l")
            try_lift = False
    elif direction == "r":
        if rook[0] + 1 not in owned_x:
            del(owned_x[rook[0]])
            rook = (rook[0] + 1, rook[1])
            moves.append(f"{rook[0]} {rook[1]} R")
            owned_x[rook[0]] = rook
        elif try_lift:
            if lifted == None:
                lift(owned_x[rook[0] + 1])
                rook = move_rook(rook, "r")
                while True:
                    rook = move_rook(rook, "r")
                    if rook[0] in owned_x and owned_x[rook[0]] == rook:
                        break       
            else:
                drop()
                rook = move_rook(rook, "r")
    elif direction == "u":
        if rook[1] + 1 not in owned_y:
            del(owned_y[rook[1]])
            rook = (rook[0], rook[1] + 1)
            moves.append(f"{rook[0]} {rook[1]} U")
            owned_y[rook[1]] = rook
        elif try_lift:
            if lifted == None:
                lift(owned_y[rook[1] + 1])
                rook = move_rook(rook, "u")
                while True:
                    rook = move_rook(rook, "u")
                    if rook[1] in owned_y and owned_y[rook[1]] == rook:
                        break       
            else:
                drop()  
                rook = move_rook(rook, "u")
    elif direction == "d":
        if rook[1] - 1 not in owned_y:
            del(owned_y[rook[1]])
            rook = (rook[0], rook[1] - 1)
            moves.append(f"{rook[0]} {rook[1]} D")
            owned_y[rook[1]] = rook
        elif try_lift:
            if lifted == None:
                lift(owned_y[rook[1] - 1])
                rook = move_rook(rook, "d")
                while True:
                    rook = move_rook(rook, "d")
                    if rook[1] in owned_y and owned_y[rook[1]] == rook:
                        break       
            else:
                drop()            
                rook = move_rook(rook, "d")
    return rook
    


while completed < len(targets):
    no_move = True
    for target, rook in assigned_targets.items():
        if rook != lifted:
            x_move = target[0] - rook[0]
            y_move = target[1] - rook[1]

            if x_move != 0:
                if x_move < 0:
                    new_rook = move_rook(rook, "l")
                elif x_move > 0:
                    new_rook = move_rook(rook, "r")
            elif y_move != 0:
                if y_move < 0:
                    new_rook = move_rook(rook, "u")
                elif y_move > 0:
                    new_rook = move_rook(rook, "d")

        if new_rook == rook:
            print(f"Could not move {rook}")
        else:
            no_move = False
            if target == rook:
                completed += 1
            assigned_targets[target] = rook

    if no_move:
        try_lift = True

            
         

print(len(moves))
print("\n".join(moves))