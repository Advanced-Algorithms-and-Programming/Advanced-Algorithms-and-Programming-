import random

class PostNode:
    def __init__(self, post_id, likes, comments, shares, timestamp):
        self.post_id = post_id
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.timestamp = timestamp
        self.engagement_score = (likes * 1) + (comments * 2) + (shares * 3)
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0



def enqueue(queue, new_post):
    if queue.head is None or new_post.engagement_score > queue.head.engagement_score:
        new_post.next = queue.head
        queue.head = new_post
    else:
        current = queue.head

        while (current.next is not None and
               current.next.engagement_score >= new_post.engagement_score):
            current = current.next

        new_post.next = current.next
        current.next = new_post

    queue.size += 1

def dequeue_max(queue):
    if queue.head is None:
        return None

    max_post = queue.head
    queue.head = queue.head.next
    queue.size -= 1

    return max_post



def peek_max(queue):
    if queue.head is None:
        return None
    return queue.head


def update_score(queue, target_id, new_likes, new_comments, new_shares):
    if queue.head is None:
        return

    dummy = PostNode(-1, 0, 0, 0, 0)
    dummy.next = queue.head

    current = dummy
    extracted_post = None

    while current.next is not None:
        if current.next.post_id == target_id:
            extracted_post = current.next
            current.next = current.next.next
            queue.size -= 1
            break
        current = current.next

    queue.head = dummy.next

    if extracted_post:
        extracted_post.likes = new_likes
        extracted_post.comments = new_comments
        extracted_post.shares = new_shares

        extracted_post.engagement_score = (
            new_likes * 1 + new_comments * 2 + new_shares * 3
        )

        enqueue(queue, extracted_post)

def refresh_all(queue):
    temp_list = []

    while queue.head is not None:
        temp_list.append(dequeue_max(queue))

    for post in temp_list:
        post.engagement_score = (
            post.likes * 1 + post.comments * 2 + post.shares * 3
        )
        enqueue(queue, post)



def get_top_k(queue, k):
    top_posts = []
    current = queue.head
    count = 0

    while current is not None and count < k:
        top_posts.append(current)
        current = current.next
        count += 1

    return top_posts


def decay_older_than(queue, target_time):
    temp_list = []

    while queue.head is not None:
        temp_list.append(dequeue_max(queue))

    for post in temp_list:
        if post.timestamp < target_time:
            post.engagement_score *= 0.8

        enqueue(queue, post)



class DualQueue:
    def __init__(self):
        self.viral_queue = PriorityQueue()
        self.normal_queue = PriorityQueue()


def dual_enqueue(dual_queue, new_post):
    if new_post.engagement_score > 100:
        enqueue(dual_queue.viral_queue, new_post)
    else:
        enqueue(dual_queue.normal_queue, new_post)


def dual_dequeue(dual_queue):

    if dual_queue.viral_queue.head is None and dual_queue.normal_queue.head is None:
        return None

    if dual_queue.viral_queue.head is None:
        return dequeue_max(dual_queue.normal_queue)

    if dual_queue.normal_queue.head is None:
        return dequeue_max(dual_queue.viral_queue)

    random_value = random.random()

    if random_value <= 0.70:
        return dequeue_max(dual_queue.viral_queue)
    else:
        return dequeue_max(dual_queue.normal_queue)


if __name__ == "__main__":

    pq = PriorityQueue()

    p1 = PostNode(1, 10, 2, 1, 100)
    p2 = PostNode(2, 50, 5, 2, 120)
    p3 = PostNode(3, 5, 1, 0, 80)

    enqueue(pq, p1)
    enqueue(pq, p2)
    enqueue(pq, p3)

    print("Top Post:", peek_max(pq).post_id)

    update_score(pq, 3, 20, 5, 2)

    top_posts = get_top_k(pq, 2)
    print("Top 2 Posts:", [p.post_id for p in top_posts])