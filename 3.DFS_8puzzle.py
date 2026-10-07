# 8-Puzzle using DFS

BLANK_MOVES = {
    -3: "Up",
    3: "Down",
    -1: "Left",
    1: "Right",
}

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


def dfs(start, goal):
    stack = [start]
    parent = {start: None}
    explored = 0

    while stack:
        state = stack.pop()
        explored += 1
        previous = parent[state]
        if previous is None:
            move = "initial state"
        else:
            move = f"blank moved {BLANK_MOVES[state.index(0) - previous.index(0)]}"
        print(f"\nExplored state #{explored} ({move}):", flush=True)
        display(state)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1], explored

        for neighbor in get_neighbors(state):
            if neighbor not in parent:
                parent[neighbor] = state
                stack.append(neighbor)

    return None, explored


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

        solution, explored = dfs(start, goal)

        if solution:
            print(
                f"Solution found using DFS in {len(solution) - 1} moves "
                f"(explored {explored} states):"
            )
            for step, state in enumerate(solution):
                if step == 0:
                    print("Step 0 (initial state):")
                else:
                    previous_blank = solution[step - 1].index(0)
                    current_blank = state.index(0)
                    direction = BLANK_MOVES[current_blank - previous_blank]
                    print(f"Step {step} (blank moved {direction}):")
                display(state)
        else:
            print(f"No solution found (explored {explored} states).")

print("Hanish S Adhi - 1BM24CS109")