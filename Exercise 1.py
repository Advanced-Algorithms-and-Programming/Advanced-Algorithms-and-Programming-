# -----------------------------
# Check whether invitation is valid
# -----------------------------

def is_valid_invitation(invited, graph):

    for i in range(len(invited)):
        for j in range(i + 1, len(invited)):

            user1 = invited[i]
            user2 = invited[j]

            if user2 in graph[user1]:
                return False

    return True


# -----------------------------
# Exact solution using backtracking
# -----------------------------

def find_max_invitations_exact(graph):

    nodes = list(graph.keys())
    best_set = []

    def backtrack(current_set, remaining_nodes):

        nonlocal best_set

        # Update best solution
        if len(current_set) > len(best_set):
            best_set = current_set[:]

        # Pruning condition
        if len(current_set) + len(remaining_nodes) <= len(best_set):
            return

        for i in range(len(remaining_nodes)):

            node = remaining_nodes[i]

            # Check conflicts
            valid = True

            for invited in current_set:
                if node in graph[invited]:
                    valid = False
                    break

            if valid:

                new_remaining = []

                for next_node in remaining_nodes[i + 1:]:

                    if next_node not in graph[node]:
                        new_remaining.append(next_node)

                current_set.append(node)

                backtrack(current_set, new_remaining)

                current_set.pop()

    backtrack([], nodes)

    return len(best_set), best_set


# -----------------------------
# Greedy heuristic solution
# -----------------------------

def find_max_invitations_greedy(graph):

    remaining = {node: set(neighbors) for node, neighbors in graph.items()}

    invited = []

    while remaining:

        # Select node with smallest degree
        node = min(remaining, key=lambda x: len(remaining[x]))

        invited.append(node)

        # Remove node and neighbors
        to_remove = set(remaining[node])
        to_remove.add(node)

        for r in to_remove:
            remaining.pop(r, None)

        for other in remaining:
            remaining[other] -= to_remove

    return len(invited), invited


# -----------------------------
# Example Graph
# -----------------------------

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


# -----------------------------
# Testing
# -----------------------------

print("Validation Test:")
print(is_valid_invitation(['A', 'D'], graph))

print("\nExact Solution:")
size, invited = find_max_invitations_exact(graph)
print(size, invited)

print("\nGreedy Solution:")
size, invited = find_max_invitations_greedy(graph)
print(size, invited)