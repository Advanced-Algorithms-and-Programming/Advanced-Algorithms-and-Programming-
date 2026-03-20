

class Post:
    def __init__(self, post_id, user_id, content_preview, timestamp, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.engagement_score = self.compute_score()

    def compute_score(self):
        return self.likes + 2 * self.comments + 3 * self.shares

    def __repr__(self):
        return f"Post(ID={self.post_id}, Score={self.engagement_score})"



def max_engagement(posts, left, right):
    if left == right:
        return posts[left]

    mid = (left + right) // 2

    left_max = max_engagement(posts, left, mid)
    right_max = max_engagement(posts, mid + 1, right)

    if left_max.engagement_score > right_max.engagement_score:
        return left_max
    else:
        return right_max



def sum_engagement(posts, left, right):
    if left == right:
        return posts[left].engagement_score

    mid = (left + right) // 2

    return sum_engagement(posts, left, mid) + sum_engagement(posts, mid + 1, right)


def avg_engagement(posts, left, right):
    total = sum_engagement(posts, left, right)
    n = right - left + 1
    return total / n



def count_above(posts, left, right, threshold):
    if left == right:
        if posts[left].engagement_score > threshold:
            return 1
        else:
            return 0

    mid = (left + right) // 2

    return count_above(posts, left, mid, threshold) + count_above(posts, mid + 1, right, threshold)


def merge(posts, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if posts[i].engagement_score <= posts[j].engagement_score:
            temp.append(posts[i])
            i += 1
        else:
            temp.append(posts[j])
            j += 1

    while i <= mid:
        temp.append(posts[i])
        i += 1

    while j <= right:
        temp.append(posts[j])
        j += 1

    for k in range(len(temp)):
        posts[left + k] = temp[k]


def merge_sort(posts, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(posts, left, mid)
    merge_sort(posts, mid + 1, right)
    merge(posts, left, mid, right)



def find_peak(hours, left, right, n):
    mid = (left + right) // 2

    if ((mid == 0 or hours[mid] >= hours[mid - 1]) and
        (mid == n - 1 or hours[mid] >= hours[mid + 1])):
        return mid

    if mid > 0 and hours[mid - 1] > hours[mid]:
        return find_peak(hours, left, mid - 1, n)

    return find_peak(hours, mid + 1, right, n)



posts = [
    Post(1, 101, "Post A", "2026-03-20 10:00", 100, 20, 10),   # 100 + 40 + 30 = 170
    Post(2, 102, "Post B", "2026-03-20 11:00", 200, 30, 20),   # 200 + 60 + 60 = 320
    Post(3, 103, "Post C", "2026-03-20 12:00", 50, 15, 5),     # 50 + 30 + 15 = 95
    Post(4, 104, "Post D", "2026-03-20 01:00", 150, 25, 20)    # 150 + 50 + 60 = 260
]

n = len(posts)


print("Engagement Scores:")
for post in posts:
    print(f"Post {post.post_id}: {post.engagement_score}")

print("\nMaximum Engagement Post:")
print(max_engagement(posts, 0, n - 1))

print("\nTotal Engagement:")
print(sum_engagement(posts, 0, n - 1))

print("\nAverage Engagement:")
print(avg_engagement(posts, 0, n - 1))

threshold = 200
print(f"\nCount of Posts Above Threshold {threshold}:")
print(count_above(posts, 0, n - 1, threshold))

print("\nPosts Before Sorting:")
print(posts)

merge_sort(posts, 0, n - 1)

print("\nPosts After Sorting by Engagement:")
print(posts)

hourly_data = [10, 20, 30, 25, 15]
peak_index = find_peak(hourly_data, 0, len(hourly_data) - 1, len(hourly_data))

print("\nHourly Data:")
print(hourly_data)
print("Peak Hour Index:", peak_index)
print("Peak Value:", hourly_data[peak_index])