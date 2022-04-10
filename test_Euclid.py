from Euclid import euclid_gcd


def test_euclid_gcd():
    prime1 = 17
    prime2 = 23
    gcd_result = euclid_gcd(prime1, prime2)
    assert gcd_result == 1
