def gcd(a: int, b: int):
    while b!= 0:
        t = b
        b = a % b
        a = t
    return(a)

def lcm(a: int, b: int):
    result = (a * b)/gcd(a, b)
    return(result)