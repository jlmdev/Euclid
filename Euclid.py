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


def euclid_extended_algorithm(a, b):
    return_list = []
    if a == 0:
        return b, 0, 1
    gcd, temp_y, temp_x = euclid_extended_algorithm(b % a, a)
    x = temp_x - (b // a) * temp_y
    y = temp_y
    return gcd, x, y


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
    first = int(input('First number: '))
    second = int(input('Second number: '))
    ee = euclid_extended_algorithm(first, second)
    print(f'gcd: {ee}')
    input('*** press enter to continue ***')


def select_task():
    choice = input('What would you like to do?\n')
    if choice == 'gcd':
        gcd_io()
    if choice == 'gs':
        gcd_steps_io()
    if choice == 'ee':
        euclid_extended_algorithm_io()
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
