import functools


@functools.cache
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


def binomial(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


count = 0
for n in range(1, 101):
    for r in range(1, n):
        if binomial(n, r) > 1_000_000:
            count += 1
print(count)
