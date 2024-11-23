def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        real_part = -b / (2*a)
        imag_part = -discriminant**0.5 / (2*a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        return (root1, root2)
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
    
def heron_formula(a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

    

#test the functions
if __name__ == '__main__':
    print(factorial_recursive(5))
    print(quadratic_roots(1, -3, 2))
    print(heron_formula(3, 4, 5))
    print(fibonacci(10))