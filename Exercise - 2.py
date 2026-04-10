class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_friendship(self, u, v):
        self.add_user(u)
        self.add_user(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def dfs_recursive(self, start_user):
        if start_user not in self.graph:
            return []

        visited = set()
        result = []

        def dfs_helper(user):
            if user in visited:
                return
            visited.add(user)
            result.append(user)
            for friend in self.graph[user]:
                if friend not in visited:
                    dfs_helper(friend)

        dfs_helper(start_user)
        return result

    def dfs_iterative(self, start_user):
        if start_user not in self.graph:
            return []

        visited = set()
        result = []
        stack = [start_user]

        while stack:
            user = stack.pop()
            if user not in visited:
                visited.add(user)
                result.append(user)
                for friend in reversed(self.graph[user]):
                    if friend not in visited:
                        stack.append(friend)

        return result

    def find_connected_components(self):
        visited = set()
        components = []

        for user in self.graph:
            if user not in visited:
                component = []
                stack = [user]

                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        component.append(current)
                        for friend in reversed(self.graph[current]):
                            if friend not in visited:
                                stack.append(friend)

                components.append(component)

        return components

    def is_connected(self):
        if not self.graph:
            return True
        return len(self.find_connected_components()) == 1

    def has_path(self, start_user, target_user):
        if start_user not in self.graph or target_user not in self.graph:
            return False

        visited = set()

        def dfs(user):
            if user == target_user:
                return True
            visited.add(user)
            for friend in self.graph[user]:
                if friend not in visited:
                    if dfs(friend):
                        return True
            return False

        return dfs(start_user)

    def find_path(self, start_user, target_user):
        if start_user not in self.graph or target_user not in self.graph:
            return []

        visited = set()
        path = []

        def dfs(user):
            visited.add(user)
            path.append(user)

            if user == target_user:
                return True

            for friend in self.graph[user]:
                if friend not in visited:
                    if dfs(friend):
                        return True

            path.pop()
            return False

        if dfs(start_user):
            return path
        return []

    def get_connected_components_sizes(self):
        components = self.find_connected_components()
        return [len(component) for component in components]

    def find_largest_component(self):
        components = self.find_connected_components()
        if not components:
            return []
        largest = components[0]
        for component in components:
            if len(component) > len(largest):
                largest = component
        return largest

    def find_isolated_users(self):
        isolated = []
        for user in self.graph:
            if len(self.graph[user]) == 0:
                isolated.append(user)
        return isolated


g = SocialGraph()

g.add_friendship("A", "B")
g.add_friendship("B", "C")
g.add_friendship("D", "E")
g.add_user("F")

print("Recursive DFS from A:", g.dfs_recursive("A"))
print("Iterative DFS from A:", g.dfs_iterative("A"))
print("Connected Components:", g.find_connected_components())
print("Is Graph Connected?:", g.is_connected())
print("Has Path A to C?:", g.has_path("A", "C"))
print("Has Path A to E?:", g.has_path("A", "E"))
print("Find Path A to C:", g.find_path("A", "C"))
print("Find Path A to E:", g.find_path("A", "E"))
print("Connected Component Sizes:", g.get_connected_components_sizes())
print("Largest Component:", g.find_largest_component())
print("Isolated Users:", g.find_isolated_users())