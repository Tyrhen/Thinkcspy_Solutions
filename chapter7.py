"""Select Chapter 7 Problems from How to Think Like a Computer Scientist"""

    
#p1
def odd_number_count(array):
    """counts only the odd numbers in an array"""
    count = 0
    for i in array:
        if i %2 != 0:
            count+=1
    return count

#p2
def even_num_sum(array):
    """sums only the even numbers in an array""" 
    even_nums = list(filter(lambda x: x%2==0,array))
    return sum(even_nums)

#p3
def five_letters(array):
    """counts all the items in an array that have a length of 5"""
    five_letter_words = list(filter(lambda x: len(x)==5,array))
    return len(five_letter_words)

#P4
def sum_negative_num(array):
    negative_values = list(filter(lambda x: x<0, array))
    return sum(negative_values)

#P5
def sum_exclude_first_even(array):
    """sums an array up to the first even number"""
    total = 0 
    for i in array:
        if i % 2 != 0:
            total += i
        else:
            return total
    return total

#P6
def count_until_keyword(array,keyword):
    count = 0
    for word in array:
        if word != keyword:
            count +=1
        else:
            count+=1
            return count 
    return count

#p7
def newton_sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

#P8
def triangular_nums(n):
    for i in range(1,n+1):
        print('{0}    {1}'.format(i,i*(i+1)/2))

#P10
def is_prime(n):
    if n in [0,1,2]:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    
    return True

#P15

def num_even_digits(array):
    
    str_int = list(map(lambda x:int(x), str(array)))
    even_digits = list(filter(lambda x: x%2 == 0, str_int))
    return len(even_digits)

def sum_of_squares(array):
    sum = 0
    for num in array:
        num_sq = num**2
        sum += num_sq
    return sum
    
"""--------------------------------------------------------------------------"""
import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} success'.format(linenum)
    else:
        msg = 'Test at line {0} failed'.format(linenum)
    print(msg)

def test_suite():
    """test suite for select chapter 7 problems"""

    #test suite for P1
    print('test suite P1')
    test((odd_number_count([1,3,5,6,7,8]) == 4))
    test((odd_number_count([0,11,1,3,5,6,7,8]) == 5))
    test((odd_number_count([1,4,5,6,7,8]) == 3))

    #test suite for P2
    print('-----test suite P2-----')
    test((even_num_sum([1,2,3,4,5]) == 6))

    #test suite for P3
    print('-----test suite P3-----')
    test((five_letters(['hello','goodbye','welcome','ammie']) ==2))
    test((five_letters([]) == 0))
    test((five_letters(['11111']) == 1))

    #test suite for P4
    print('-----test suite P4-----')
    test(sum_negative_num([-1,1,3,-2,4])==-3)
    test(sum_negative_num([1])==0)
    test(sum_negative_num([])==0)

    #test suite for P5
    print('-----test suite P5-----')
    test((sum_exclude_first_even([1,3,5,2]) == 9))
    test((sum_exclude_first_even([1,3,5,7]) == 16))
    test((sum_exclude_first_even([2,3,5,2]) == 0))

    #test suite for P6
    print('-----test suite P6-----')
    test(count_until_keyword(['mike','ike','ty','sam','ko'],'sam')==4)
    test(count_until_keyword(['sam','ike','ty','sam','ko'],'sam')==1)
    test(count_until_keyword(['ike','ty','ko'],'sam')==3)
    
    #test suite for P7
    print('-----test suite P6-----')
    (newton_sqrt(49.0))
    (newton_sqrt(25))
    (newton_sqrt(81.0))

    #test suite for p9
    print('-----test suite P9-----')
    (triangular_nums(4))
    (triangular_nums(5))
    (triangular_nums(6))  

    #test suite for p10
    print('-----test suite P10-----')
    test(is_prime(5)==True)
    test(is_prime(10)==False)
    test(not is_prime(10)== True)
    test(is_prime(1)==True)

    #test suite for p15
    print('-----test suite P15-----')
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    

    #test suite for p16
    print('-----test suite P16-----')
    test(sum_of_squares([2,3,4])==29)
    test(sum_of_squares([]) == 0)
    test(sum_of_squares([2,-3,4]) == 29)
    

test_suite()
