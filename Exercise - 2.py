class CategoryNode:
    def __init__(self, name, post_count):
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None


def in_order_collect(node):
    if node is None:
        return []
    result = []
    result += in_order_collect(node.left)
    result.append(node.name)
    result += in_order_collect(node.right)
    return result


def in_order_accumulate_posts(node, total=0):
    if node is None:
        return total
    total = in_order_accumulate_posts(node.left, total)
    total = total + node.post_count
    total = in_order_accumulate_posts(node.right, total)
    return total


def in_order_find_kth(node, k):
    count = [0]
    def helper(node):
        if node is None:
            return None
        left = helper(node.left)
        if left is not None:
            return left
        count[0] += 1
        if count[0] == k:
            return node.name
        return helper(node.right)
    return helper(node)


def pre_order_export(node, level=0):
    if node is None:
        return ""
    indent = " " * level
    result = indent + f"{node.name}({node.post_count})\n"
    result += pre_order_export(node.left, level + 1)
    result += pre_order_export(node.right, level + 1)
    return result


def pre_order_copy(node):
    if node is None:
        return None
    new_node = CategoryNode(node.name, node.post_count)
    new_node.left = pre_order_copy(node.left)
    new_node.right = pre_order_copy(node.right)
    return new_node


def pre_order_serialize(node):
    if node is None:
        return ""
    result = f"{node.name}({node.post_count})|"
    result += pre_order_serialize(node.left)
    result += pre_order_serialize(node.right)
    return result


def post_order_total_posts(node):
    if node is None:
        return 0
    left_sum = post_order_total_posts(node.left)
    right_sum = post_order_total_posts(node.right)
    return left_sum + right_sum + node.post_count


def post_order_average_depth(node):
    def helper(node, depth):
        if node is None:
            return 0, 0
        if node.left is None and node.right is None:
            return depth, 1
        left_sum, left_count = helper(node.left, depth + 1)
        right_sum, right_count = helper(node.right, depth + 1)
        return left_sum + right_sum, left_count + right_count
    total_depth, leaf_count = helper(node, 0)
    if leaf_count == 0:
        return 0
    return total_depth / leaf_count


def post_order_collect_leaves(node):
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.name]
    result = []
    result += post_order_collect_leaves(node.left)
    result += post_order_collect_leaves(node.right)
    return result


def find_most_popular_category(node):
    if node is None:
        return None
    max_node = node
    left = find_most_popular_category(node.left)
    right = find_most_popular_category(node.right)
    if left is not None and left.post_count > max_node.post_count:
        max_node = left
    if right is not None and right.post_count > max_node.post_count:
        max_node = right
    return max_node


def category_with_most_subcategories(node):
    if node is None:
        return None, -1
    count = 0
    if node.left is not None:
        count += 1
    if node.right is not None:
        count += 1
    best_node = node
    best_count = count
    left_node, left_count = category_with_most_subcategories(node.left)
    right_node, right_count = category_with_most_subcategories(node.right)
    if left_count > best_count:
        best_node = left_node
        best_count = left_count
    if right_count > best_count:
        best_node = right_node
        best_count = right_count
    return best_node, best_count


if __name__ == "__main__":
    root = CategoryNode("Technology", 150)
    root.left = CategoryNode("Programming", 85)
    root.right = CategoryNode("Design", 60)

    root.left.left = CategoryNode("Python", 42)
    root.left.right = CategoryNode("Java", 30)

    root.right.right = CategoryNode("UIUX", 25)

    print("In-order Collect:", in_order_collect(root))
    print("Total Posts:", in_order_accumulate_posts(root))
    print("3rd Node:", in_order_find_kth(root, 3))

    print(pre_order_export(root))
    print("Serialized:", pre_order_serialize(root))

    print("Total Posts (Post-order):", post_order_total_posts(root))
    print("Average Depth:", post_order_average_depth(root))
    print("Leaf Nodes:", post_order_collect_leaves(root))

    most_popular = find_most_popular_category(root)
    print("Most Popular:", most_popular.name, most_popular.post_count)

    node, count = category_with_most_subcategories(root)
    print("Most Subcategories:", node.name, count)