def generate_fibonacci(n : int) -> list:
    if n == 0 : return []
    if n == 1 : return [0]
    a = [0, 1]
    p = 0
    for i in range(1, n-1, 1):
        a.append(a[i-1] + a[i])
    return a


print(generate_fibonacci(10))
    