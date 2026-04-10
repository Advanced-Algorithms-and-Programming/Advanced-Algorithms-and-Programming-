from collections import deque, defaultdict

class SocialGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = defaultdict(set)

    # Add friendship
    def add_friendship(self, u, v):
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    # Remove friendship
    def remove_friendship(self, u, v):
        self.adj_list[u].discard(v)
        self.adj_list[v].discard(u)

    # Check friendship
    def are_friends(self, u, v):
        return v in self.adj_list[u]

    # Get friends
    def get_friends(self, u):
        return list(self.adj_list[u])

    # Degree
    def get_degree(self, u):
        return len(self.adj_list[u])

    # Friend recommendations (friends of friends)
    def recommend_friends(self, user):
        recommendations = set()
        for friend in self.adj_list[user]:
            for fof in self.adj_list[friend]:
                if fof != user and fof not in self.adj_list[user]:
                    recommendations.add(fof)
        return list(recommendations)

    # BFS shortest path
    def shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    # Find isolated users
    def find_isolated_users(self):
        return [u for u in range(1, self.n + 1) if len(self.adj_list[u]) == 0]

    # DFS for connected components
    def connected_components(self):
        visited = set()
        components = []

        for user in range(1, self.n + 1):
            if user not in visited:
                stack = [user]
                component = []

                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        component.append(node)
                        stack.extend(self.adj_list[node] - visited)

                components.append(component)
        return components

    # BFS distance distribution (Six Degrees)
    def bfs_distances(self, start):
        dist = {start: 0}
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in self.adj_list[node]:
                if neighbor not in dist:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        return dist


# Example Usage
g = SocialGraph(5)

g.add_friendship(1, 2)
g.add_friendship(1, 3)
g.add_friendship(2, 4)
g.add_friendship(3, 5)

print("Recommendations for 1:", g.recommend_friends(1))
print("Shortest path 1 to 5:", g.shortest_path(1, 5))
print("Isolated users:", g.find_isolated_users())
print("Connected components:", g.connected_components())
print("Distances from 1:", g.bfs_distances(1))