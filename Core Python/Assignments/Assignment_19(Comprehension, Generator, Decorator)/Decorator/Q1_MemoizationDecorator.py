# 1. Develop a memoization decorator that caches the results of function calls and returns the cached result when the same inputs occur again. This can greatly improve the performance of recursive or computationally intensive functions.

def memoize(func):
    cache = {}  # dictionary to store results
    def wrapper(x):
        if x in cache:
            print("Getting from cache for:", x)
            return cache[x]
        else:
            result = func(x)
            cache[x] = result
            print("Calculating result for:", x)
            return result
    return wrapper

@memoize
def square(n):
    return n * n

print(square(4))
print(square(5))
print(square(4))   # this time result will come from cache