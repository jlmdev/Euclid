# Euclid Algorithms
# jlmdev


def euclid_gcd(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    gcd = b
    return gcd
