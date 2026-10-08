# Hill Climbing for 4-Queens Problem

print("Hanish S Adhi - 1BM24CS109")
def cost(state):
    """Return number of attacking pairs of queens."""
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def generate_neighbors(state):
    """Generate all neighbor states by swapping any two queens."""
    neighbors = []
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(tuple(new_state))

    # Keep deterministic order for tie-breaking
    return neighbors


def hill_climb(initial_state):
    current = tuple(initial_state)
    step = 0

    print("Hill climbing for 4-Queens")
    print("Initial state:", current)
    print()

    while True:
        current_cost = cost(current)
        print(f"Step {step}: current state = {current}, cost = {current_cost}")

        if current_cost == 0:
            print("Goal reached! No queens attack each other.")
            break

        neighbors = generate_neighbors(current)
        neighbor_data = []

        print("Neighbor costs:")
        for neighbor in neighbors:
            c = cost(neighbor)
            neighbor_data.append((c, neighbor))
            print(f"  {neighbor} -> cost = {c}")

        best_cost, best_neighbor = min(neighbor_data, key=lambda x: (x[0], x[1]))

        print(f"Best neighbor = {best_neighbor}, cost = {best_cost}")

        if best_cost >= current_cost:
            print("No improving neighbor found. Local optimum reached.")
            break

        current = best_neighbor
        print(f"Move to: {current}")
        print("-" * 60)
        step += 1

    print("\nFinal state:", current)
    print("Final cost:", cost(current))


def read_initial_state():
    while True:
        try:
            values = list(map(int, input(
                "Enter the initial state as 4 space-separated values "
                "(0-3), for example 3 1 2 0: "
            ).split()))
        except EOFError:
            print("\nInput interrupted. Exiting.")
            raise SystemExit(0)

        if len(values) == 4 and sorted(values) == [0, 1, 2, 3]:
            return values

        print("Invalid input. Enter each value from 0 to 3 exactly once.")


initial_state = read_initial_state()
hill_climb(initial_state)
