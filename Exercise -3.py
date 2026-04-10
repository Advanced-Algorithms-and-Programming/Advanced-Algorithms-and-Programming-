from collections import deque, defaultdict

class SocialGraph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    # Add friendship
    def add_friendship(self, u, v):
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    # Get friends
    def get_friends(self, u):
        return self.adj_list[u]

    # Get all users
    def get_all_users(self):
        return self.adj_list.keys()


    def bfs(self, start):
        visited = set([start])
        queue = deque([start])
        result = []

        while queue:
            u = queue.popleft()
            result.append(u)

            for v in self.get_friends(u):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return result

    def bfs_distances(self, start):
        dist = {start: 0}
        queue = deque([start])

        while queue:
            u = queue.popleft()

            for v in self.get_friends(u):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return dist

    def shortest_path(self, start, target):
        if start == target:
            return [start]

        queue = deque([start])
        visited = set([start])
        pred = {}

        while queue:
            u = queue.popleft()

            if u == target:
                break

            for v in self.get_friends(u):
                if v not in visited:
                    visited.add(v)
                    pred[v] = u
                    queue.append(v)

        if target not in pred:
            return []

        # Reconstruct path
        path = []
        curr = target

        while curr in pred:
            path.insert(0, curr)
            curr = pred[curr]

        path.insert(0, start)
        return path

    def degrees_of_separation(self, start, target):
        dist = self.bfs_distances(start)
        return dist[target] if target in dist else -1

    def friends_k_hops(self, start, k):
        dist = self.bfs_distances(start)
        result = []

        for user, d in dist.items():
            if 0 < d <= k:
                result.append(user)

        return result
    def compute_average_degrees(self):
        total_dist = 0
        pairs = 0

        for u in self.get_all_users():
            dist = self.bfs_distances(u)

            for v, d in dist.items():
                if d > 0:
                    total_dist += d
                    pairs += 1

        return total_dist / pairs if pairs > 0 else 0


    def get_distance_distribution(self, start):
        dist = self.bfs_distances(start)
        freq = {}

        for v, d in dist.items():
            if d > 0:
                if d not in freq:
                    freq[d] = 0
                freq[d] += 1

        return freq
    def recommend_friends(self, start, max_recommendations=5):
        recs = {}
        friends = self.get_friends(start)

        for f in friends:
            for fof in self.get_friends(f):
                if fof != start and fof not in friends:
                    if fof not in recs:
                        recs[fof] = 0
                    recs[fof] += 1

        # Sort by highest mutual friends
        sorted_recs = sorted(recs, key=recs.get, reverse=True)

        return sorted_recs[:max_recommendations]


g = SocialGraph()

g.add_friendship(1, 2)
g.add_friendship(1, 3)
g.add_friendship(2, 4)
g.add_friendship(3, 5)

print("BFS:", g.bfs(1))
print("Distances:", g.bfs_distances(1))
print("Shortest Path 1→5:", g.shortest_path(1, 5))
print("Degrees (1→5):", g.degrees_of_separation(1, 5))
print("Within 2 hops:", g.friends_k_hops(1, 2))
print("Recommendations:", g.recommend_friends(1))
print("Distance Distribution:", g.get_distance_distribution(1))
print("Average Degrees:", g.compute_average_degrees())