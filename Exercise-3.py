import math
import random


def count_cross_edges(groupA, groupB, graph):
    """Counts the number of friendships severed between the two groups."""
    cross_edges = 0
    for u in groupA:
        if u in graph:
            for v in graph[u]:
                if v in groupB:
                    cross_edges += 1
    return cross_edges

def find_balanced_partition_greedy(graph):
    """Finds a local optimum by making single-node swaps."""
    nodes = list(graph.keys())
    N = len(nodes)
    
    
    if N < 2:
        return 0, set(nodes), set()

    # Calculate 40% balance constraint
    min_size = math.ceil(0.4 * N)
    
    # Start with a random valid split
    shuffled = nodes.copy()
    random.shuffle(shuffled)
    split_idx = random.randint(min_size, N - min_size)
    
    groupA = set(shuffled[:split_idx])
    groupB = set(shuffled[split_idx:])
    
    current_cross_edges = count_cross_edges(groupA, groupB, graph)
    improvement = True
    
   
    while improvement:
        improvement = False
        best_move_node = None
        best_source = None
        best_target = None
        best_cross_edges = current_cross_edges
        
        for node in nodes:
            # Try moving from A to B
            if node in groupA and len(groupA) - 1 >= min_size:
                groupA.remove(node)
                groupB.add(node)
                edges = count_cross_edges(groupA, groupB, graph)
                
                if edges < best_cross_edges:
                    best_cross_edges = edges
                    best_move_node = node
                    best_source = groupA
                    best_target = groupB
                    
                # Revert move to test the next node
                groupB.remove(node)
                groupA.add(node)
                
          
            elif node in groupB and len(groupB) - 1 >= min_size:
                groupB.remove(node)
                groupA.add(node)
                edges = count_cross_edges(groupA, groupB, graph)
                
                if edges < best_cross_edges:
                    best_cross_edges = edges
                    best_move_node = node
                    best_source = groupB
                    best_target = groupA
                    
            
                groupA.remove(node)
                groupB.add(node)
        
        
        if best_move_node is not None:
            best_source.remove(best_move_node)
            best_target.add(best_move_node)
            current_cross_edges = best_cross_edges
            improvement = True
            
    return current_cross_edges, groupA, groupB


def find_balanced_partition_local_search(graph, iterations):
    """Runs the greedy algorithm multiple times to escape local minima."""
    best_cross_edges = float('inf')
    best_groupA = None
    best_groupB = None
    
    for _ in range(iterations):
        edges, groupA, groupB = find_balanced_partition_greedy(graph)
        
        if edges < best_cross_edges:
            best_cross_edges = edges
            best_groupA = groupA.copy()
            best_groupB = groupB.copy()
            
    return best_cross_edges, best_groupA, best_groupB


if __name__ == "__main__":
    
    social_graph = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3]
    }
    
    total_users = len(social_graph)
    min_required = math.ceil(0.4 * total_users)
    
    
    print(" LAB 10: GROUP FORMATION - MINIMIZE EXTERNAL FRIENDS")
    
    print(f"Total Users: {total_users}")
    print(f"Balance Constraint (40%): Minimum {min_required} users per team")
    print("\nRunning Local Search (10 iterations)...\n")
    
    
    final_edges, final_team_a, final_team_b = find_balanced_partition_local_search(social_graph, iterations=10)
    
  
    print("=== OPTIMAL TEAM SPLIT ===")
    print(f"Team A Members: {list(final_team_a)}")
    print(f"Team B Members: {list(final_team_b)}")
    print(f"\nSevered Friendships (Cross-Edges): {final_edges}")
    
    print("Success: Teams are balanced and friendships are maximized within constraints.")
    
