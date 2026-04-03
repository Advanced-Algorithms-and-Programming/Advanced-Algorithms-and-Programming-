class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

def calculate_height(node):
    if node is None:
        return -1
    return 1 + max(calculate_height(node.left), calculate_height(node.right))


def calculate_node_height(node, target_id, level=0):
    if node is None:
        return -1
    if node.category_id == target_id:
        return level

    left = calculate_node_height(node.left, target_id, level + 1)
    if left != -1:
        return left

    return calculate_node_height(node.right, target_id, level + 1)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def is_balanced(node):
    if node is None:
        return True

    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


def is_full_binary_tree(node):
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left and node.right:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)

    return False


def is_perfect_binary_tree(node):
    h = calculate_height(node)
    total_nodes = count_nodes(node)
    return total_nodes == (2 ** (h + 1) - 1)


from collections import deque

def is_complete_binary_tree(root):
    if root is None:
        return True

    queue = deque([root])
    found_null = False

    while queue:
        node = queue.popleft()

        if node is None:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


def find_category(node, target_id):
    if node is None:
        return None

    if node.category_id == target_id:
        return node

    left = find_category(node.left, target_id)
    if left:
        return left

    return find_category(node.right, target_id)


def find_path_to_root(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path


def lowest_common_ancestor(node, id1, id2):
    if node is None:
        return None

    if node.category_id == id1 or node.category_id == id2:
        return node

    left = lowest_common_ancestor(node.left, id1, id2)
    right = lowest_common_ancestor(node.right, id1, id2)

    if left and right:
        return node

    return left if left else right




def build_sample_tree():
    tech = CategoryNode(1, "Technology", 150)
    prog = CategoryNode(2, "Programming", 85)
    design = CategoryNode(3, "Design", 65)
    python = CategoryNode(4, "Python", 42)
    java = CategoryNode(5, "Java", 30)
    uiux = CategoryNode(6, "UI/UX", 38)
    graphics = CategoryNode(7, "Graphics", 22)
    django = CategoryNode(8, "Django", 18)
    flask = CategoryNode(9, "Flask", 12)


    tech.left = prog
    tech.right = design

    prog.parent = tech
    design.parent = tech

    prog.left = python
    prog.right = java
    python.parent = prog
    java.parent = prog

    design.left = uiux
    design.right = graphics
    uiux.parent = design
    graphics.parent = design

    python.left = django
    python.right = flask
    django.parent = python
    flask.parent = python

    return tech


if __name__ == "__main__":
    root = build_sample_tree()

    print("Tree Height:", calculate_height(root))
    print("Height of Java:", calculate_node_height(root, 5))
    print("Total Nodes:", count_nodes(root))
    print("Leaf Nodes:", count_leaves(root))
    print("Is Balanced:", is_balanced(root))

    node = find_category(root, 4)
    print("Found Category:", node.name if node else "Not found")

    django_node = find_category(root, 8)
    print("Path to Root:", find_path_to_root(django_node))

    lca = lowest_common_ancestor(root, 8, 5)
    print("LCA of Django & Java:", lca.name if lca else "None")

    print("Is Full:", is_full_binary_tree(root))
    print("Is Perfect:", is_perfect_binary_tree(root))
    print("Is Complete:", is_complete_binary_tree(root))