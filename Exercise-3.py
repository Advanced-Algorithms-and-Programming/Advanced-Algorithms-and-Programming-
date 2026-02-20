

# Cosine Similarity

def cosine_similarity(matrix, user_a, user_b):
    dot = 0
    norm_a = 0
    norm_b = 0

    for k in range(len(matrix[0])):
        dot += matrix[user_a][k] * matrix[user_b][k]
        norm_a += matrix[user_a][k] ** 2
        norm_b += matrix[user_b][k] ** 2

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot / (math.sqrt(norm_a) * math.sqrt(norm_b))


# Top-K Similar Users- excluding friends

def top_k_similar_users(matrix, target, k, friends):
    similarities = []

    for user in range(len(matrix)):
        if user != target and user not in friends[target]:
            sim = cosine_similarity(matrix, target, user)
            similarities.append((user, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:k]





def recommend_interests(matrix, target, k, friends):
    similar_users = top_k_similar_users(matrix, target, k, friends)
    num_interests = len(matrix[0])
    scores = [0] * num_interests

    for user, _ in similar_users:
        for i in range(num_interests):
            if matrix[target][i] == 0:
                scores[i] += matrix[user][i]

    return scores
