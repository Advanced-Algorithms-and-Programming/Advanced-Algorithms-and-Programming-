def maximize_reach_exact(budget, costs, reaches):
    n = len(costs)


    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for b in range(budget + 1):

            # If current user's cost is within budget
            if costs[i - 1] <= b:

                include = reaches[i - 1] + dp[i - 1][b - costs[i - 1]]
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


def is_within_budget(selection, costs, budget):

    total_cost = 0

    for user in selection:
        total_cost += costs[user]

    return total_cost <= budget


def maximize_reach_greedy(budget, costs, reaches):

    users = []


    for i in range(len(costs)):
        ratio = reaches[i] / costs[i]
        users.append((ratio, i, costs[i], reaches[i]))

    users.sort(reverse=True)

    total_cost = 0
    total_reach = 0
    selected_users = []


    for ratio, index, cost, reach in users:

        if total_cost + cost <= budget:

            selected_users.append(index)
            total_cost += cost
            total_reach += reach

    return total_reach, selected_users



costs = [4, 5, 6, 3]
reaches = [40, 50, 60, 30]
budget = 10


exact_reach, exact_users = maximize_reach_exact(
    budget,
    costs,
    reaches
)

print("Exact Solution")
print("Maximum Reach:", exact_reach)
print("Selected Users:", exact_users)


greedy_reach, greedy_users = maximize_reach_greedy(
    budget,
    costs,
    reaches
)

print("\nGreedy Solution")
print("Maximum Reach:", greedy_reach)
print("Selected Users:", greedy_users)



print("\nBudget Validation")
print(
    is_within_budget(
        exact_users,
        costs,
        budget
    )
)