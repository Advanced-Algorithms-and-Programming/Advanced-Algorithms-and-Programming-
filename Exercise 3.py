def is_within_budget(selection, costs, budget):

    total_cost = 0

    for user in selection:
        total_cost += costs[user]

    return total_cost <= budget


def maximize_reach(budget, costs, influences):

    n = len(costs)

    # DP table
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        for b in range(budget + 1):

            if costs[i - 1] <= b:

                include = influences[i - 1] + dp[i - 1][b - costs[i - 1]]
                exclude = dp[i - 1][b]

                dp[i][b] = max(include, exclude)

            else:
                dp[i][b] = dp[i - 1][b]

    selected_users = []
    b = budget

    for i in range(n, 0, -1):

        if dp[i][b] != dp[i - 1][b]:

            selected_users.append(i - 1)
            b -= costs[i - 1]

    selected_users.reverse()

    return dp[n][budget], selected_users


def fast_alternative_strategy(budget, costs, influences):

    n = len(costs)

    users = []

    for i in range(n):

        ratio = influences[i] / costs[i]
        users.append((ratio, i))
    users.sort(reverse=True)

    total_cost = 0
    total_influence = 0
    selected = []

    for ratio, i in users:

        if total_cost + costs[i] <= budget:

            selected.append(i)
            total_cost += costs[i]
            total_influence += influences[i]

    return total_influence, selected

budget = 50
costs = [10, 20, 30]
influences = [60, 100, 120]


max_inf, selected_users = maximize_reach(
    budget,
    costs,
    influences
)

print("Exact DP Solution")
print("Maximum Influence:", max_inf)
print("Selected Users:", selected_users)


greedy_inf, greedy_users = fast_alternative_strategy(
    budget,
    costs,
    influences
)

print("\nGreedy Approximation")
print("Maximum Influence:", greedy_inf)
print("Selected Users:", greedy_users)