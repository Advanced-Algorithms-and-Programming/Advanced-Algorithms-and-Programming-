class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_username = False
        self.user_id = None

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, username, user_id):
        current = self.root
        for char in username:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_username = True
        current.user_id = user_id

    def search(self, username):
        current = self.root
        for char in username:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.user_id if current.is_end_of_username else None

    def autocomplete(self, prefix, max_results=10):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # Prefix not found
        
        results = []
        self._dfs(current, prefix, results, max_results)
        return results

    def _dfs(self, node, current_string, results, max_results):
        if len(results) >= max_results:
            return
        if node.is_end_of_username:
            results.append((current_string, node.user_id))
        for char, child_node in sorted(node.children.items()): # Sorted for consistent output
            self._dfs(child_node, current_string + char, results, max_results)


class ActivitySegmentTree:
    def __init__(self, activity_array):
        self.n = len(activity_array)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self.build(1, 0, self.n - 1, activity_array)

    def build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid, arr)
        self.build(2 * node + 1, mid + 1, end, arr)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        # Out of bounds
        if r < start or l > end:
            return 0
        # Fully inside range
        if l <= start and end <= r:
            return self.tree[node]
        # Partially inside range
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, l, r)
        right_sum = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum

    def get_range_sum(self, l, r):
        # Handle edge cases for out-of-bounds input
        l, r = max(0, l), min(self.n - 1, r) 
        if l > r: return 0
        return self.query(1, 0, self.n - 1, l, r)


if __name__ == "__main__":
    print(" PART A: TRIE TEST CASES ")
    trie = AutocompleteTrie()
    trie.insert("alice", 1)
    trie.insert("bob", 2)
    trie.insert("ali", 3)
    trie.insert("alice123", 4)
    
    print(f"1. Search 'alice': User ID {trie.search('alice')}")
    print(f"2. Autocomplete 'ali' (max 5): {trie.autocomplete('ali', 5)}")
    print(f"3. Autocomplete 'ali' (max 2): {trie.autocomplete('ali', 2)}")
    print(f"4. Autocomplete 'zane' (no match): {trie.autocomplete('zane', 5)}")
    print(f"5. Autocomplete '' (empty prefix): {trie.autocomplete('', 3)}")

    print("\nPART B: SEGMENT TREE TEST CASES ")
    activities = [10, 20, 30, 40, 50, 60, 70]
    print(f"Initial Activity Array: {activities}")
    st = ActivitySegmentTree(activities)
    
    print(f"1. Range Query Days 1-3 (20+30+40): {st.get_range_sum(1, 3)}")
    print(f"2. Single Day Query Day 4: {st.get_range_sum(4, 4)}")
    print(f"3. Entire Range Query Days 0-6: {st.get_range_sum(0, 6)}")
    print(f"4. Out of Bounds Query Days -1 to 10: {st.get_range_sum(-1, 10)}")
