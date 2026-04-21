import math
import random
import time

class TrendingHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] > self.heap[p][0]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def heapify_down(self, i):
        n = len(self.heap)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i

            if l < n and self.heap[l][0] > self.heap[largest][0]:
                largest = l
            if r < n and self.heap[r][0] > self.heap[largest][0]:
                largest = r

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def push(self, post_id, likes, timestamp):
        self.heap.append((likes, post_id, timestamp))
        self.heapify_up(len(self.heap) - 1)

    def pop_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return top

    def peek_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def get_top_k(self, k):
        temp = TrendingHeap()
        temp.heap = self.heap.copy()
        result = []

        for _ in range(min(k, len(temp.heap))):
            result.append(temp.pop_max())

        return result

    def update_likes(self, post_id, new_likes, timestamp):
        for i in range(len(self.heap)):
            likes, pid, old_time = self.heap[i]
            if pid == post_id:
                old_likes = likes
                self.heap[i] = (new_likes, post_id, timestamp)

                if new_likes > old_likes:
                    self.heapify_up(i)
                else:
                    self.heapify_down(i)
                return True
        return False

    def size(self):
        return len(self.heap)

    def is_valid_heap(self):
        for i in range(1, len(self.heap)):
            p = (i - 1) // 2
            if self.heap[i][0] > self.heap[p][0]:
                return False
        return True

    def get_height(self):
        if len(self.heap) == 0:
            return 0
        return math.floor(math.log2(len(self.heap))) + 1

    def get_level_order(self):
        result = []
        index = 0
        level_size = 1

        while index < len(self.heap):
            result.append(self.heap[index:index + level_size])
            index += level_size
            level_size *= 2

        return result


h = TrendingHeap()
current_time = int(time.time())

for i in range(1, 101):
    h.push(i, random.randint(0, 1000), current_time)

for i in range(1, 10001):
    post_id = random.randint(1, 100)
    new_likes = random.randint(0, 1000)
    h.update_likes(post_id, new_likes, current_time + i)

    if i % 1000 == 0:
        print("Top 5 posts after", i, "updates:")
        for post in h.get_top_k(5):
            print(post)
        print()

print("Heap Size:", h.size())
print("Top Post:", h.peek_max())
print("Heap Height:", h.get_height())
print("Valid Heap:", h.is_valid_heap())

print("Level Order:")
for level in h.get_level_order():
    print(level)