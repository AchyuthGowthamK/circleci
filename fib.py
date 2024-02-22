def fibonacci(limit):
    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= limit:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example usage:
limit = 100  # Change this value to set the limit
fib_series = fibonacci(limit)
print("Fibonacci series up to", limit, ":", fib_series)
