# Number of pairs
n = int(input())

game = {} # Maps card value to position
removed_positions = []

for i in range(1, 2*n + 1):
    game[i] = []

def make_guess():
    global removed_positions
    for pos in game.values():
        if len(pos) == 2:
            return (pos[0], pos[1])
    all_known_positions = [item for sublist in game.values() for item in sublist]
    
    # Guess the next two items afer the last known
    if all_known_positions:
        all_known_positions.sort()
        guess = (all_known_positions[-1] + 1, all_known_positions[-1] + 2)
        if guess[0] not in removed_positions and guess[1] not in removed_positions:
            return (all_known_positions[-1] + 1, all_known_positions[-1] + 2)

    if removed_positions:
        removed_positions.sort()
        return (removed_positions[-1] + 1, removed_positions[-1] + 2)
    else:
        return (1, 2)

def match(guess):
    global game, removed_positions
    remove_value = None
    for value, position in game.items():
        if guess[0] in position and guess[1] in position:
            remove_value = value

    removed_positions += [guess[0], guess[1]]
    if remove_value:
        del game[remove_value]

# Until we win
while len(removed_positions) < 2*n:
    guess = make_guess()
    print(f"ME -> {guess[0]} {guess[1]}")
    response = input()
    if response == "MATCH":
        match(guess)
    elif response == "-1":
        exit()
    else:
        card_1, card_2 = list(map(int, response.split()))
        if guess[0] not in game[card_1]:
            game[card_1].append(guess[0])
        if guess[1] not in game[card_2]:
            game[card_2].append(guess[1])

print("-1") 