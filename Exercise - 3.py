class GeneralizedCategoryNode:
def __init__(self, category_id, name, post_count=0):
self.category_id = category_id
self.name = name
self.post_count = post_count
self.children = []

def add_child(self, child_node):
self.children.append(child_node)

def level_order_generalized(root):
"""Breadth-first search to print the tree level by level."""
if not root:
return []

result = []
queue = [root]

while queue:
current = queue.pop(0)
result.append(current.name)
# Add all children of the current node to the back of the queue
queue.extend(current.children)

return result

def calculate_fan_out(root):
"""Finds the maximum number of direct children any single node has."""
if not root:
return 0

max_fan_out = len(root.children)

for child in root.children:
max_fan_out = max(max_fan_out, calculate_fan_out(child))

return max_fan_out

if __name__ == "__main__":

print("Test Case 1: Standard Multi-Level Tree ")
tech = GeneralizedCategoryNode("1", "Tech")
prog = GeneralizedCategoryNode("2", "Programming")
design = GeneralizedCategoryNode("3", "Design")
python = GeneralizedCategoryNode("4", "Python")
java = GeneralizedCategoryNode("5", "Java")

tech.add_child(prog)
tech.add_child(design)
prog.add_child(python)
prog.add_child(java)

print("Level-Order Output:", level_order_generalized(tech))
print("Fan-Out:", calculate_fan_out(tech))
print("\n")


print("Test Case 2: Single Node (Empty Hierarchy)")
single_node = GeneralizedCategoryNode("6", "Tech")

print("Level-Order Output:", level_order_generalized(single_node))
print("Fan-Out:", calculate_fan_out(single_node))
print("\n")


print("Test Case 3: Flat Tree (High Fan-Out) ")
root_node = GeneralizedCategoryNode("7", "Root")

for i in range(1, 6):
root_node.add_child(GeneralizedCategoryNode(f"child_{i}", f"Child{i}"))

print("Level-Order Output:", level_order_generalized(root_node))
print("Fan-Out:", calculate_fan_out(root_node))