import random


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best = [random.uniform(bounds[d][0], bounds[d][1]) for d in range(dim)]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(bounds[d][0], bounds[d][1]) for d in range(dim)]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

        if best_value < epsilon:
            break

    return best, best_value
