"""
Chapter 14 Exercise from How to think like a CS
"""

from unit_tester import test

# P.1A
def merge_common(xs, ys):
    """ returns a list of common values contained in both arrays """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            yi += 1

        elif xs[xi] < ys[yi]:
            xi += 1

        else:
            yi += 1


# P.1B
def merge_unique_first(xs, ys):
    """ returns a list of values unique to the 1st array when both are merged """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1

        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            yi += 1


# P1.C
def merge_unique_second(xs, ys):
    """ returns a list of values unique to the 2nd array when both are merged"""
    result = []
    xi = 0
    yi = 0
    xs, ys = ys, xs

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            xi += 1

        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            yi += 1


# P1.D
def merge_all(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            result.append(ys[yi])
            yi += 1


# P1.E
def merge_bagdiff(xs, ys):
    """ returns the numbers that would not be elimated by a matching element in the 2nd array """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] == ys[yi]:
            if xs[xi - 1] == ys[yi]:
                result.append(xs[xi])
            xi += 1

        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            yi += 1


# P5.A
def lotto_draw():
    """creates a randomized list of numbers to simulate a random lotto draw"""
    import random

    rng = random.Random()

    lotto = []

    while len(lotto) <= 6:
        lotto.append(rng.randint(1, 49))

    return lotto


# P5.B
def lotto_match(xs, ys):
    """ returns the count of the number of correct picks"""
    xs.sort()
    ys.sort()

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            return len(result)

        if yi >= len(ys):
            return len(result)

        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            yi += 1

        elif xs[xi] < ys[yi]:
            xi += 1

        else:
            yi += 1


# P5.C
def lotto_matches(lotto, my_tickets):
    """returns a list of the the number of correct picks per ticket"""
    result = []

    for ticket in my_tickets:
        match = lotto_match(lotto, ticket)
        result.append(match)

    return result


# P5.D
def count_primes_in(array):
    """returns the number of prime numbers in an array"""
    results = []

    for num in array:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                results.append(num)
    return len(results)


# P5.E
def list_primes_in(array):
    """ returns a list of the prime numbers in an array"""
    results = []

    for num in array:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                results.append(num)
    return results


def prime_misses(my_ticket):
    """returns a list of the prime numbers in the lotto that were
    not guessed"""
    result = []

    lotto_nums = lotto_draw()
    only_prime_lotto_nums = list_primes_in(lotto_nums)

    for ticket in my_ticket:
        missed_primes = merge_unique_first(only_prime_lotto_nums, ticket)
        result.extend(missed_primes)

    unique_misses = set(result)
    list_unique_misses = list(unique_misses)

    print(list_unique_misses)
    return list_unique_misses


def test_suite():
    print("\n P1.A Merge Common Items")
    test(merge_common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4])
    test(merge_common([1, 2, 3, 4], [5, 6, 7, 8]) == [])
    test(merge_common([1, 2, 4], [4, 5, 6, 7, 8]) == [4])

    print("\n P1.B Merge unique items in the 1st array")
    test(merge_unique_first([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2])
    test(merge_unique_first([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4])
    test(merge_unique_first([1, 2, 4, 33], [4, 5, 6, 7, 8]) == [1, 2, 33])

    print("\n P1.C Merge unique items in the 2nd array")
    test(merge_unique_second([1, 2, 3, 4], [3, 4, 5, 6]) == [5, 6])
    test(merge_unique_second([1, 2, 3, 4], [5, 6, 7, 8]) == [5, 6, 7, 8])
    test(merge_unique_second([1, 2, 4, 33], [4, 5, 6, 7, 8]) == [5, 6, 7, 8])

    print("\n P.1D Merge Common Items")
    test(merge_all([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2, 3, 3, 4, 4, 5, 6])
    test(merge_all([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8])
    test(merge_all([1, 2, 4], [4, 5, 6, 7, 8]) == [1, 2, 4, 4, 5, 6, 7, 8])

    print("\n P.1E Merge Bagdiff")
    test(merge_bagdiff([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2])
    test(merge_bagdiff([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4])
    test(merge_bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])

    print("\n P5.B Lotto Match")
    my_tickets = [
        [7, 17, 37, 19, 23, 43],
        [7, 2, 13, 41, 31, 43],
        [2, 5, 7, 11, 13, 17],
        [13, 17, 37, 19, 23, 43],
    ]
    test(lotto_match([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3)
    test(lotto_match([42, 4, 7, 11, 1, 13], [2, 5, 8, 12, 14, 17]) == 0)

    print("\n P5.C Lotto Match")
    test(lotto_matches([42, 4, 7, 11, 1, 13], my_tickets) == [1, 2, 3, 1])
    test(lotto_matches([43, 4, 7, 11, 1, 13], my_tickets) == [2, 3, 3, 2])
    test(lotto_matches([10, 6, 8, 18, 20, 14], my_tickets) == [0, 0, 0, 0])

    print("\n P5.D Count Prime")
    test(count_primes_in([42, 4, 7, 11, 1, 13]) == 3)
    test(count_primes_in([42, 4, 8, 21, 1, 14]) == 0)

    print("\n P5.E Prime Missed")

    test(prime_misses(my_tickets))
    test(prime_misses(my_tickets))


test_suite()
