"""Select problems from Chapter 11 'How to Think Like a Computer Scientist'"""

import sys

#P5
def add_vectors(u,v):
    """returns the sum of two vectors in matrix format"""
    result = []
    for i in range(len(u)):
        sum = u[i] + v[i]
        result.append(sum)
    return result
        
#P6
def scalar_mult(s,m):
    """returns a scaled matrix given the scalar factor and a matrix"""
    result = []
    for i in range(len(m)):
        scaled = s*m[i]
        result.append(scaled)
    return result

#P7
def dot_product(u,v):
    """returns the dot product of two matrices"""
    result = []
    for i in range(len(u)):
        product = u[i] * v[i]
        result.append(product)
    return sum(result)

#P8
def cross_product(u,v):
    """returns the cross product of two matrices that have 3 elements"""
    result = [u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2],
              u[0]*v[1] - u[1]*v[0]]
    return result

#P10
def replace(s,old,new):
    """replaces all occurences of a user defined value with another"""
    result = ''
    for letter in s:
        if letter == old:
            letter = new
        result += letter
    return result
        
"""--------------------------------------------------------------------------"""

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} Pass'.format(linenum)
    else:
        msg = 'Test at line {0} Failed'.format(linenum)
    print(msg)
  
def test_suite():
    #P5
    print('\nP5 Test Suite')
    test(add_vectors([1,1],[1,1])==[2,2])
    test(add_vectors([1,2],[1,4])==[2,6])
    test(add_vectors([1,2,1],[1,4,3])==[2,6,4])
    #P6
    print('\nP6 Test Suite')
    test(scalar_mult(5,[1,2])==[5,10])
    test(scalar_mult(3,[1,0,-1])==[3,0,-3])
    test(scalar_mult(7,[3,0,5,11,2])==[21,0,35,77,14])
    #P7
    print('\nP7 Test Suite')
    test(dot_product([1,1],[1,1])== 2)
    test(dot_product([1,2],[1,4])== 9)
    test(dot_product([1,2,1],[1,4,3])== 12)

    #P8
    print('\nP8 Test Suite')
    test(cross_product([5,2,1],[1,4,3])== [2,-14,18])
    test(cross_product([3,4,2],[1,4,3])== [4,-7,8])
    test(cross_product([1,2,1],[1,4,3])== [2,-2,2])

    #P10
    print('\nP10 Test Suite')
    test(replace('Mississippi','i','I')=='MIssIssIppI')
    test(replace('Mississippi','p','P')=='MississiPPi')
    test(replace('Playstation5','a','')=='Plysttion5')
    
    
    
              
test_suite()
      
