import turtle
from unit_tester import test
import os

# P1-P2 setup
def make_window(colr, ttle):
    """
    Set up the window with the given background color and title.
    Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
    Set up a turtle with the given color and pensize.
    Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    t.penup()
    t.setpos(-100, 0)
    t.pendown()
    t.speed(0)

    return t


# P1
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [
            60,
            -120,
            60,
            0,
        ]:
            koch(t, order - 1, size / 3)
            t.left(angle)


def Koch_snowflake():
    for i in range(3):
        koch(ty, 2, 200)
        ty.right(120)


# P2a
def Cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [
            80,
            -160,
            80,
            0,
        ]:
            Cesaro(t, order - 1, size / 3)
            t.right(angle)


# P2b
def cesaro_square():
    for i in range(4):
        Cesaro(ty, 4, 1000)
        ty.right(90)


# P5
def recursive_min(nested_list):
    smallest = None
    Unvisted = True
    for element in nested_list:
        if type(element) == list:
            val = recursive_min(element)
        else:
            val = element

        if Unvisted or val < smallest:
            smallest = val
            Unvisted = False

    return smallest


# P6
def recursive_count(target, nested_list):
    total = 0
    for element in nested_list:
        if type(element) == list:
            total += recursive_count(target, element)
        elif target == element:
            total += 1

    return total


# P7
def recursive_flatten(nested_list):
    flattened_list = []
    for element in nested_list:
        if type(element) == list:
            element = recursive_flatten(element)
            flattened_list += element
        else:
            flattened_list.append(element)

    return flattened_list


# P8
def NR_Fibonacci(n):
    if n <= 1:
        return n
    else:
        N1 = 0
        N2 = 1
        for i in range(2, n + 1):
            # total = 1 | total = 2 | total = 3
            total = N1 + N2
            # N1 = 1 | N1 = 1 | N1 = 2
            N1 = N2
            # N2 = 1 | N2 = 2 | N2 = 3
            N2 = total
    return total


# P10
def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = []
    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            dirlist.append(os.path.join(dirpath, x))
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)  # Print the line
        fullname = os.path.join(path, f)  # Turn name into full pathname
        if os.path.isdir(fullname):  # If a directory, recurse.
            print_files(fullname, prefix + "| ")


def test_suite():
    print("\n Recursive Min")
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

    print("\n Recursive Count")
    test(recursive_count(2, []) == 0)
    test(recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(
        recursive_count(
            "a", [["this", ["a", ["thing", "a"], "a"], "is"], ["a", "easy"]]
        )
        == 4
    )
    print("\n Recursive Flatten")
    test(
        recursive_flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
        == [2, 9, 2, 1, 13, 2, 8, 2, 6]
    )
    test(
        recursive_flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6]
    )
    test(
        recursive_flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6]
    )

    print("\n Non Recursive Fibonacci")
    test(NR_Fibonacci(1) == 1)
    test(NR_Fibonacci(0) == 0)
    test(NR_Fibonacci(7) == 13)


# test_suite()
