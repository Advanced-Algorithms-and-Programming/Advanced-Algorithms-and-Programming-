class ActivityNode:
    def __init__(self, activity):
        self.activity_type = activity
        self.next = None


class ActivityStack:
    def __init__(self):
        self.top = None
        self.count = 0


    
    def push(self, activity):

        new_node = ActivityNode(activity)

        new_node.next = self.top

        self.top = new_node

        self.count += 1


    
    def pop(self):

        if self.top is None:
            return "Stack Empty"

        temp = self.top

        self.top = self.top.next

        self.count -= 1

        return temp.activity_type


    
    def peek(self):

        if self.top is None:
            return "Stack Empty"

        return self.top.activity_type


    
    def is_empty(self):

        return self.top is None


    
    def size(self):

        return self.count


   
    def display_recent(self, n):

        current = self.top

        count = 0

        while current is not None and count < n:

            print(current.activity_type)

            current = current.next

            count += 1



def undo_last(activity_stack, undo_stack):

    last_activity = activity_stack.pop()

    if last_activity != "Stack Empty":
        undo_stack.push(last_activity)

    return last_activity




class NotificationNode:

    def __init__(self, notification):

        self.notification = notification

        self.next = None


class NotificationQueue:

    def __init__(self):

        self.front = None

        self.rear = None

        self.count = 0


    
    def enqueue(self, notification):

        new_node = NotificationNode(notification)

        if self.rear is None:

            self.front = new_node

            self.rear = new_node

        else:

            self.rear.next = new_node

            self.rear = new_node

        self.count += 1


    
    def dequeue(self):

        if self.front is None:
            return "Queue Empty"

        temp = self.front

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1

        return temp.notification


    
    def peek_front(self):

        if self.front is None:
            return "Queue Empty"

        return self.front.notification


    
    def is_empty(self):

        return self.front is None


    
    def size(self):

        return self.count


    
    def display_pending(self):

        current = self.front

        while current is not None:

            print(current.notification)

            current = current.next


    
    def priority_enqueue(self, notification):

        new_node = NotificationNode(notification)

        new_node.next = self.front

        self.front = new_node

        if self.rear is None:
            self.rear = new_node

        self.count += 1




class FeedProcessor:

    def __init__(self):

        self.recent_activities = ActivityStack()

        self.notification_queue = NotificationQueue()

        self.processed_log = NotificationQueue()


    
    def process_incoming(self):

        notification = self.notification_queue.dequeue()

        if notification != "Queue Empty":

            self.recent_activities.push(notification)


    
    def batch_process(self, k):

        for i in range(k):

            self.process_incoming()


    
    def clear_history(self):

        while not self.recent_activities.is_empty():

            activity = self.recent_activities.pop()

            self.processed_log.enqueue(activity)


    
    def get_stats(self):

        return (
            self.recent_activities.size(),
            self.notification_queue.size(),
            self.processed_log.size()
        )




if __name__ == "__main__":

    system = FeedProcessor()

    system.notification_queue.enqueue("User1 liked your post")

    system.notification_queue.enqueue("User2 commented")

    system.notification_queue.enqueue("User3 followed you")

    system.notification_queue.priority_enqueue("URGENT: Security Alert")

    print("Pending Notifications:")

    system.notification_queue.display_pending()

    print("\nProcessing 3 notifications...")

    system.batch_process(3)

    print("\nRecent Activities:")

    system.recent_activities.display_recent(5)

    print("\nSystem Stats:")

    print(system.get_stats())