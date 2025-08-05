def factorial(n, nivel=0):
    print("  " * nivel + f"factorial({n})")
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1, nivel + 1)

print(factorial(5))

