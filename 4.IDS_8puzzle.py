# 8-Puzzle using Iterative Deepening Search (IDS)
print("Hanish S Adhi - 1BM24CS109")
def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def is_valid_state(state):
    return len(state) == 9 and set(state) == set(range(9))


def is_solvable(start, goal):
    goal_order = {
        tile: index
        for index, tile in enumerate(tile for tile in goal if tile != 0)
    }
    tiles = [goal_order[tile] for tile in start if tile != 0]
    inversions = sum(
        tiles[i] > tiles[j]
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
    )
    return inversions % 2 == 0


def depth_limited_search(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(
                neighbor,
                goal,
                depth - 1,
                path + [neighbor]
            )

            if result:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        print("Searching at depth:", depth)

        result = depth_limited_search(
            start,
            goal,
            depth,
            [start]
        )

        if result:
            return result

        depth += 1


try:
    start = tuple(map(int, input(
        "Enter initial state (9 tiles separated by spaces; use 0 for blank): "
    ).split()))
    goal = tuple(map(int, input(
        "Enter goal state (9 tiles separated by spaces; use 0 for blank): "
    ).split()))
except ValueError:
    print("Invalid input: enter integers from 0 to 8.")
else:
    if not is_valid_state(start):
        print("Invalid initial state: enter each number from 0 to 8 exactly once.")
    elif not is_valid_state(goal):
        print("Invalid goal state: enter each number from 0 to 8 exactly once.")
    elif not is_solvable(start, goal):
        print("The initial state cannot reach the goal state.")
    else:
        print("\nInitial State:")
        display(start)
        print("Goal State:")
        display(goal)

        solution = ids(start, goal)

        print("Solution found using IDS:")
        for state in solution:
            display(state)