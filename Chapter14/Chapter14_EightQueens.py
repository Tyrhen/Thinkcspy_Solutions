"""
This is the Eight Queens Puzzle in Chapter 14 of How to Think like a CS

Objective:
find locations of were n number of queens can exist on a chess board
without being able to attack one another
"""

from unit_tester import test


def share_diagonal(x0, y0, x1, y1):
    """Compute if two coordinates are diagonal to each other"""
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    return dx == dy


def col_clashes(bs, c):
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False


def has_clashes(chess_board):
    """Determine whether we have any queens clashing on the diagonals.
    We're assuming here that the_board is a permutation of column
    numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(chess_board)):
        if col_clashes(chess_board, col):
            return True
    return False


def main(x):
    """returns unique solutions to the Queen Placement Problem
    given size of the board"""
    import random
    import time

    rng = random.Random()
    bd = list(range(x))
    num_found = 0
    tries = 0
    found_solutions = []

    t0 = time.process_time()
    while num_found < 50:
        rng.shuffle(bd)
        tries += 1

        if not has_clashes(bd) and bd not in found_solutions:
            print("Found unique solution {0} in {1} tries".format(bd, tries))
            num_found += 1
            found_solutions.append(list(bd))

            tries = 0

    t1 = time.process_time()
    print("{0} solutions found in {1} seconds".format(num_found, t1 - t0))


def test_suite():
    print("\n share diagonals")
    test(not share_diagonal(5, 2, 2, 0))
    test(share_diagonal(5, 2, 3, 0))
    test(share_diagonal(5, 2, 4, 3))
    test(share_diagonal(5, 2, 4, 1))

    print("\n Column Clashes")
    test(not col_clashes([6, 4, 2, 0, 5], 4))
    test(not col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7))
    test(col_clashes([0, 1], 1))
    test(col_clashes([5, 6], 1))
    test(col_clashes([6, 5], 1))
    test(col_clashes([0, 6, 4, 3], 3))
    test(col_clashes([5, 0, 7], 2))
    test(not col_clashes([2, 0, 1, 3], 1))
    test(col_clashes([2, 0, 1, 3], 2))

    print("\n Column Clashes")
    test(not has_clashes([6, 4, 2, 0, 5, 7, 1, 3]))
    test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]))
    test(has_clashes([0, 1, 2, 3]))
    test(not has_clashes([2, 0, 3, 1]))
