def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def cosine(n):
    def inner(x):
        x_rad = x * (3.14 / 180)
        cos_value = 0
        for i in range(n):
            term = ((-1) ** i) * (x_rad ** (2 * i)) / factorial(2 * i)
            cos_value += term
        return round(cos_value, 6)
    
    return inner

n, x = map(int, input().split())
cosine_function = cosine(n)

print(cosine_function(x))
