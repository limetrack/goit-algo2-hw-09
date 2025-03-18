import random


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1):
    dim = len(bounds)
    current = [random.uniform(bounds[d][0], bounds[d][1]) for d in range(dim)]
    current_value = func(current)

    for _ in range(iterations):
        neighbor = [
            current[d] + random.uniform(-step_size, step_size) for d in range(dim)
        ]
        neighbor = [
            max(min(neighbor[d], bounds[d][1]), bounds[d][0]) for d in range(dim)
        ]
        neighbor_value = func(neighbor)

        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value

        if abs(current_value - neighbor_value) < epsilon:
            break

    return current, current_value
