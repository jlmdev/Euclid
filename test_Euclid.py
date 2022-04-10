from Euclid import euclid_gcd, euclid_gcd_with_steps, euclid_extended_algorithm


def test_euclid_gcd():
    prime1 = 17
    prime2 = 23
    gcd_result = euclid_gcd(prime1, prime2)
    assert gcd_result == 1


def test_euclid_gcd_with_steps():
    prime1 = 17
    prime2 = 23
    gcd_result = euclid_gcd_with_steps(prime1, prime2)
    assert gcd_result == [6, 5, 1, 0]


def test_euclid_extended_algorithm():
    num1 = 10
    num2 = 25
    extended_algorithm_result = euclid_extended_algorithm(num1, num2)
    assert extended_algorithm_result == (5, -2, 1)
