class StoryNode:
    def __init__(self, story_id, user_id, content_preview, timestamp):
        self.story_id = story_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.views = 0
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_story(self, node):
        if self.head is None:
            self.head = self.tail = node
            self.current = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove_story(self, story_id):
        temp = self.head

        while temp:
            if temp.story_id == story_id:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev

                if self.current == temp:
                    self.current = temp.next

                self.size -= 1
                return True
            temp = temp.next
        return False

    def move_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.content_preview
        return None

    def move_backward(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.content_preview
        return None


    def jump_to(self, story_id):
        temp = self.head
        while temp:
            if temp.story_id == story_id:
                self.current = temp
                return temp.content_preview
            temp = temp.next
        return None


    def insert_after(self, current_id, new_story):
        temp = self.head
        while temp:
            if temp.story_id == current_id:
                new_story.next = temp.next
                new_story.prev = temp

                if temp.next:
                    temp.next.prev = new_story
                else:
                    self.tail = new_story

                temp.next = new_story
                self.size += 1
                return True
            temp = temp.next
        return False


    def display_around_current(self, k):
        temp = self.current


        for _ in range(k):
            if temp.prev:
                temp = temp.prev

        count = 0
        while temp and count < (2 * k + 1):
            print(temp.story_id, "-", temp.content_preview)
            temp = temp.next
            count += 1

    def track_view(self):
        if self.current:
            self.current.views += 1


    def most_viewed(self):
        temp = self.head
        max_story = None
        max_views = -1

        while temp:
            if temp.views > max_views:
                max_views = temp.views
                max_story = temp
            temp = temp.next

        return max_story

    def reorder_by_views(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head

            while temp.next:
                if temp.views < temp.next.views:
                    temp.story_id, temp.next.story_id = temp.next.story_id, temp.story_id
                    temp.user_id, temp.next.user_id = temp.next.user_id, temp.user_id
                    temp.content_preview, temp.next.content_preview = temp.next.content_preview, temp.content_preview
                    temp.timestamp, temp.next.timestamp = temp.next.timestamp, temp.timestamp
                    temp.views, temp.next.views = temp.next.views, temp.views
                    swapped = True
                temp = temp.next



feed = DoublyLinkedList()

s1 = StoryNode(1, 101, "Morning coffee", "08:00")
s2 = StoryNode(2, 102, "Workout complete", "09:00")
s3 = StoryNode(3, 103, "Sunset photo", "18:30")

feed.add_story(s1)
feed.add_story(s2)
feed.add_story(s3)

feed.jump_to(2)
feed.track_view()
feed.track_view()

feed.jump_to(3)
feed.track_view()

print("Most viewed story:", feed.most_viewed().content_preview)

feed.reorder_by_views()

print("Feed after reordering:")
temp = feed.head
while temp:
    print(temp.story_id, temp.content_preview, "Views:", temp.views)
    temp = temp.next