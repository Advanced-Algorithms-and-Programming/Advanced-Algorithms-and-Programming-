1. The Iterative Flattener

def flatten_iterative(root_comment):
result = []
stack = [(root_comment, "STATE_START")]
while stack:
current, state = stack.pop()
if state == "STATE_START":
result.append(current) 
stack.append((current, "STATE_REPLIES_DONE"))
for reply in reversed(current.replies):
stack.append((reply, "STATE_START"))
elif state == "STATE_REPLIES_DONE":
continue 
return result


2. Tail Recursion for Counting

def count_comments_tail(comment, accumulator=0):
total = accumulator + 1
for reply in comment.replies:
total = count_comments_tail(reply, total)
return total