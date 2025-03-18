import random
import math


def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    dim = len(bounds)
    current = [random.uniform(bounds[d][0], bounds[d][1]) for d in range(dim)]
    current_value = func(current)

    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break

        neighbor = [current[d] + random.uniform(-0.5, 0.5) for d in range(dim)]
        neighbor = [
            max(min(neighbor[d], bounds[d][1]), bounds[d][0]) for d in range(dim)
        ]
        neighbor_value = func(neighbor)

        delta = neighbor_value - current_value
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temp):
            current, current_value = neighbor, neighbor_value

    return current, current_value
