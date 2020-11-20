"""Select Chapter 8 Problems from How to Think Like a Computer Scientist"""
import string

# p2
def prefix_suffix_modify():
    """attaches different prefixes to a suffix with a special condition
    for the 'Q' and 'O' prefixes"""
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


# p3
def count_letters(word, letter):
    """Counts the number of instances of a letter in a string"""
    assert isinstance(word, str) == True, "Please input a string!"
    count = 0
    for char in word:
        if char == letter:
            count += 1

    return count


# P4
def count_letters_mod(word, letter, index=0):
    """counts the number of instances of a letter in a string using the
    Find string method"""
    count = 0
    while index < len(word):
        result = word.find(letter, index)
        if result != -1:
            count += 1
            index = result + 1
        else:
            index += 1

    return count


# P5
def letter_text_analyzer(text, letter):
    """This function parses a string for the number of words that contain
    a certain letter"""
    count = 0
    text_mod = ""
    for char in text:
        if char not in string.punctuation:
            text_mod += char
    text_split = text_mod.split()

    for word in text_split:
        if letter in word:
            count += 1
    result = "Your text contains {0} words,of which {1} ({2:.1%}) contain an '{3}'"

    return result.format(len(text_split), count, count / len(text_split), letter)


# P6
def times_table_6x6(x):
    """displays a times table for numbers up to 12"""
    assert x > 12 == False, "The highest value of input is 12"
    layout = ""
    index = 0
    while x > index:
        layout += "{%s:>4}" % index
        index += 1

    for i in range(1, x + 1):
        print(
            layout.format(
                i * 1,
                i * 2,
                i * 3,
                i * 4,
                i * 5,
                i * 6,
                i * 7,
                i * 8,
                i * 9,
                i * 10,
                i * 11,
                i * 12,
            )
        )


# p7
def string_reverse(text):
    """reverses the spelling/order of a string"""
    rev_text = text[::-1]
    return rev_text


# p8
def string_mirror(text):
    """reverses the spelling/order of a string and adds it the end of the
    unaltered string"""
    rev_text = text[::-1]
    mirror_text = text + rev_text
    return mirror_text


# p9
def string_letter_removal(word, letter):
    """removes all the instances of a letter from a word"""
    text_mod = ""
    for char in word:
        if char != letter:
            text_mod += char
    return text_mod


# P10
def string_palidrome(word):
    """Confirms whether or not a word is a palidrome (the same word when
    reversed)"""
    if word == string_reverse(word):
        return True
    else:
        return False


# P11
def string_substring_count(
    word,
    letter,
):
    """counts the number of occurences of a substring in a string using the
    Find string method. Works exactly like thecount_letters_mod fuction
    I made"""
    count = 0
    index = 0
    while index < len(word):
        result = word.find(letter, index)
        if result != -1:
            count += 1
            index = result + 1
        else:
            index += 1

    return count


# P12
def string_substring_removal_first(string, substring):
    """ remove only the first instance of a substring in a string"""
    result = string.replace(substring, "", 1)
    return result


# P13
def string_substring_removal_all(string, substring):
    """ remove all instances of a substring from a string"""
    result = string.replace(substring, "")
    return result


"""--------------------------------------------------------------------------"""
import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} passed".format(linenum)
    else:
        msg = "Test at line {0} failed".format(linenum)
    print(msg)


def test_suite():

    # p3
    print("Test Suite P1")
    test(count_letters("banana", "a") == 3)
    test(count_letters("playstation", "a") == 2)
    test(count_letters("", "a") == 0)

    # p4
    print("\nTest Suite P2")
    test(count_letters_mod("banana", "a", index=0) == 3)
    test(count_letters_mod("playstation", "a", index=3) == 1)
    test(count_letters_mod("", "a", index=0) == 0)

    # p7
    print("\nTest Suite P7")
    test(string_reverse("happy") == "yppah")
    test(string_reverse("Python") == "nohtyP")
    test(string_reverse("a") == "a")

    # p8
    print("\nTest Suite P8")
    test(string_mirror("good") == "gooddoog")
    test(string_mirror("Python") == "PythonnohtyP")
    test(string_mirror("s") == "ss")

    # p9
    print("\nTest Suite P9")
    test(string_letter_removal("banana", "a") == "bnn")
    test(string_letter_removal("playstation", "a") == "plysttion")
    test(string_letter_removal("a", "a") == "")

    # p10
    print("\nTest Suite P10")
    test(string_palidrome("racecar") == True)
    test(string_palidrome("banana") == False)
    test(string_palidrome("a") == True)

    # p11
    print("\nTest Suite P11")
    test(string_substring_count("banana", "an") == 2)
    test(string_substring_count("mississippi", "is") == 2)
    test(string_substring_count("aaaaaa", "aaa") == 4)

    # p12
    print("\nTest Suite P12")
    test(string_substring_removal_first("banana", "an") == "bana")
    test(string_substring_removal_first("bicycle", "cyc") == "bile")
    test(string_substring_removal_first("mississippi", "iss") == "missippi")

    # p13
    print("\nTest Suite P13")
    test(string_substring_removal_all("banana", "an") == "ba")
    test(string_substring_removal_all("bicycle", "cyc") == "bile")
    test(string_substring_removal_all("mississippi", "iss") == "mippi")


test_suite()
