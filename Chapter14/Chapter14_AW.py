"""
Mission: To return a list of words from a text that are not in our vocab

Requirements:
must search through a text to find an item
must return a list of unknown words in a list
must read a file and return its content in a list
"""
from unit_tester import test
import time


def linear_search(array, target):
    """Searchs for an item in a list in a linear fashion"""
    for i, item in enumerate(array):
        if item == target:
            return i
    return -1


def binary_search(array, target):
    """implementation of binary search to find a target item"""
    low = 0
    high = len(array)

    while True:

        if low == high:
            return -1

        mid_index = (high + low) // 2
        mid_item = array[mid_index]

        if mid_item == target:
            return mid_index

        elif mid_item < target:
            low = mid_index + 1

        else:
            high = mid_index


def get_words_in_file(filename):
    """get the words from a file and returns a list of the words free of punctuation"""
    f = open(filename)
    content = f.read()
    f.close()
    words = clean_text(content)
    return words


def clean_text(content):
    """takes a string and returns the punctuation-free lowercase string version in a list"""
    my_substitutions = content.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        "abcdefghijklmnopqrstuvwxyz                                          ",
    )

    cleaned_text = content.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def remove_adjacent_dups(array):
    """ removes adjacent duplicates from a list"""
    no_duplicates = []
    most_recent = None
    for item in array:
        if item != most_recent:
            no_duplicates.append(item)
            most_recent = item

    return no_duplicates


def merge(array1, array2):
    """ merges two sorted list into a single sorted list"""
    array1_pointer = 0
    array2_pointer = 0
    merged = []

    while True:
        if array1_pointer >= len(array1):
            merged.extend(array2[array2_pointer:])
            print(merged)

            return merged
        if array2_pointer >= len(array2):
            merged.extend(array1[array1_pointer:])
            print(merged)

            return merged

        if array1[array1_pointer] <= array2[array2_pointer]:
            merged.append(array1[array1_pointer])
            array1_pointer += 1

        else:
            array1[array1_pointer] > array2[array2_pointer]
            merged.append(array2[array2_pointer])
            array2_pointer += 1


def find_unknown_merge_pattern(vocab, wds):
    """Both the vocab and the words must be sorted. Returns a new list of words from wds that do not occur in vocab"""
    xi = 0
    yi = 0
    result = []
    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:
            yi += 1
        elif vocab[xi] < wds[yi]:
            xi += 1
        else:
            result.append(wds[yi])
            yi += 1


def unknown_words(vocab, text):
    """collects all the words that appear in text that are not in the vocab"""
    unknown = []
    for word in text:
        if binary_search(vocab, word) < 0:
            unknown.append(word)
    return unknown


def test_suite():
    friends = "Joe Zoe Brad Angelina Zuki Thandi Paris".split()
    print("\n Linear Search")
    test(linear_search(friends, "Zoe") == 1)
    test(linear_search(friends, "Joe") == 0)
    test(linear_search(friends, "Paris") == 6)
    test(linear_search(friends, "Bill") == -1)

    print("\n Unknown Words")
    vocab = "apple boy dog down fell girl grass the tree".split()
    book_words = "the apple fell from the tree to the grass".split()
    test(unknown_words(vocab, book_words) == ["from", "to"])
    test(unknown_words([], book_words) == book_words)
    test(unknown_words(vocab, ["the", "boy", "fell"]) == [])

    print("\n clean_text")
    test(clean_text("My name is Earl!") == "my name is earl".split())
    test(clean_text("Well, I never!, said Alice.") == "well i never said alice".split())

    print("\n Binary Search")
    xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
    test(binary_search(xs, 20) == -1)
    test(binary_search(xs, 99) == -1)
    test(binary_search(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        test(binary_search(xs, v) == i)

    print("\n Remove Duplicates")
    test(remove_adjacent_dups([1, 2, 3, 3, 3, 3, 5, 6, 9, 9]) == [1, 2, 3, 5, 6, 9])
    test(remove_adjacent_dups([]) == [])
    test(
        remove_adjacent_dups(["a", "big", "big", "bite", "dog"])
        == ["a", "big", "bite", "dog"]
    )

    print("\n Merge Sorted")
    xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    ys = [4, 8, 12, 16, 20, 24]
    zs = xs + ys
    zs.sort()
    test(merge(xs, []) == [])
    test(merge(xs, ys) == zs)
    test(merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
    test(
        merge(["a", "big", "cat"], ["big", "bite", "dog"])
        == ["a", "big", "big", "bite", "cat", "dog"]
    )


bigger_vocab = get_words_in_file("vocab.txt")
all_words = get_words_in_file("alice_in_wonderland.txt")


t0 = time.process_time()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknown_merge_pattern(bigger_vocab, book_words)
t1 = time.process_time()

print("There are {0} unknown words.".format(len(missing_words)))
print("that took {0:.4f} seconds.".format(t1 - t0))
