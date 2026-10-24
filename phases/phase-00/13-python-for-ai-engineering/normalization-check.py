"""Show why feature statistics must be fit on training data only."""

from math import sqrt


def population_stats(values: list[float]) -> tuple[float, float]:
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return mean, sqrt(variance)


train = [1.0, 2.0, 3.0]
test = [100.0]

print("train only:", population_stats(train))
print("train plus test:", population_stats(train + test))
