import heapq


def minimum_cost_to_connect_cables(cables):
    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        cost = cable1 + cable2
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6, 22, 1, 19]
    result = minimum_cost_to_connect_cables(cables)
    print("Minimum cost to connect all cables:", result)
