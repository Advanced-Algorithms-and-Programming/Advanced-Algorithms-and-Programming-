def is_valid_labeling(labeling, graph):
    for user in graph:
        for friend in graph[user]:
            if labeling[user] == labeling[friend]:
                return False
    return True


def assign_labels(k, graph):
    users = list(graph.keys())
    labeling = {user: -1 for user in users}

    def backtrack(index):
        if index == len(users):
            return True

        user = users[index]

        for label in range(k):
            valid = True

            for friend in graph[user]:
                if labeling[friend] == label:
                    valid = False
                    break

            if valid:
                labeling[user] = label

                if backtrack(index + 1):
                    return True

                labeling[user] = -1

        return False

    success = backtrack(0)
    return success, labeling


def find_min_labels(graph):
    for k in range(1, len(graph) + 1):
        success, labeling = assign_labels(k, graph)

        if success:
            return k, labeling

    return len(graph), {user: user for user in graph}


# Example graph
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

minimum_labels, final_labeling = find_min_labels(graph)

print("Minimum labels needed:", minimum_labels)
print("Final labeling:", final_labeling)
print("Is valid:", is_valid_labeling(final_labeling, graph))