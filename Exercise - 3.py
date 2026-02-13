def merge_intervals(intervals):
    """
    Merges overlapping intervals into a single list of non-overlapping intervals.
    Complexity: Time O(n log n), Space O(n)
    """
    # 1. Handle empty input [cite: 4]
    if not intervals:
        return []

    # 2. Sort intervals based on the starting value [cite: 5]
    
    intervals.sort(key=lambda x: x[0])

    # 3. Initialize the merged list with the first interval [cite: 6, 7]
    merged = []
    current = intervals[0]

    # 4. Iterate through the rest of the intervals [cite: 8]
    for i in range(1, len(intervals)):
        next_interval = intervals[i]

        # Check if the next interval overlaps with the current one [cite: 9]
        if next_interval[0] <= current[1]:
            # Merge by extending the end time [cite: 9]
            current[1] = max(current[1], next_interval[1])
        else:
            # No overlap: add the completed 'current' interval and move to next [cite: 9]
            merged.append(current)
            current = next_interval

    # 5. Add the last remaining interval [cite: 10]
    merged.append(current)
    
    return merged

# --- Test Cases from Source [cite: 43] ---
if __name__ == "__main__":
    test_data = [
        ([[1, 3], [2, 5]], "Overlapping intervals"),
        ([[1, 4], [4, 6]], "Touching intervals"),
        ([[1, 2], [3, 4]], "No overlap"),
        ([[0, 10], [2, 5]], "One inside another"),
        ([], "Empty input"),
        ([[7, 9]], "Single interval")
    ]

    print("--- Exercise 3: Merge Intervals Results ---")
    for data, reason in test_data:
        result = merge_intervals(data)
        print(f"Input: {data:18} | Result: {result:18} | Reason: {reason}")