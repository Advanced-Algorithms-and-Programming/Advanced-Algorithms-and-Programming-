class CommentNode:
    def __init__(self, comment_id, user_id, content, timestamp, likes):
        self.comment_id = comment_id
        self.user_id = user_id
        self.content = content[:100]  # limit to 100 chars
        self.timestamp = timestamp
        self.likes = likes
        self.replies = []

    def add_reply(self, reply):
        self.replies.append(reply)


# 1. Display Thread
def display_thread(comment, level=0):
    print("  " * level + f"{comment.comment_id} ({comment.user_id}): {comment.content}")
    for reply in comment.replies:
        display_thread(reply, level + 1)


# 2. Count Total Comments
def count_total_comments(comment):
    count = 1
    for reply in comment.replies:
        count += count_total_comments(reply)
    return count


# 3. Total Likes
def total_likes(comment):
    total = comment.likes
    for reply in comment.replies:
        total += total_likes(reply)
    return total


# 4. Find Deepest Reply
def find_deepest_reply(comment):
    if not comment.replies:
        return 1

    max_depth = 0
    for reply in comment.replies:
        depth = find_deepest_reply(reply)
        max_depth = max(max_depth, depth)

    return max_depth + 1


# 5. Search by User
def search_by_user(user_id, comment):
    result = []

    if comment.user_id == user_id:
        result.append(comment)

    for reply in comment.replies:
        result.extend(search_by_user(user_id, reply))

    return result


# 6. Contains Keyword
def contains_keyword(keyword, comment):
    if keyword.lower() in comment.content.lower():
        return True

    for reply in comment.replies:
        if contains_keyword(keyword, reply):
            return True

    return False


# 7. Delete Comment (Cascade)
def delete_comment(comment_id, comment):
    if comment.comment_id == comment_id:
        return None

    new_replies = []
    for reply in comment.replies:
        updated = delete_comment(comment_id, reply)
        if updated is not None:
            new_replies.append(updated)

    comment.replies = new_replies
    return comment


c101 = CommentNode(101, "Alice", "This recipe looks amazing!", "t1", 5)
c201 = CommentNode(201, "Bob", "I tried it last night!", "t2", 3)
c301 = CommentNode(301, "Alice", "What did you think?", "t3", 2)
c401 = CommentNode(401, "Bob", "It was delicious!", "t4", 4)
c202 = CommentNode(202, "Charlie", "Can I use olive oil instead?", "t5", 1)
c302 = CommentNode(302, "Alice", "Yes, that works too!", "t6", 2)

c101.add_reply(c201)
c101.add_reply(c202)
c201.add_reply(c301)
c301.add_reply(c401)
c202.add_reply(c302)
print("Display Thread:")
display_thread(c101)

print("\nTotal Comments:", count_total_comments(c101))
print("Total Likes:", total_likes(c101))
print("Max Depth:", find_deepest_reply(c101))

print("\nSearch by User (Alice):")
for c in search_by_user("Alice", c101):
    print(c.comment_id, c.content)

print("\nContains 'delicious':", contains_keyword("delicious", c101))
print("\nDelete Comment 201:")
new_tree = delete_comment(201, c101)
print("\nThread After Deletion:")
display_thread(new_tree)