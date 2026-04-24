class UserNode:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends
        self.left = None
        self.right = None


class UserBST:
    def __init__(self):
        self.root = None

    def insert(self, user_id, name, friends):
        new_node = UserNode(user_id, name, friends)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if user_id < current.user_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif user_id > current.user_id:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                print("User ID already exists")
                return

    def find(self, user_id):
        current = self.root

        while current:
            if user_id == current.user_id:
                return current
            elif user_id < current.user_id:
                current = current.left
            else:
                current = current.right

        return None


    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.user_id)
            self._inorder_helper(node.right, result)

    # Delete user
    def delete(self, user_id):
        self.root = self._delete_helper(self.root, user_id)

    def _delete_helper(self, node, user_id):
        if node is None:
            return None

        if user_id < node.user_id:
            node.left = self._delete_helper(node.left, user_id)

        elif user_id > node.user_id:
            node.right = self._delete_helper(node.right, user_id)

        else:
            # No child
            if node.left is None and node.right is None:
                return None

            # One child
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            # Two children
            successor = self._find_smallest(node.right)

            node.user_id = successor.user_id
            node.name = successor.name
            node.friends = successor.friends

            node.right = self._delete_helper(node.right, successor.user_id)

        return node

    def _find_smallest(self, node):
        while node.left:
            node = node.left
        return node

    # Friend Suggestions
    def suggest_friends(self, user_id, max_suggestions=5):
        user = self.find(user_id)

        if user is None:
            return []

        direct_friends = set(user.friends)
        suggestions = {}

        for friend_id in direct_friends:
            friend_node = self.find(friend_id)

            if friend_node:
                for fof in friend_node.friends:
                    if fof != user_id and fof not in direct_friends:
                        suggestions[fof] = suggestions.get(fof, 0) + 1

        sorted_suggestions = sorted(
            suggestions.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_suggestions[:max_suggestions]

    def get_height(self):
        return self._height_helper(self.root)

    def _height_helper(self, node):
        if node is None:
            return 0

        return 1 + max(
            self._height_helper(node.left),
            self._height_helper(node.right)
        )

    def is_balanced(self):
        return self._balanced_helper(self.root)

    def _balanced_helper(self, node):
        if node is None:
            return True

        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return (
            self._balanced_helper(node.left)
            and self._balanced_helper(node.right)
        )


    def get_leaf_count(self):
        return self._leaf_helper(self.root)

    def _leaf_helper(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self._leaf_helper(node.left) + self._leaf_helper(node.right)


tree = UserBST()

tree.insert(50, "Alice", [30, 70])
tree.insert(30, "Bob", [50, 20])
tree.insert(70, "Charlie", [50, 90])
tree.insert(20, "David", [30])
tree.insert(90, "Eva", [70])

print("Sorted Users:", tree.inorder_traversal())

user = tree.find(30)
if user:
    print("Found User:", user.name)

print("Friend Suggestions for 50:", tree.suggest_friends(50))

print("Tree Height:", tree.get_height())
print("Balanced:", tree.is_balanced())
print("Leaf Nodes:", tree.get_leaf_count())

tree.delete(30)
print("After Deletion:", tree.inorder_traversal())