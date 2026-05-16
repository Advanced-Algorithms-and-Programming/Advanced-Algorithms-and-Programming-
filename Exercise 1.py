from itertools import combinations


def is_valid_coverage(selected_users, graph):

    covered = set()

    for user in selected_users:


        covered.add(user)


        for friend in graph[user]:
            covered.add(friend)


    for node in graph:
        if node not in covered:
            return False

    return True



def find_minimum_coverage(graph):

    nodes = list(graph.keys())
    n = len(nodes)

    best_solution = None
    best_size = float('inf')

    # try subsets from small to large
    for r in range(n + 1):

        for subset in combinations(nodes, r):

            if is_valid_coverage(subset, graph):

                best_solution = list(subset)
                best_size = len(subset)

                return best_size, best_solution

    return None



def find_fast_coverage(graph):

    uncovered = set(graph.keys())
    selected = []

    while uncovered:

        best_node = None
        best_cover = set()

        for node in graph:

            current_cover = {node}

            for neighbor in graph[node]:

                if neighbor in uncovered:
                    current_cover.add(neighbor)

            # choose node covering maximum uncovered nodes
            if len(current_cover & uncovered) > len(best_cover):

                best_cover = current_cover & uncovered
                best_node = node

        selected.append(best_node)

        # remove covered nodes
        uncovered -= best_cover

    return len(selected), selected



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}


exact_size, exact_users = find_minimum_coverage(graph)

print("Exact Minimum Coverage")
print("Size:", exact_size)
print("Users:", exact_users)



greedy_size, greedy_users = find_fast_coverage(graph)

print("\nGreedy Coverage")
print("Size:", greedy_size)
print("Users:", greedy_users)