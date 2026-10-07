# Vacuum Cleaner Agent
print("Hanish S Adhi - 1BM24CS109")
def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


def goal_based_agent(location, status, goal):
    if status == "Dirty":
        return "Suck"

    if location != goal:
        if location == "A":
            return "Move Right"
        else:
            return "Move Left"

    return "Goal Reached"


def vacuum_cleaner():
    location = input("Enter starting location (A/B): ").upper()
    status_a = input("Enter status of A (Clean/Dirty): ").capitalize()
    status_b = input("Enter status of B (Clean/Dirty): ").capitalize()

    print("\n--- Simple Reflex Agent ---")

    current_location = location

    while True:
        if current_location == "A":
            status = status_a
        else:
            status = status_b

        action = simple_reflex_agent(current_location, status)

        print("Location:", current_location,
              "Status:", status,
              "Action:", action)

        if action == "Suck":
            if current_location == "A":
                status_a = "Clean"
            else:
                status_b = "Clean"

        elif action == "Move Right":
            current_location = "B"

        elif action == "Move Left":
            current_location = "A"

        if status_a == "Clean" and status_b == "Clean":
            break

    print("Both rooms are clean!")

    print("\n--- Goal-Based Agent ---")

    current_location = location
    goal = "B"

    for i in range(5):
        if current_location == "A":
            status = status_a
        else:
            status = status_b

        action = goal_based_agent(current_location, status, goal)

        print("Location:", current_location,
              "Status:", status,
              "Action:", action)

        if action == "Goal Reached":
            break

        if action == "Suck":
            if current_location == "A":
                status_a = "Clean"
            else:
                status_b = "Clean"

        elif action == "Move Right":
            current_location = "B"

        elif action == "Move Left":
            current_location = "A"


vacuum_cleaner()