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


def euclid_gcd_with_steps(a, b):
    r_list = [a, b]
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
        r_list.append(r)
    return r_list


def euclid_extended_algorithm(x, n):
    """
    gcd(x, n)
    sx + tn = 1
    sx - 1 = -tn
    if gcd = 1, s % n is multiplicative inverse of x if positive.
    if negative, add t to n to get multiplicative inverse.
    :param x: x
    :param n: n
    :return:
    """
    if x == 0:
        return n, 0, 1
    gcd, temp_n, temp_s = euclid_extended_algorithm(n % x, x)
    s = temp_s - (n // x) * temp_n
    t = temp_n
    return gcd, s, t


def multiplicative_inverse(s, n):
    multi_inv = 0
    if s < 0:
        multi_inv = (s % n)
    else:
        multi_inv = (s % n)
    return multi_inv


def menu():
    print('------- Menu --------')
    print('gcd: gcd')
    print('gs: gcd with intermediate steps shown')
    print('ee: Euclid Extended Algorithm')
    print('rsa: Simplified RSA Keys')
    print('e: exit')


def gcd_steps_io():
    print('')
    first = int(input('First number: '))
    second = int(input('Second number: '))
    steps_list = euclid_gcd_with_steps(first, second)
    for number in steps_list:
        print(number, end=' ')
    print()
    input('*** press enter to continue ***')


def gcd_io():
    print('')
    first = int(input('First number: '))
    second = int(input('Second number: '))
    gcd = euclid_gcd(first, second)
    print(f'gcd: {gcd}')
    input('*** press enter to continue ***')


def euclid_extended_algorithm_io():
    print('')
    x = int(input('First number (x): '))
    n = int(input('Second number (n): '))
    gcd, s, t = euclid_extended_algorithm(x, n)
    print('sx + tn = 1')
    print('sx - 1 = -tn')
    print(f'gcd: {gcd}')
    print(f's: {s}')
    print(f't: {t}')
    multi_inv = multiplicative_inverse(s, n)
    print(f'Multiplicative inverse of x: {multi_inv}')
    input('*** press enter to continue ***')


def rsa_keys():
    p = int(input('Enter p: '))
    q = int(input('Enter q: '))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = int(input('Enter e: '))
    # check that e and phi are relatively prime
    if euclid_gcd(e, phi) == 1:
        gcd, s, t = euclid_extended_algorithm(e, phi)
        print(f'Public Key: N = {p * q}, e = {e}')
        print(f'Private Key: {s}')
        m = int(input('Enter message number: '))
        c = (m ** e) % n
        print(f'Encrypted message: {c}')
        d = (c ** s) % n
        print(f'Decrypted message: {d}')
        input('*** press enter to continue ***')


def select_task():
    choice = input('What would you like to do?\n')
    if choice == 'gcd':
        gcd_io()
    if choice == 'gs':
        gcd_steps_io()
    if choice == 'ee':
        euclid_extended_algorithm_io()
    if choice == 'rsa':
        rsa_keys()
    if choice == 'e':
        return 'e'


def main():
    while True:
        menu()
        task = select_task()
        if task == 'e':
            break


if __name__ == '__main__':
    main()
