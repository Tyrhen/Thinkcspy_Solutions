
import string
#p2
def prefix_suffix_modify():
    """attaches different prefixes to a suffix with a special condition
        for the 'Q' and 'O' prefixes"""
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter+'u'+suffix)
        else:
            print(letter + suffix)

#p3
def count_letters(word,letter):
    """Counts the number of instances of a letter in a string"""
    assert isinstance(word,str)==True, "Please input a string!"
    count = 0
    for char in word:
        if char == letter:
            count+=1

    return count

#P4
def count_letters_mod(word,letter,index=0):
    """counts the number of instances of a letter in a string using the
        Find string method"""
    count = 0
    while index < len(word):
        result = word.find(letter,index)
        if result != -1:
            count+=1
            index = result+1
        else:
            index+=1

    return count

#P5
def letter_text_analyzer(text,letter):
    """This function parses a string for the number of words that contain
        a certain letter"""
    count = 0
    text_mod = ''
    for char in text:
        if char not in string.punctuation:
            text_mod += char
    text_split = text_mod.split()

    for word in text_split:
        if letter in word:
            count += 1
    result = "Your text contains {0} words,of which {1} ({2:.1%}) contain an '{3}'"
    
    return result.format(len(text_split),count,
                        count/len(text_split),letter)

#P6
def times_table_6x6(x):
    layout =""
    index = 0
    while x>index:
        layout+='{%s:>4}'%index
        index+=1

     
    for i in range(1,x+1):
        print(layout.format(i*1,i*2,i*3,i*4,i*5,i*6,
                            i*7,i*8,i*9,i*10,i*11,i*12))
#p7
def string_reverse(text):
    rev_text = text[::-1]
    return rev_text

#p8
def string_mirror(text):
    rev_text = text[::-1]
    mirror_text = text+rev_text
    return mirror_text

#p9
def string_letter_removal(word,letter):
    text_mod = ''
    for char in word:
        if char != letter:
            text_mod+= char
    return text_mod

#P10
def string_palidrome(word):
    if word == string_reverse(word):
        return True
    else:
        return False


#P11
def string_substring_count(word,letter,index=0):
    """counts the number of occurences of a substring in a string using the
        Find string method. Works exactly like thecount_letters_mod fuction
        I made"""
    count = 0
    while index < len(word):
        result = word.find(letter,index)
        if result != -1:
            count+=1
            index = result+1
        else:
            index+=1

    return count

#P12
def string_substring_removal_first(string,substring):
    result = string.replace(substring,'',1)
    return result

#P13
def string_substring_removal_all(string,substring):
    result = string.replace(substring,'')
    return result
    


