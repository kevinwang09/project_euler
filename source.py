## Primality test function from wikipedia
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

## list all prime factors, with repeats
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def triangular(n: int):
    return(n*(n+1)/2)

def pentagonal(n: int):
    return(n*(3*n-1)/2)

def hexagonal(n: int):
    return(n*(2*n-1))

def solve_quad(a: int, b: int, c: int):
    root1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    if(root1>=0):
        return(root1)
    else: 
        return((-b-math.sqrt(b**2-4*a*c))/(2*a))