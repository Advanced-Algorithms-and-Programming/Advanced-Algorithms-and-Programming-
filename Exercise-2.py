# Exercise: Social Network Friend Analysis

# 1. Mutual Friends
def mutual_friends(A, B):
    common = set()
    for friend in A:
        if friend in B:
            common.add(friend)
    return common


# 2. Unique Friends (A only)
def unique_from_a(A, B):
    unique = set()
    for friend in A:
        if friend not in B:
            unique.add(friend)
    return unique


# 3. Union of Friends
def combine_all(A, B):
    total = A.copy()
    for friend in B:
        total.add(friend)
    return total


# 4. Jaccard Similarity
def jaccard_similarity(A, B):
    inter = mutual_friends(A, B)
    union = combine_all(A, B)

    if len(union) == 0:
        return 0

    return len(inter) / len(union)


# 5. Friend Suggestion
def suggest_friends(user_id, user_friends, network):
    suggestions = set()

    for friend in user_friends:
        friends_of_friend = network.get(friend, set())

        for person in friends_of_friend:
            if person != user_id and person not in user_friends:
                suggestions.add(person)

    return suggestions


